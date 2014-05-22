from itertools import chain
from easydict import EasyDict
import requests

from soccermetrics import SoccermetricsRestException
from soccermetrics import __api_version__ as API_VERSION

class Resource(object):
    """
    Represents a REST resource.  Sets high-level endpoint for API.

    :param base_uri: Base URI of API.
    :type base_uri: string
    :param auth: Authentication credential.
    :type auth: tuple
    """
    def __init__(self, base_uri, auth):
        self.base_uri = base_uri
        self.auth = auth

        self.endpoint = "/%s" % API_VERSION

    def get(self, uid=None, **kwargs):
        """
        Retrieves a representation of REST resource.

        The response is an object with the following attributes:

        +------------+-----------------------+
        | Attribute  | Description           |
        +============+=======================+
        | headers    | Response headers      |
        +------------+-----------------------+
        | meta       | Response meta-data    |
        +------------+-----------------------+
        | data       | Response data         |
        +------------+-----------------------+

        :param uid: Unique ID of API resource representation.
        :type uid: integer
        :param kwargs: Collection of query parameters.
        :type kwargs: dict
        :returns: Resource representation.
        :rtype: ``EasyDict`` object.
        """
        uri = "%s%s/%d" % (self.base_uri, self.endpoint, uid) if uid else \
            "%s%s" % (self.base_uri, self.endpoint)

        full_param_dict = dict(kwargs, **self.auth)

        try:
            resp = requests.get(uri,params=full_param_dict)
            if resp.status_code == 200:
                return Response(self.base_uri, self.auth, resp)
            else:
                data = resp.json()
                raise SoccermetricsRestException(resp.status_code,data['uri'],data['message'])
        except requests.exceptions.RequestException as e:
            raise SoccermetricsRestException(500, uri, msg=e)

    def head(self):
        """
        Retrieves header data of REST resource.

        The response is an object with the following attribute:

        +------------+-----------------------+
        | Attribute  | Description           |
        +============+=======================+
        | headers    | Response headers      |
        +------------+-----------------------+

        :returns: Header data.
        :rtype: ``EasyDict`` object.
        """
        uri = "%s%s" % (self.base_uri, self.endpoint)

        resp = requests.head(uri,params=self.auth)

        if resp.status_code < 400:
            return EasyDict(dict(headers=resp.headers))
        else:
            raise SoccermetricsRestException(resp.status_code,resp.url)

    def options(self):
        """
        Retrieves documentation of REST resource.

        If the status code is 200 (OK), returns the documentation.  Otherwise,
        returns an error.

        The response is an object with the following attributes:

        +------------+------------------------+
        | Attribute  | Description            |
        +============+========================+
        | headers    | Response headers       |
        +------------+------------------------+
        | data       | Resource documentation |
        +------------+------------------------+

        Link resources are not included in the documentation.

        :returns: Resource documentation data.
        :rtype: ``EasyDict`` object.
        """
        uri = "%s%s" % (self.base_uri, self.endpoint)

        resp = requests.options(uri,params=self.auth)

        if resp.status_code == 200:
            return Response(self.base_uri, self.auth, resp)
        else:
            raise SoccermetricsRestException(resp.status_code,resp.url)


class Link(Resource):
    """
    Access to linked resources, can also access any API endpoint.

    Derived from :class:`Resource`.
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of Link class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(Link, self).__init__(base_uri, auth)

    def get(self, uri, **kwargs):
        """
        Returns a representation of the REST resource.

        Derived from :func:`Resource.get`.

        :param uri: URI of REST resource, relative to base URI.
        :type uri: string
        :param kwargs: Collection of query parameters.
        :type kwargs: dict
        :returns: Resource representation.
        :rtype: ``EasyDict`` object.
        """
        self.endpoint = uri
        return super(Link, self).get(**kwargs)

    def head(self, uri):
        """
        Retrieves header data of REST resource.

        Derived from :func:`Resource.head`.

        :param uri: URI of REST resource, relative to base URI.
        :type uri: string
        :returns: Header data.
        :rtype: ``EasyDict`` object.
        """
        self.endpoint = uri
        return super(Link, self).head()

    def options(self, uri):
        """
        Retrieves documentation of REST resource representation.

        Derived from :func:`Resource.options`.

        :param uri: URI of REST resource, relative to base URI.
        :type uri: string
        :returns: Resource documentation data.
        :rtype: ``EasyDict`` object.
        """
        self.endpoint = uri
        return super(Link, self).options()


class Response(Resource):
    """
    Represents a REST API response object.

    Derived from :class:`Resource`.
    """
    def __init__(self, base_uri, auth, resp):
        """
        Constructor of Response class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        :param resp: response object from API request
        :type resp: JSON
        """
        super(Response, self).__init__(base_uri, auth)
        jresp = resp.json()
        self._meta = EasyDict(jresp['meta'])
        self.status = resp.status_code
        self.headers = EasyDict(resp.headers)
        self.data = [EasyDict(rec) for rec in jresp['result']]

    def _iter(self):
        """Custom iterator to retrieve all data from API response"""
        resp = self
        while True:
            yield (resp.data)
            if not resp._meta or not resp._meta.next:
                raise StopIteration
            else:
                resp = resp.next()

    @property
    def page(self):
        """Current page property"""
        return self._meta.page if self._meta else 0

    @property
    def pages(self):
        """Total pages property"""
        return self._meta.total_pages if self._meta else 0

    @property
    def records_page(self):
        """Records per page property"""
        return self._meta.records if self._meta else 0

    @property
    def records(self):
        """Total records property"""
        return self._meta.total_records if self._meta else 0

    def first(self):
        """Go to first page of API response"""
        if self._meta:
            self.endpoint = self._meta.first
            return super(Response, self).get()
        else:
            return None

    def next(self):
        """Go to next page of API response"""
        if self._meta and self._meta.next:
            self.endpoint = self._meta.next
            return super(Response, self).get()
        return None

    def prev(self):
        """Go to previous page of API response"""
        if self._meta and self._meta.prev:
            self.endpoint = self._meta.prev
            return super(Response, self).get()
        return None

    def last(self):
        """Go to last page of API response"""
        if self._meta:
            self.endpoint = self._meta.last
            return super(Response, self).get()
        return None

    def all(self):
        """Retrieve all data of API response"""
        rec = []
        for page in self._iter():
            rec.extend(page)
        return rec
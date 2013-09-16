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

        full_param_dict = dict(chain(kwargs.items() + self.auth.items()))

        resp = requests.get(uri,params=full_param_dict)

        if resp.status_code == 200:
            jresp = resp.json()
            return EasyDict(dict(headers=resp.headers,
                                 meta=jresp['meta'],
                                 data=jresp['result']))
        else:
            raise SoccermetricsRestException(resp.status_code,resp.url)

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
            jresp = resp.json()
            return EasyDict(dict(headers=resp.headers,
                                 meta=jresp['meta'],
                                 data=jresp['result']))
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
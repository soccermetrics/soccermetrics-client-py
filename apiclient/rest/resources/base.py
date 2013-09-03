from itertools import chain
import requests

from apiclient import SoccermetricsRestException
from apiclient import __api_version__ as API_VERSION

class Resource(object):
    """
    Represents a REST resource.
    """
    def __init__(self, base_uri, auth):
        self.base_uri = base_uri
        self.auth = auth

        self.endpoint = "/%s" % API_VERSION

    def get(self, uid=None, **kwargs):
        """
        Retrieves a representation of REST resource.
        """
        uri = "%s%s/%d" % (self.base_uri, self.endpoint, uid) if uid else \
            "%s%s" % (self.base_uri, self.endpoint)

        full_param_dict = dict(chain(kwargs.items() + self.auth.items()))

        resp = requests.get(uri,params=full_param_dict)

        if resp.status_code == 200:
            result = resp.json()['result']
            return result[0] if len(result) == 1 else result
        else:
            raise SoccermetricsRestException(resp.status_code,resp.url)

    def head(self):
        """
        Retrieves header data of REST resource.
        """
        uri = "%s%s" % (self.base_uri, self.endpoint)

        resp = requests.head(uri,params=self.auth)

        if resp.status_code < 400:
            return resp.headers
        else:
            raise SoccermetricsRestException(resp.status_code,resp.url)

    def options(self):
        """
        Retrieves documentation of REST resource representation.

        Link resources are not included in the documentation.
        """
        uri = "%s%s" % (self.base_uri, self.endpoint)

        resp = requests.options(uri,params=self.auth)

        if resp.status_code == 200:
            return dict(headers=resp.headers,
                    data=resp.json()['result']['data'])
        else:
            raise SoccermetricsRestException(resp.status_code,resp.url)


class Link(Resource):
    """
    Access to linked resources, can also access any API endpoint.
    """
    def __init__(self, base_uri, auth):
        super(Link, self).__init__(base_uri, auth)

    def get(self, uri, **kwargs):
        self.endpoint = uri
        return super(Link, self).get(**kwargs)

    def head(self, uri):
        self.endpoint = uri
        return super(Link, self).head()

    def options(self, uri):
        self.endpoint = uri
        return super(Link, self).options()
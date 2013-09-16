from soccermetrics.rest.resources import Resource

class Personnel(Resource):
    """
    Represents a Personnel REST resource (/personnel endpoint).

    Derived from :class:`Resource`.
    """
    def __init__(self, resource, base_uri, auth):
        """
        Constructor of Personnel class.

        :param resource: Name of resource.
        :type resource: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(Personnel, self).__init__(base_uri,auth)

        self.endpoint += "/personnel/%s" % resource
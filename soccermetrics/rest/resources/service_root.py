from soccermetrics.rest.resources import Resource

class Root(Resource):
    """
    Represents the service root of the REST API (/ endpoint).

    Derived from :class:`base.Resource`.
    """

    def __init__(self, base_uri, auth):
        """
        Constructor of Root class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(Root, self).__init__(base_uri, auth)

        self.endpoint += '/'
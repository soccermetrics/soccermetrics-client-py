from soccermetrics.rest.resources import Resource

class Validation(Resource):
    """
    Establish access to Validation resources (/ endpoint).

    Derived from :class:`base.Resource`.
    """

    def __init__(self, resource, base_uri, auth):
        """
        Constructor of Validation class.

        :param resource: Name of resource.
        :type resource: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(Validation, self).__init__(base_uri,auth)

        self.endpoint += "/%s" % resource
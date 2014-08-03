from soccermetrics.rest.resources import Resource

class MatchEventResource(Resource):
    """
    Represents a Match Event REST resource (/events/``resource`` endpoints).

    Derived from :class:`base.Resource`.
    """
    def __init__(self, play, resource, base_uri, auth):
        """
        Constructor of MatchEventResource class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param resource: Name of resource.
        :type resource: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(MatchEventResource, self).__init__(base_uri,auth)

        self.endpoint += "/%s/events/%s" % (play, resource)


class MatchEvents(object):
    """
    Establish access to Match Event objects (/events endpoint).

    +--------------+-----------------------+
    | Attribute    | Description           |
    +==============+=======================+
    | all          | All micro events      |
    +--------------+-----------------------+
    | touches      | All touch events      |
    +--------------+-----------------------+
    | actions      | All event actions     |
    +--------------+-----------------------+
    """
    def __init__(self, play, base_uri, auth):
        """
        Constructor of MatchEvents class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        self.all = MatchEventResource(play, "all", base_uri, auth)
        self.touches = MatchEventResource(play, "touches", base_uri, auth)
        self.actions = MatchEventResource(play, "actions", base_uri, auth)

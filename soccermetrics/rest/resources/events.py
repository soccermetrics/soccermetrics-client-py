from soccermetrics.rest.resources import Resource

class MatchEventResource(Resource):
    """
    Represents a Match Event REST resource (/events/``resource`` endpoints).

    Derived from :class:`base.Resource`.
    """
    def __init__(self, resource, base_uri, auth):
        """
        Constructor of MatchEventResource class.

        :param resource: Name of resource.
        :type resource: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(MatchEventResource, self).__init__(base_uri,auth)

        self.endpoint += "/events/%s" % resource


class MatchEvents(object):
    """
    Establish access to Match Event objects (/events endpoint).

    +----------------+-----------------------+
    | Attribute      | Description           |
    +================+=======================+
    | goals          | Goal events           |
    +----------------+-----------------------+
    | penalties      | Penalty kick events   |
    +----------------+-----------------------+
    | offenses       | Disciplinary events   |
    +----------------+-----------------------+
    | substitutions  | Substitution events   |
    +----------------+-----------------------+
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of MatchEvents class.

        :param resource: Name of resource.
        :type resource: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        self.goals = MatchEventResource("goals", base_uri, auth)
        self.penalties = MatchEventResource("penalties", base_uri, auth)
        self.offenses = MatchEventResource("offenses", base_uri, auth)
        self.substitutions = MatchEventResource("substitutions", base_uri, auth)
from apiclient.rest.resources import Resource

class MatchEventResource(Resource):
    """
    Represents a Match Event REST resource.
    """
    def __init__(self, resource, base_uri, auth):
        super(MatchEventResource, self).__init__(base_uri,auth)

        self.endpoint += "/events/%s" % resource


class MatchEvents(object):
    """
    Access to Match Event objects.
    """
    def __init__(self, base_uri, auth):

        self.goals = MatchEventResource("goals", base_uri, auth)
        self.penalties = MatchEventResource("penalties", base_uri, auth)
        self.offenses = MatchEventResource("offenses", base_uri, auth)
        self.substitutions = MatchEventResource("substitutions", base_uri, auth)
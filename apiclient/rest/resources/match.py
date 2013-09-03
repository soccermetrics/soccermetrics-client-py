from apiclient.rest.resources import Resource

class MatchResource(Resource):
    """
    Represents a Match REST resource.
    """
    def __init__(self, base_uri, auth):
        super(MatchResource, self).__init__(base_uri,auth)

        self.base_endpoint = self.endpoint + "/matches"
        self.match = None
        self.resource = None

    def EndpointURI(self):
        return '/'.join(str(x) for x in [self.base_endpoint,self.match,self.resource] if x)

    def get(self, match=None, uid=None, **kwargs):
        self.match = match
        self.endpoint = self.EndpointURI()
        return super(MatchResource, self).get(uid, **kwargs)

    def head(self):
        self.match = None
        self.endpoint = self.EndpointURI()
        return super(MatchResource, self).head()

    def options(self):
        self.match = None
        self.endpoint = self.EndpointURI()
        return super(MatchResource, self).options()


class MatchInformation(MatchResource):
    """
    Access to Match Information resources.
    """
    def __init__(self, base_uri, auth):
        super(MatchInformation, self).__init__(base_uri,auth)
        self.resource = "info"


class MatchConditions(MatchResource):
    """
    Access to Match Conditions resources.
    """
    def __init__(self, base_uri, auth):
        super(MatchConditions, self).__init__(base_uri,auth)
        self.resource = "conditions"


class MatchLineups(MatchResource):
    """
    Access to Match Lineups resources.
    """
    def __init__(self, base_uri, auth):
        super(MatchLineups, self).__init__(base_uri,auth)
        self.resource = "lineups"


class Match(object):
    """
    Access to Match objects.
    """
    def __init__(self, base_uri, auth):
        self.information = MatchInformation(base_uri,auth)
        self.lineups = MatchLineups(base_uri,auth)
        self.conditions = MatchConditions(base_uri,auth)
from soccermetrics.rest.resources import Resource

class MatchResource(Resource):
    """
    Represents a Match REST resource (/matches endpoints).

    Derived from :class:`resources.Resource`.
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of MatchResource class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(MatchResource, self).__init__(base_uri,auth)

        self.base_endpoint = self.endpoint + "/matches"
        self.match = None
        self.resource = None

    def EndpointURI(self):
        """
        Construct URI of Match REST resource.

        URI is of format ``/matches/<match>/<resource>/``.

        :returns: URI of REST resource.
        :rtype: string
        """
        return '/'.join(str(x) for x in [self.base_endpoint,self.match,self.resource] if x)

    def get(self, match=None, uid=None, **kwargs):
        """
        Retrieves a representation of Match REST resource.

        :param match: Unique ID associated with football match.
        :type match: integer
        :param uid: Unique ID of API resource representation.
        :type uid: integer
        :param kwargs: Collection of query parameters.
        :type kwargs: dict
        :returns: Resource representation.
        :rtype: Return value of :func:`MatchResource.get`.
        """
        self.match = match
        self.endpoint = self.EndpointURI()
        return super(MatchResource, self).get(uid, **kwargs)

    def head(self):
        """
        Retrieves header data of Match REST resource.

        :returns: Header data.
        :rtype: Return value of :func:`MatchResource.head`.
        """
        self.match = None
        self.endpoint = self.EndpointURI()
        return super(MatchResource, self).head()

    def options(self):
        """
        Retrieves documentation of Match REST resource.

        If the status code is 200 (OK), returns the documentation.  Otherwise,
        returns an error.

        Link resources are not included in the documentation.

        :returns: Resource documentation data.
        :rtype: Return value of :func:`MatchResource.options`.
        """
        self.match = None
        self.endpoint = self.EndpointURI()
        return super(MatchResource, self).options()


class MatchInformation(MatchResource):
    """
    Access to Match Information resources (/matches/info resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, base_uri, auth):
        super(MatchInformation, self).__init__(base_uri,auth)
        self.resource = "info"


class MatchConditions(MatchResource):
    """
    Access to Match Conditions resources (/matches/conditions resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, base_uri, auth):
        super(MatchConditions, self).__init__(base_uri,auth)
        self.resource = "conditions"


class MatchLineups(MatchResource):
    """
    Access to Match Lineups resources (/matches/lineups resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, base_uri, auth):
        super(MatchLineups, self).__init__(base_uri,auth)
        self.resource = "lineups"


class Match(object):
    """
    Access to Match objects.

    +----------------+-----------------------+
    | Attribute      | Description           |
    +================+=======================+
    | information    | Match information     |
    +----------------+-----------------------+
    | lineups        | Match lineups         |
    +----------------+-----------------------+
    | conditions     | Match conditions      |
    +----------------+-----------------------+
    """
    def __init__(self, base_uri, auth):
        self.information = MatchInformation(base_uri,auth)
        self.lineups = MatchLineups(base_uri,auth)
        self.conditions = MatchConditions(base_uri,auth)

from soccermetrics.rest.resources import Resource

class AnalyticsResource(Resource):
    """Represents an Analytics REST resource.

    The Match Analytics resources controls access to advanced player
    and team analytics related to events in a football match and
    derived from basic match data.

    Derived from :class:`resources.Resource`.
    """
    def __init__(self, resource, base_uri, auth):
        """
        Constructor of AnalyticsResource class.

        :param resource: Name of Analytics resource.
        :type resource: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(AnalyticsResource, self).__init__(base_uri,auth)

        self.base_endpoint = self.endpoint + '/analytics/match'
        self.match = None
        self.resource = resource

    def EndpointURI(self):
        """
        Construct URI of Analytics REST resource.

        URI is of format ``/analytics/match/<match>/<resource>/``.

        :returns: URI of REST resource.
        :rtype: string
        """
        return '/'.join(str(x) for x in [self.base_endpoint,self.match,self.resource] if x)

    def get(self, match, **kwargs):
        """
        Retrieves a representation of Analytics REST resource.

        :param match: Unique ID associated with football match.
        :type match: integer
        :param kwargs: Collection of query parameters.
        :type kwargs: dict
        :returns: Resource representation.
        :rtype: Return value of :func:`Resource.get`.
        """
        self.match = match
        self.endpoint = self.EndpointURI()
        return super(AnalyticsResource, self).get(**kwargs)

    def head(self):
        """
        Retrieves header data of Analytics REST resource.

        :returns: Header data.
        :rtype: Return value of :func:`Resource.head`.
        """
        self.match = None
        self.endpoint = self.EndpointURI()
        return super(AnalyticsResource, self).head()

    def options(self):
        """
        Retrieves documentation of Analytics REST resource.

        If the status code is 200 (OK), returns the documentation.  Otherwise,
        returns an error.

        Link resources are not included in the documentation.

        :returns: Resource documentation data.
        :rtype: Return value of :func:`Resource.options`.
        """
        self.match = None
        self.endpoint = self.EndpointURI()
        return super(AnalyticsResource, self).options()

class MatchAnalytics(object):
    """Represents a Match Analytics REST resource (/analytics/match endpoints).

        +----------------+--------------------------+
        | Attribute      | Description              |
        +================+==========================+
        | state          | Match state              |
        +----------------+--------------------------+
        | segment        | Match segments           |
        +----------------+--------------------------+
        | tsr            | Match Total Shots Ratio  |
        +----------------+--------------------------+
    """
    def __init__(self, base_uri, auth):
        self.state = AnalyticsResource("state", base_uri, auth)
        self.segment = AnalyticsResource("segment", base_uri, auth)
        self.tsr = AnalyticsResource("tsr", base_uri, auth)
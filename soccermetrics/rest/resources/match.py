from soccermetrics.rest.resources import Resource
from soccermetrics.rest.resources.events import MatchEvents
from soccermetrics.rest.resources.statistics import MatchStatistics

class MatchResource(Resource):
    """
    Represents a Match REST resource (<play>/matches/<resource> endpoints).

    The Match Resources are a collection of macro-events, micro-events, and
    summary statistics resources in the Soccermetrics Connect API.

    Derived from :class:`resources.Resource`.
    """
    def __init__(self, play, base_uri, auth):
        """
        Constructor of MatchResource class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(MatchResource, self).__init__(base_uri,auth)

        self.base_endpoint = "%s/%s/matches" % (self.endpoint, play)
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

        If the status code is 200 (OK), returns the representation.  Otherwise,
        returns an error.

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
    Access to Match Information resources (/<play>/matches/info resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, play, base_uri, auth):
        super(MatchInformation, self).__init__(play, base_uri, auth)
        self.resource = "info"


class MatchConditions(MatchResource):
    """
    Access to Match Conditions resources (/<play>/matches/conditions resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, play, base_uri, auth):
        super(MatchConditions, self).__init__(play, base_uri, auth)
        self.resource = "conditions"


class MatchLineups(MatchResource):
    """
    Access to Match Lineups resources (/<play>/matches/lineups resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, play, base_uri, auth):
        super(MatchLineups, self).__init__(play, base_uri, auth)
        self.resource = "lineups"


class MatchGoals(MatchResource):
    """
    Access to Match Goals resources (/<play>/matches/goals resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, play, base_uri, auth):
        super(MatchGoals, self).__init__(play, base_uri, auth)
        self.resource = "goals"

class MatchPenalties(MatchResource):
    """
    Access to Match Penalties resources (/<play>/matches/penalties resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, play, base_uri, auth):
        super(MatchPenalties, self).__init__(play, base_uri, auth)
        self.resource = "penalties"


class MatchOffenses(MatchResource):
    """
    Access to Match Offenses resources (/<play>/matches/offenses resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, play, base_uri, auth):
        super(MatchOffenses, self).__init__(play, base_uri, auth)
        self.resource = "offenses"


class MatchSubstitutions(MatchResource):
    """
    Access to Match Substitutions resources (/<play>/matches/substitutions resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, play, base_uri, auth):
        super(MatchSubstitutions, self).__init__(play, base_uri, auth)
        self.resource = "substitutions"


class MatchShootouts(MatchResource):
    """
    Access to Match Shootouts resources (/<play>/matches/shootouts resource).

    Derived from :class:`MatchResource`.
    """
    def __init__(self, play, base_uri, auth):
        super(MatchShootouts, self).__init__(play, base_uri, auth)
        self.resource = "shootouts"


class MatchPlay(object):
    """
    Access to Match objects for a specific type of match (club,
    national team).

    +----------------+---------------------------+
    | Attribute      | Description               |
    +================+===========================+
    | information    | Match information         |
    +----------------+---------------------------+
    | lineups        | Match lineups             |
    +----------------+---------------------------+
    | conditions     | Match conditions          |
    +----------------+---------------------------+
    | goals          | Goal events               |
    +----------------+---------------------------+
    | penalties      | Penalty kick events       |
    +----------------+---------------------------+
    | offenses       | Disciplinary events       |
    +----------------+---------------------------+
    | substitutions  | Substitution events       |
    +----------------+---------------------------+
    | shootouts      | Penalty shootout events   |
    +----------------+---------------------------+
    | stats          | Match statistics          |
    +----------------+---------------------------+
    | events         | Match micro-events        |
    +----------------+---------------------------+
    """
    def __init__(self, play, base_uri, auth):
        self.information = MatchInformation(play, base_uri, auth)
        self.lineups = MatchLineups(play, base_uri, auth)
        self.conditions = MatchConditions(play, base_uri, auth)
        self.goals = MatchGoals(play, base_uri, auth)
        self.penalties = MatchPenalties(play, base_uri, auth)
        self.offenses = MatchOffenses(play, base_uri, auth)
        self.substitutions = MatchSubstitutions(play, base_uri, auth)
        self.shootouts = MatchShootouts(play, base_uri, auth)

        self.stats = MatchStatistics(play, base_uri, auth)
        self.events = MatchEvents(play, base_uri, auth)
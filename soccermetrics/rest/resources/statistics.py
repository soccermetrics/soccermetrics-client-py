from soccermetrics.rest.resources import Resource

class MatchStatisticsResource(Resource):
    """
    Represents a Match Statistics REST resource (/stats/<statistic>/<resource> endpoints).

    Derived from :class:`base.Resource`.
    """
    def __init__(self, statistic, resource, base_uri, auth):
        """
        Constructor of MatchStatisticsResource class.

        :param statistic: Statistic type.
        :type statistic: string
        :param resource: Name of resource.
        :type resource: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(MatchStatisticsResource, self).__init__(base_uri,auth)

        self.endpoint += "/stats/%s/%s" % (statistic, resource)


class CrossingStatistics(object):
    """
    Establish access to Cross statistical resources (/stats/crosses endpoint).

    +----------------+-----------------------+
    | Attribute      | Description           |
    +================+=======================+
    | corners        | Crosses from corners  |
    +----------------+-----------------------+
    | totals         | Total crossing stats  |
    +----------------+-----------------------+

    """
    def __init__(self, base_uri, auth):
        """
        Constructor of CrossingStatistics class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(CrossingStatistics, self).__init__()

        statistic = "crosses"

        self.corners = MatchStatisticsResource(statistic, "corners", base_uri, auth)
        self.totals = MatchStatisticsResource(statistic, "totals", base_uri, auth)


class DefensiveStatistics(object):
    """
    Establish access to Defensive statistical resources (/stats/defense endpoint).

    +----------------+----------------------------+
    | Attribute      | Description                |
    +================+============================+
    | actions        | Defensive actions          |
    +----------------+----------------------------+
    | blocks         | Shot block stats           |
    +----------------+----------------------------+
    | clearances     | Ball clearance stats       |
    +----------------+----------------------------+
    | goalline       | Goal-line clearance stats  |
    +----------------+----------------------------+
    | tackles        | Tackling stats             |
    +----------------+----------------------------+
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of DefensiveStatistics class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(DefensiveStatistics, self).__init__()

        statistic = "defense"

        self.actions = MatchStatisticsResource(statistic, "actions", base_uri, auth)
        self.blocks = MatchStatisticsResource(statistic, "blocks", base_uri, auth)
        self.clearances = MatchStatisticsResource(statistic, "clearances", base_uri, auth)
        self.goalline = MatchStatisticsResource(statistic, "goalline", base_uri, auth)
        self.tackles = MatchStatisticsResource(statistic, "tackles", base_uri, auth)


class FoulingStatistics(object):
    """
    Access to Foul statistical resources (/stats/fouls endpoint).

    +--------------+-----------------------+
    | Attribute    | Description           |
    +==============+=======================+
    | cards        | Card stats            |
    +--------------+-----------------------+
    | wins         | Foul suffered stats   |
    +--------------+-----------------------+
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of FoulingStatistics class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(FoulingStatistics, self).__init__()

        statistic = "fouls"

        self.cards = MatchStatisticsResource(statistic, "cards", base_uri, auth)
        self.wins = MatchStatisticsResource(statistic, "wins", base_uri, auth)


class GoalStatistics(object):
    """
    Access to Goal statistical resources (/stats/goals endpoint).

    +----------------+----------------------------+
    | Attribute      | Description                |
    +================+============================+
    | assists        | Goal assist stats          |
    +----------------+----------------------------+
    | bodyparts      | Goalscoring bodypart stats |
    +----------------+----------------------------+
    | locations      | Goalscoring location stats |
    +----------------+----------------------------+
    | penalties      | Match penalty stats        |
    +----------------+----------------------------+
    | totals         | Total goalscoring stats    |
    +----------------+----------------------------+
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of GoalStatistics class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(GoalStatistics, self).__init__()

        statistic = "goals"

        self.assists = MatchStatisticsResource(statistic, "assists", base_uri, auth)
        self.bodyparts = MatchStatisticsResource(statistic, "bodyparts", base_uri, auth)
        self.locations = MatchStatisticsResource(statistic, "locations", base_uri, auth)
        self.penalties = MatchStatisticsResource(statistic, "penalties", base_uri, auth)
        self.totals = MatchStatisticsResource(statistic, "totals", base_uri, auth)


class GoalkeepingStatistics(object):
    """
    Access to Goalkeeper statistical resources (/stats/goalkeeper endpoint).

    +----------------+----------------------------+
    | Attribute      | Description                |
    +================+============================+
    | actions        | Goalkeeping action stats   |
    +----------------+----------------------------+
    | goals          | Goals allowed stats        |
    +----------------+----------------------------+
    | shots          | Shots allowed stats        |
    +----------------+----------------------------+
    | saves          | Goalkeeper saves stats     |
    +----------------+----------------------------+
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of GoalkeepingStatistics class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(GoalkeepingStatistics, self).__init__()

        statistic = "goalkeeper"

        self.actions = MatchStatisticsResource(statistic, "actions", base_uri, auth)
        self.goals = MatchStatisticsResource(statistic, "goals", base_uri, auth)
        self.shots = MatchStatisticsResource(statistic, "shots", base_uri, auth)
        self.saves = MatchStatisticsResource(statistic, "saves", base_uri, auth)


class PassingStatistics(object):
    """
    Access to Passing statistical resources (/stats/passes endpoint).

    +----------------+----------------------------+
    | Attribute      | Description                |
    +================+============================+
    | directions     | Pass direction stats       |
    +----------------+----------------------------+
    | lengths        | Pass length stats          |
    +----------------+----------------------------+
    | locations      | Pass location stats        |
    +----------------+----------------------------+
    | totals         | Total passing stats        |
    +----------------+----------------------------+
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of PassingStatistics class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(PassingStatistics, self).__init__()

        statistic = "passes"

        self.directions = MatchStatisticsResource(statistic, "directions", base_uri, auth)
        self.lengths = MatchStatisticsResource(statistic, "lengths", base_uri, auth)
        self.locations = MatchStatisticsResource(statistic, "locations", base_uri, auth)
        self.totals = MatchStatisticsResource(statistic, "totals", base_uri, auth)


class SetPieceStatistics(object):
    """
    Access to Set-Piece statistical resources (/stats/setpieces endpoint).

    +----------------+----------------------------+
    | Attribute      | Description                |
    +================+============================+
    | corners        | Corner kick stats          |
    +----------------+----------------------------+
    | freekicks      | Direct freekick stats      |
    +----------------+----------------------------+
    | throwins       | Throw-in stats             |
    +----------------+----------------------------+
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of SetPieceStatistics class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(SetPieceStatistics, self).__init__()

        statistic = "setpieces"

        self.corners = MatchStatisticsResource(statistic, "corners", base_uri, auth)
        self.freekicks = MatchStatisticsResource(statistic, "freekicks", base_uri, auth)
        self.throwins = MatchStatisticsResource(statistic, "throwins", base_uri, auth)


class ShotStatistics(object):
    """
    Access to Shot statistical resources (/stats/shots endpoint).

    +----------------+----------------------------+
    | Attribute      | Description                |
    +================+============================+
    | bodyparts      | Shot bodypart stats        |
    +----------------+----------------------------+
    | locations      | Shot location stats        |
    +----------------+----------------------------+
    | plays          | Shot play stats            |
    +----------------+----------------------------+
    | totals         | Total shot stats           |
    +----------------+----------------------------+
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of ShotStatistics class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(ShotStatistics, self).__init__()

        statistic = "shots"

        self.bodyparts = MatchStatisticsResource(statistic, "bodyparts", base_uri, auth)
        self.locations = MatchStatisticsResource(statistic, "locations", base_uri, auth)
        self.plays = MatchStatisticsResource(statistic, "plays", base_uri, auth)
        self.totals = MatchStatisticsResource(statistic, "totals", base_uri, auth)


class TouchStatistics(object):
    """
    Access to Touch statistical resources (/stats/touches endpoint).

    +----------------+----------------------------+
    | Attribute      | Description                |
    +================+============================+
    | duels          | 50/50 dueling stats        |
    +----------------+----------------------------+
    | locations      | Ball touch location stats  |
    +----------------+----------------------------+
    | totals         | Total ball touch stats     |
    +----------------+----------------------------+
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of TouchStatistics class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(TouchStatistics, self).__init__()

        statistic = "touches"

        self.duels = MatchStatisticsResource(statistic, "duels", base_uri, auth)
        self.locations = MatchStatisticsResource(statistic, "locations", base_uri, auth)
        self.totals = MatchStatisticsResource(statistic, "totals", base_uri, auth)


class MatchStatistics(object):
    """
    Establish access to Match Statistics objects (/stats endpoints).

    +----------------+----------------------------+
    | Attribute      | Description                |
    +================+============================+
    | crosses        | Crossing statistics        |
    +----------------+----------------------------+
    | defense        | Defensive statistics       |
    +----------------+----------------------------+
    | fouls          | Foul statistics            |
    +----------------+----------------------------+
    | goals          | Goal statistics            |
    +----------------+----------------------------+
    | goalkeeper     | Goalkeeping statistics     |
    +----------------+----------------------------+
    | passes         | Passing statistics         |
    +----------------+----------------------------+
    | setpieces      | Set-piece statistics       |
    +----------------+----------------------------+
    | shots          | Shot statistics            |
    +----------------+----------------------------+
    | touches        | Ball touch statistics      |
    +----------------+----------------------------+
    """
    def __init__(self, base_uri, auth):
        """
        Constructor of MatchStatistics class.

        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """

        self.crosses = CrossingStatistics(base_uri, auth)
        self.defense = DefensiveStatistics(base_uri, auth)
        self.fouls = FoulingStatistics(base_uri, auth)
        self.goals = GoalStatistics(base_uri, auth)
        self.goalkeeper = GoalkeepingStatistics(base_uri, auth)
        self.passes = PassingStatistics(base_uri, auth)
        self.setpieces = SetPieceStatistics(base_uri, auth)
        self.shots = ShotStatistics(base_uri, auth)
        self.touches = TouchStatistics(base_uri, auth)
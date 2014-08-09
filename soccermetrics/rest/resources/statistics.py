from soccermetrics.rest.resources import Resource

class MatchStatisticsResource(Resource):
    """
    Represents a Match Statistics REST resource.

    The Match Statistics resources controls access to summary in-match
    statistical data of players who are in the match lineups of a
    football match.

    Derived from :class:`base.Resource`.
    """
    def __init__(self, play, statistic, resource, base_uri, auth):
        """
        Constructor of MatchStatisticsResource class.

        :param play: Type of teams playing in matches.
        :type play: string
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

        self.endpoint += "/%s/stats/%s/%s" % (play, statistic, resource)


class CrossingStatistics(object):
    """
    Establish access to Cross statistical resources (/<play>/stats/crosses endpoint).

    +----------------+-----------------------+
    | Attribute      | Description           |
    +================+=======================+
    | corners        | Crosses from corners  |
    +----------------+-----------------------+
    | totals         | Total crossing stats  |
    +----------------+-----------------------+

    """
    def __init__(self, play, base_uri, auth):
        """
        Constructor of CrossingStatistics class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(CrossingStatistics, self).__init__()

        statistic = "crosses"

        self.corners = MatchStatisticsResource(play, statistic, "corners", base_uri, auth)
        self.totals = MatchStatisticsResource(play, statistic, "totals", base_uri, auth)


class DefensiveStatistics(object):
    """
    Establish access to Defensive statistical resources (/<play>/stats/defense endpoint).

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
    def __init__(self, play, base_uri, auth):
        """
        Constructor of DefensiveStatistics class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(DefensiveStatistics, self).__init__()

        statistic = "defense"

        self.actions = MatchStatisticsResource(play, statistic, "actions", base_uri, auth)
        self.blocks = MatchStatisticsResource(play, statistic, "blocks", base_uri, auth)
        self.clearances = MatchStatisticsResource(play, statistic, "clearances", base_uri, auth)
        self.goalline = MatchStatisticsResource(play, statistic, "goalline", base_uri, auth)
        self.tackles = MatchStatisticsResource(play, statistic, "tackles", base_uri, auth)


class FoulingStatistics(object):
    """
    Access to Foul statistical resources (/<play>/stats/fouls endpoint).

    +--------------+-----------------------+
    | Attribute    | Description           |
    +==============+=======================+
    | cards        | Card stats            |
    +--------------+-----------------------+
    | wins         | Foul suffered stats   |
    +--------------+-----------------------+
    """
    def __init__(self, play, base_uri, auth):
        """
        Constructor of FoulingStatistics class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(FoulingStatistics, self).__init__()

        statistic = "fouls"

        self.cards = MatchStatisticsResource(play, statistic, "cards", base_uri, auth)
        self.wins = MatchStatisticsResource(play, statistic, "wins", base_uri, auth)


class GoalStatistics(object):
    """
    Access to Goal statistical resources (/<play>/stats/goals endpoint).

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
    def __init__(self, play, base_uri, auth):
        """
        Constructor of GoalStatistics class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(GoalStatistics, self).__init__()

        statistic = "goals"

        self.assists = MatchStatisticsResource(play, statistic, "assists", base_uri, auth)
        self.bodyparts = MatchStatisticsResource(play, statistic, "bodyparts", base_uri, auth)
        self.locations = MatchStatisticsResource(play, statistic, "locations", base_uri, auth)
        self.penalties = MatchStatisticsResource(play, statistic, "penalties", base_uri, auth)
        self.totals = MatchStatisticsResource(play, statistic, "totals", base_uri, auth)


class GoalkeepingStatistics(object):
    """
    Access to Goalkeeper statistical resources (/<play>/stats/goalkeeper endpoint).

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
    def __init__(self, play, base_uri, auth):
        """
        Constructor of GoalkeepingStatistics class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(GoalkeepingStatistics, self).__init__()

        statistic = "goalkeeper"

        self.actions = MatchStatisticsResource(play, statistic, "actions", base_uri, auth)
        self.goals = MatchStatisticsResource(play, statistic, "goals", base_uri, auth)
        self.shots = MatchStatisticsResource(play, statistic, "shots", base_uri, auth)
        self.saves = MatchStatisticsResource(play, statistic, "saves", base_uri, auth)


class PassingStatistics(object):
    """
    Access to Passing statistical resources (/<play>/stats/passes endpoint).

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
    def __init__(self, play, base_uri, auth):
        """
        Constructor of PassingStatistics class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(PassingStatistics, self).__init__()

        statistic = "passes"

        self.directions = MatchStatisticsResource(play, statistic, "directions", base_uri, auth)
        self.lengths = MatchStatisticsResource(play, statistic, "lengths", base_uri, auth)
        self.locations = MatchStatisticsResource(play, statistic, "locations", base_uri, auth)
        self.totals = MatchStatisticsResource(play, statistic, "totals", base_uri, auth)


class SetPieceStatistics(object):
    """
    Access to Set-Piece statistical resources (/<play>/stats/setpieces endpoint).

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
    def __init__(self, play, base_uri, auth):
        """
        Constructor of SetPieceStatistics class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(SetPieceStatistics, self).__init__()

        statistic = "setpieces"

        self.corners = MatchStatisticsResource(play, statistic, "corners", base_uri, auth)
        self.freekicks = MatchStatisticsResource(play, statistic, "freekicks", base_uri, auth)
        self.throwins = MatchStatisticsResource(play, statistic, "throwins", base_uri, auth)


class ShotStatistics(object):
    """
    Access to Shot statistical resources (/<play>/stats/shots endpoint).

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
    def __init__(self, play, base_uri, auth):
        """
        Constructor of ShotStatistics class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(ShotStatistics, self).__init__()

        statistic = "shots"

        self.bodyparts = MatchStatisticsResource(play, statistic, "bodyparts", base_uri, auth)
        self.locations = MatchStatisticsResource(play, statistic, "locations", base_uri, auth)
        self.plays = MatchStatisticsResource(play, statistic, "plays", base_uri, auth)
        self.totals = MatchStatisticsResource(play, statistic, "totals", base_uri, auth)


class TouchStatistics(object):
    """
    Access to Touch statistical resources (/<play>/stats/touches endpoint).

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
    def __init__(self, play, base_uri, auth):
        """
        Constructor of TouchStatistics class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(TouchStatistics, self).__init__()

        statistic = "touches"

        self.duels = MatchStatisticsResource(play, statistic, "duels", base_uri, auth)
        self.locations = MatchStatisticsResource(play, statistic, "locations", base_uri, auth)
        self.totals = MatchStatisticsResource(play, statistic, "totals", base_uri, auth)


class MatchStatistics(object):
    """
    Establish access to Match Statistics objects (/<play>/stats endpoints).

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
    def __init__(self, play, base_uri, auth):
        """
        Constructor of MatchStatistics class.

        :param play: Type of teams playing in matches.
        :type play: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """

        self.crosses = CrossingStatistics(play, base_uri, auth)
        self.defense = DefensiveStatistics(play, base_uri, auth)
        self.fouls = FoulingStatistics(play, base_uri, auth)
        self.goals = GoalStatistics(play, base_uri, auth)
        self.goalkeeper = GoalkeepingStatistics(play, base_uri, auth)
        self.passes = PassingStatistics(play, base_uri, auth)
        self.setpieces = SetPieceStatistics(play, base_uri, auth)
        self.shots = ShotStatistics(play, base_uri, auth)
        self.touches = TouchStatistics(play, base_uri, auth)
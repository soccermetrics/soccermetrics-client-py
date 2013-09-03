from apiclient.rest.resources import Resource

class MatchStatisticsResource(Resource):
    """
    Represents a Match Statistics REST resource.
    """
    def __init__(self, statistic, resource, base_uri, auth):
        super(MatchStatisticsResource, self).__init__(base_uri,auth)

        self.endpoint += "/stats/%s/%s" % (statistic, resource)


class CrossingStatistics(object):
    """
    Access to Cross statistical resources.
    """
    def __init__(self, base_uri, auth):
        super(CrossingStatistics, self).__init__()

        statistic = "crosses"

        self.corners = MatchStatisticsResource(statistic, "corners", base_uri, auth)
        self.totals = MatchStatisticsResource(statistic, "totals", base_uri, auth)


class DefensiveStatistics(object):
    """
    Access to Defensive statistical resources.
    """
    def __init__(self, base_uri, auth):
        super(DefensiveStatistics, self).__init__()

        statistic = "defense"

        self.actions = MatchStatisticsResource(statistic, "actions", base_uri, auth)
        self.blocks = MatchStatisticsResource(statistic, "blocks", base_uri, auth)
        self.clearances = MatchStatisticsResource(statistic, "clearances", base_uri, auth)
        self.goalline = MatchStatisticsResource(statistic, "goalline", base_uri, auth)
        self.tackles = MatchStatisticsResource(statistic, "tackles", base_uri, auth)


class FoulingStatistics(object):
    """
    Access to Foul statistical resources.
    """
    def __init__(self, base_uri, auth):
        super(FoulingStatistics, self).__init__()

        statistic = "fouls"

        self.cards = MatchStatisticsResource(statistic, "cards", base_uri, auth)
        self.wins = MatchStatisticsResource(statistic, "wins", base_uri, auth)


class GoalStatistics(object):
    """
    Access to Goal statistical resources.
    """
    def __init__(self, base_uri, auth):
        super(GoalStatistics, self).__init__()

        statistic = "goals"

        self.assists = MatchStatisticsResource(statistic, "assists", base_uri, auth)
        self.bodyparts = MatchStatisticsResource(statistic, "bodyparts", base_uri, auth)
        self.locations = MatchStatisticsResource(statistic, "locations", base_uri, auth)
        self.penalties = MatchStatisticsResource(statistic, "penalties", base_uri, auth)
        self.totals = MatchStatisticsResource(statistic, "totals", base_uri, auth)


class GoalkeepingStatistics(object):
    """
    Access to Goalkeeper statistical resources.
    """
    def __init__(self, base_uri, auth):
        super(GoalkeepingStatistics, self).__init__()

        statistic = "goalkeeper"

        self.actions = MatchStatisticsResource(statistic, "actions", base_uri, auth)
        self.goals = MatchStatisticsResource(statistic, "goals", base_uri, auth)
        self.shots = MatchStatisticsResource(statistic, "shots", base_uri, auth)
        self.saves = MatchStatisticsResource(statistic, "saves", base_uri, auth)


class PassingStatistics(object):
    """
    Access to Passing statistical resources.
    """
    def __init__(self, base_uri, auth):
        super(PassingStatistics, self).__init__()

        statistic = "passes"

        self.directions = MatchStatisticsResource(statistic, "directions", base_uri, auth)
        self.lengths = MatchStatisticsResource(statistic, "lengths", base_uri, auth)
        self.locations = MatchStatisticsResource(statistic, "locations", base_uri, auth)
        self.totals = MatchStatisticsResource(statistic, "totals", base_uri, auth)


class SetPieceStatistics(object):
    """
    Access to Set-Piece statistical resources.
    """
    def __init__(self, base_uri, auth):
        super(SetPieceStatistics, self).__init__()

        statistic = "setpieces"

        self.corners = MatchStatisticsResource(statistic, "corners", base_uri, auth)
        self.freekicks = MatchStatisticsResource(statistic, "freekicks", base_uri, auth)
        self.throwins = MatchStatisticsResource(statistic, "throwins", base_uri, auth)


class ShotStatistics(object):
    """
    Access to Shot statistical resources.
    """
    def __init__(self, base_uri, auth):
        super(ShotStatistics, self).__init__()

        statistic = "shots"

        self.bodyparts = MatchStatisticsResource(statistic, "bodyparts", base_uri, auth)
        self.locations = MatchStatisticsResource(statistic, "locations", base_uri, auth)
        self.plays = MatchStatisticsResource(statistic, "plays", base_uri, auth)
        self.totals = MatchStatisticsResource(statistic, "totals", base_uri, auth)


class TouchStatistics(object):
    """
    Access to Touch statistical resources.
    """
    def __init__(self, base_uri, auth):
        super(TouchStatistics, self).__init__()

        statistic = "touches"

        self.duels = MatchStatisticsResource(statistic, "duels", base_uri, auth)
        self.locations = MatchStatisticsResource(statistic, "locations", base_uri, auth)
        self.totals = MatchStatisticsResource(statistic, "totals", base_uri, auth)


class MatchStatistics(object):
    """
    Access to Match Statistics objects.
    """
    def __init__(self, base_uri, auth):

        self.crosses = CrossingStatistics(base_uri, auth)
        self.defense = DefensiveStatistics(base_uri, auth)
        self.fouls = FoulingStatistics(base_uri, auth)
        self.goals = GoalStatistics(base_uri, auth)
        self.goalkeeper = GoalkeepingStatistics(base_uri, auth)
        self.passes = PassingStatistics(base_uri, auth)
        self.setpieces = SetPieceStatistics(base_uri, auth)
        self.shots = ShotStatistics(base_uri, auth)
        self.touches = TouchStatistics(base_uri, auth)
#!/usr/bin/env/python
# -*- encoding: utf-8 -*-
#
# Compute fantasy points by player and plot weekly fantasy performance.
# Also plot distribution of fantasy points.

# All players
# -----------
# [x] Played up to 60 minutes  1
# [x] Played 60 minutes or more 2
# [x] Goal assist 3
# [x] Yellow card -1
# [x] Own goal -2
# [x] Penalty miss -2
# [x] Red card -3

# Goalkeeper-specific
# -------------------
# [x] Every three shots made by goalkeeper 1
# [x] Clean sheet by goalkeeper/defender 4
# [x] Penalty save 5
# [x] Goal scored by goalkeeper/defender 6
# [x] Every two goals conceded by goalkeeper/defender -1

# Defender-specific
# -----------------
# [x] Clean sheet by goalkeeper/defender 4
# [x] Goal scored by goalkeeper/defender 6
# [x] Every two goals conceded by goalkeeper/defender -1

# Midfielder-specific
# -------------------
# [x] Clean sheet by midfielder 1
# [x] Goal scored by midfielder 5

# Forward-specific
# ----------------
# [x] Goal scored by forward 4

import re

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from soccermetrics.rest import SoccermetricsRestClient

forwardList = ['Left Forward', 'Central Forward', 'Right Forward', 'Striker']
midfieldList = ['Left Winger', 'Right Winger', 'Central Midfielder', 'Midfielder']
defensiveList = ['Wing-back','Left Wing-back','Right Wing-back', 'Full-back',
                 'Left Full-back', 'Right Full-back', 'Libero', 'Defender',
                 'Central Defender', 'Goalkeeper']

class matchTime:
    """Match time conversion class.

    Takes into account lengths of match periods.

    :Example:

    >>> mt = matchTime()
    >>> mt = matchTime([47,49])

    """

    PERIODS = [(1, 46), (46, 91)]

    def __init__(self, matchLength=[45, 45]):
        self.matchLength = matchLength

    def total(self):
        return sum(self.matchLength)

    def absoluteTime(self,time):
        """Expresses match time on an absolute time scale.

        :param time: Match time.
        :type time: int or list of ints (time,stoppage)
        :rtype: int

        :Example:
        >>> mt = matchTime()
        >>> mt.absoluteTime(70)
        70

        """
        if type(time) is int:
            time = (time,0)

        # check value of time[0]
        # if not end of period set stoppage time to zero
        if (time[0] and (time[0] % 45)):
            newtime = (time[0],0)
            time = newtime

        # find period in which match time belongs
        for period,k in zip(matchTime.PERIODS,range(len(matchTime.PERIODS))):
            minSet = set(range(period[0],period[1]))
            if minSet.intersection((time[0],)):
                v = k

        return sum(self.matchLength[0:v]) + sum(time)-matchTime.PERIODS[v][0] + 1

def calcSampVariance(vector):
    """Calculate (sample) variance of vector"""
    if len(vector) <= 1:
        return 0
    else:
        mean = calcMean(vector)
        sos = [(x-mean)*(x-mean) for x in vector]
        return sum(sos)/(len(vector)-1)

def calcMean(vector):
    """Calculate mean of vector"""
    if len(vector) == 0:
        return 0.0
    else:
        return sum(vector)/float(len(vector))

def calcPosMultiplier(position_name):
    """Calculate point multiplier given position"""
    multiplier = 1

    if position_name in forwardList:
        multiplier = 4
    elif position_name in midfieldList:
        multiplier = 5
    elif position_name in defensiveList:
        multiplier = 6

    return multiplier

def calcMinutesPlayed(client, lineup, match):
    """Calculate total minutes played by a player in a match.

    This routine accounts for the following outcomes:

    (1) Started and played full match.
    (2) Started match and was sent off.
    (3) Started match and was substituted out.
    (4) Entered match and played remainder of match.
    (5) Entered match and was sent off.
    (6) Entered match and was substituted out.
    """
    # get total playing time of match
    match_length = matchTime([match.firsthalf_length, match.secondhalf_length])
    # did player start match?
    if lineup.is_starting:
        # was player sent off?
        ejected = client.link.get(match.link.events.offenses,
            player_name=lineup.player_name, card_type="Red").all() + \
            client.link.get(match.link.events.offenses,
            player_name=lineup.player_name, card_type="Yellow/Red").all()
        if ejected:
            eject_time = (ejected[0].time_mins, ejected[0].stoppage_mins)
            player_time = match_length.absoluteTime(eject_time)
        else:
            # was player substituted out?
            subs = client.link.get(match.link.events.substitutions,
                out_player_name=lineup.player_name).all()
            if subs:
                subs_time = (subs[0].time_mins, subs[0].stoppage_mins)
                player_time = match_length.absoluteTime(subs_time)
            else:
                player_time = match_length.total()
    # did player enter as substitute?
    else:
        subs = client.link.get(match.link.events.substitutions,
            in_player_name=lineup.player_name).all()
        if subs:
            subs_time = (subs[0].time_mins, subs[0].stoppage_mins)
            # was player sent off?
            ejected = client.link.get(match.link.events.offenses,
                player_name=lineup.player_name, card_type="Red").all() + \
                client.link.get(match.link.events.offenses,
                player_name=lineup.player_name, card_type="Yellow/Red").all()
            if ejected:
                eject_time = (ejected[0].time_mins, ejected[0].stoppage_mins)
                player_time = match_length.absoluteTime(eject_time) - \
                    match_length.absoluteTime(subs_time)
            else:
                # was sub substituted?
                subsubs = client.link.get(match.link.events.substitutions,
                    out_player_name=lineup.player_name).all()
                if subsubs:
                    subsubs_time = (subsubs[0].time_mins, subsubs[0].stoppage_mins)
                    player_time = match_length.absoluteTime(subsubs_time) - \
                        match_length.absoluteTime(subs_time)
                else:
                    player_time = match_length.total() - match_length.absoluteTime(subs_time)
        else:
            player_time = 0
    return player_time

def calcYellowCardPoints(client, resp):
    if resp.data:
        lineup = resp.data[0]
        yellows = client.link.get(lineup.link.stats.fouls.cards).data[0].yellows
        return -yellows
    else:
        return 0

def calcRedCardPoints(client, resp):
    if resp.data:
        lineup = resp.data[0]
        reds = client.link.get(lineup.link.stats.fouls.cards).data[0].reds
        return -3 * reds
    else:
        return 0

def calcGoalPoints(client, resp):
    if resp.data:
        lineup = resp.data[0]
        match = client.link.get(lineup.link.match).data[0]
        goals = client.link.get(match.link.events.goals).all()
        if goals:
            goals_not_own = len([x for x in goals
                if x.player == lineup.player
                and x.player_team == x.scoring_team])
            goals_own = len([x for x in goals
                if x.player == lineup.player
                and x.player_team != x.scoring_team])
            return calcPosMultiplier(lineup.position_name)*goals_not_own - 2*goals_own
    return 0

def calcGoalsAllowedPoints(client, resp):
    if resp.data:
        lineup = resp.data[0]
        isDefPlayer = lineup.position_name in defensiveList
        match = client.link.get(lineup.link.match).data[0]
        # get goals from opposing team
        if match.home_team_name == lineup.player_team:
            opp_team_name = match.away_team_name
        else:
            opp_team_name = match.home_team_name
        goals = client.link.get(match.link.events.goals, scoring_team_name=opp_team_name).all()
        # if player started match...
        if lineup.is_starting:
            # was player sent off?
            ejected = client.link.get(match.link.events.offenses,
                player_name=lineup.player_name, card_type="Red").all() + \
                client.link.get(match.link.events.offenses,
                player_name=lineup.player_name, card_type="Yellow/Red").all()
            if ejected:
                allowed_preeject = len([x for x in goals
                    if x.time_mins < ejected[0].time_mins])
                allowed_posteject = len([x for x in goals
                    if x.time_mins >= ejected[0].time_mins])
                goals_allowed = allowed_preeject * isDefPlayer + allowed_posteject
            else:
                # player not ejected -- was player substituted out?
                subs = client.link.get(match.link.events.substitutions,
                    out_player_name=lineup.player_name).all()
                if subs:
                    goals_allowed = len([x for x in goals
                        if x.time_mins < subs[0].time_mins]) * isDefPlayer
                else:
                    # player in full duration of match
                    goals_allowed = len(goals) * isDefPlayer
        # if player did not start...
        else:
            # did player join as substitute?
            subs = client.link.get(match.link.events.substitutions,
                in_player_name=lineup.player_name).all()
            if subs:
                # was player ejected?
                ejected = client.link.get(match.link.events.offenses,
                    player_name=lineup.player_name, card_type="Red").all() + \
                    client.link.get(match.link.events.offenses,
                    player_name=lineup.player_name, card_type="Yellow/Red").all()
                if ejected:
                    allowed_preeject = len([x for x in goals
                        if x.time_mins >= subs[0].time_mins
                        and x.time_mins < ejected[0].time_mins])
                    allowed_posteject = len([x for x in goals
                        if x.time_mins >= ejected[0].time_mins])
                    goals_allowed = allowed_preeject * isDefPlayer + allowed_posteject
                else:
                    # sub not ejected -- was sub substituted out?
                    subsubs = client.link.get(match.link.events.substitutions,
                        out_player_name=lineup.player_name).all()
                    if subsubs:
                        goals_allowed = len([x for x in goals
                            if x.time_mins >= subs[0].time_mins
                            and x.time_mins < subsubs[0].time_mins]) * isDefPlayer
                    else:
                        goals_allowed = len([x for x in goals
                            if x.time_mins >= subs[0].time_mins]) * isDefPlayer
        return int(goals_allowed*0.5)
    return 0

def calcGoalAssistPoints(client, resp):
    if resp.data:
        lineup = resp.data[0]
        assists = client.link.get(lineup.link.stats.goals.assists).data[0].total
        return 3*assists
    else:
        return 0

def calcCleanSheetPoints(client, resp):
    if resp.data:
        lineup = resp.data[0]
        match = client.link.get(lineup.link.match).data[0]
        match_length = matchTime([match.firsthalf_length, match.secondhalf_length])
        if match.home_team_name == lineup.player_team:
            opp_team_name = match.away_team_name
        else:
            opp_team_name = match.home_team_name
        goals = client.link.get(match.link.events.goals, scoring_team_name=opp_team_name).all()
        # did player start match?
        if lineup.is_starting:
            # was player sent off?
            ejected = client.link.get(match.link.events.offenses,
                player_name=lineup.player_name, card_type="Red").all() + \
                client.link.get(match.link.events.offenses,
                player_name=lineup.player_name, card_type="Yellow/Red").all()
            if ejected:
                eject_time = (ejected[0].time_mins, ejected[0].stoppage_mins)
                player_time = match_length.absoluteTime(eject_time)
                goals_allowed = len([x for x in goals
                    if x.time_mins <= eject_time[0]])
            else:
                # was player substituted out?
                subs = client.link.get(match.link.events.substitutions,
                    out_player_name=lineup.player_name).all()
                if subs:
                    subs_time = (subs[0].time_mins, subs[0].stoppage_mins)
                    player_time = match_length.absoluteTime(subs_time)
                    goals_allowed = len([x for x in goals
                        if x.time_mins <= subs_time[0]])
                else:
                    # player in for full match
                    player_time = match_length.total()
                    goals_allowed = len(goals)
        else:
            # did player join as substitute?
            subs = client.link.get(match.link.events.substitutions,
                in_player_name=lineup.player_name).all()
            if subs:
                subs_time = (subs[0].time_mins, subs[0].stoppage_mins)
                # was player sent off?
                ejected = client.link.get(match.link.events.offenses,
                    player_name=lineup.player_name, card_type="Red").all() + \
                    client.link.get(match.link.events.offenses,
                    player_name=lineup.player_name, card_type="Yellow/Red").all()
                if ejected:
                    eject_time = (ejected[0].time_mins, ejected[0].stoppage_mins)
                    player_time = match_length.absoluteTime(eject_time) - \
                        match_length.absoluteTime(subs_time)
                    goals_allowed = len([x for x in goals if x.time_mins <= eject_time[0]]) - \
                        len([x for x in goals if x.time_mins <= subs_time[0]])
                else:
                    # was sub substituted out?
                    subsubs = client.link.get(match.link.events.substitutions,
                        out_player_name=lineup.player_name).all()
                    if subsubs:
                        subsubs_time = (subsubs[0].time_mins, subsubs[0].stoppage_mins)
                        player_time = match_length.absoluteTime(subsubs_time) - \
                            match_length.absoluteTime(subs_time)
                        goals_allowed = len([x for x in goals
                            if x.time_mins >= subs[0].time_mins
                            and x.time_mins < subsubs[0].time_mins])
                    else:
                        player_time = match_length.total() - match_length.absoluteTime(subs_time)
                        goals_allowed = len([x for x in goals if x.time_mins >= subs_time[0]])
            else:
                player_time = 0
                goals_allowed = None
        if goals_allowed is not None:
            if goals_allowed == 0 and player_time >= 60:
                if lineup.position_name in defensiveList:
                    return 4
                elif lineup.position_name in midfieldList:
                    return 1
    return 0

def calcSavePoints(client, resp):
    if resp.data:
        lineup = resp.data[0]
        saves = client.link.get(lineup.link.stats.goalkeeper.saves).data[0]
        return (saves.insidebox + saves.outsidebox)/3
    else:
        return 0

def calcPenaltyPoints(client, resp):
    if resp.data:
        lineup = resp.data[0]
        match = client.link.get(lineup.link.match).data[0]
        # penalty kick misses
        pen_goals = client.link.get(match.link.events.penalties,
            player_name=lineup.player_name).all()
        if pen_goals:
            pen_misses = len([x for x in pen_goals if x.outcome_type != "Goal"])
        else:
            pen_misses = 0
        # penalty kick saves
        pen_saves = client.link.get(match.link.stats.goalkeeper.saves).data[0].penalty
        # return points (combo pen saves and misses)
        return 5*pen_saves - 3*pen_misses
    else:
        return 0

def calcParticipationPoints(client, resp):
    if resp.data:
        lineup = resp.data[0]
        match = client.link.get(lineup.link.match).data[0]
        player_time = calcMinutesPlayed(client, lineup, match)
        return 1 if player_time < 60 else 2
    return 0

def plotFantasyCharts(name, matchdays, yvec):
    """Create chart of fantasy point time history and distribution."""

    # Create a regex pattern for name
    p = re.compile('\s')

    # Create a figure with size 6 x 6 inches.
    # Create a canvas and add the figure to it.
    fig = Figure(figsize=(6,6))
    canvas = FigureCanvas(fig)

    # Create a subplot and define the title and axis labels.
    ax = fig.add_subplot(211)
    ax.set_title(u"%s: 2011-12 Fantasy Performance" % (name,),fontsize=14)
    ax.set_xlabel("Matchday",fontsize=12)
    ax.set_ylabel("Official FPL Points",fontsize=12)

    # Generate the line plot.
    ax.plot(matchdays, yvec, 'b-')

    # Create the second subplot and define the title and axis labels.
    ax = fig.add_subplot(212)
    ax.set_xlabel("Official FPL Points",fontsize=12)
    ax.set_ylabel("Occurrences",fontsize=12)

    # Generate the histogram.
    ax.hist(yvec, bins=range(min(yvec),max(yvec)+2),
        align='left', alpha=0.5, facecolor='blue')

    # Annotate the second subplot with total/average points.
    ax.text(0.6, 0.9, "Total Points: %d" % (sum(yvec),), transform=ax.transAxes)
    ax.text(0.6, 0.8, "Expected Points: %2.1f" % (calcMean(yvec),),
        transform=ax.transAxes)
    ax.text(0.6, 0.7, "Variance: %2.1f" % (calcSampVariance(yvec),),
        transform=ax.transAxes)

    # Save figure to a PNG file.
    canvas.print_figure('%s_2011-12.png' % (p.sub('_',name),), dpi=500)

if __name__ == "__main__":

    client = SoccermetricsRestClient()

    pname = u'Robin van Persie'

    matchdays = range(1,39)

    Total = []
    for day in matchdays:
        resp = client.match.lineups.get(matchday=day,player_name=pname)
        if resp.status == 200:
            if resp.data:
                print "Played on matchday %d" % day
            else:
                print "Did not play on matchday %d" % day

            weekly = [
                calcParticipationPoints(client,resp),
                calcGoalPoints(client,resp),
                calcGoalsAllowedPoints(client,resp),
                calcCleanSheetPoints(client,resp),
                calcGoalAssistPoints(client,resp),
                calcSavePoints(client,resp),
                calcPenaltyPoints(client,resp),
                calcYellowCardPoints(client,resp),
                calcRedCardPoints(client,resp)
                ]

            Total.append(sum(weekly))

            fantasypts = sum(weekly)
            print "Weekly points: ", weekly
            print "Total points: %d" % fantasypts

    # Generate fantasy plot
    plotFantasyCharts(pname, matchdays, Total)
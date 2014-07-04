#!/usr/bin/env/python
# -*- encoding: utf-8 -*-
#
# List of goalscorers in football match.
# (Japan vs Colombia, 2014 FIFA World Cup)
#
from soccermetrics.rest import SoccermetricsRestClient

if __name__ == "__main__":
    client = SoccermetricsRestClient()

    match = client.natl.match.information.get(home_team_name="Japan",
        away_team_name="Colombia")

    for datum in match.data:
        print "Match id for Japan vs Colombia is %d" % datum.id

        for goal in client.link.get(datum.link.goals, sort='time_mins').data:
            print "Goal scored by %s in minute %d by %s" % (
                goal.scoringTeamName,
                goal.timeMins,
                client.link.get(goal.link.player).data[0].fullName)

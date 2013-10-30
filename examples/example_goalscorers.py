#!/usr/bin/env/python
# -*- encoding: utf-8 -*-
#
# List of goalscorers in football match.
# (Arsenal vs Tottenham Hotspur)
#
from soccermetrics.rest import SoccermetricsRestClient

if __name__ == "__main__":
    client = SoccermetricsRestClient()

    match = client.match.information.get(home_team_name="Arsenal",
        away_team_name="Tottenham Hotspur")

    for datum in match.data:
        print "Match id for Arsenal at home to Tottenham is %d" % datum.id

        for goal in client.link.get(datum.link.events.goals, sort='time_mins').data:
            print "Goal scored by %s in minute %d by %s" % (
                goal.scoring_team_name,
                goal.time_mins,
                client.link.get(goal.link.player).data[0].full_name)

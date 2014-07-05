#!/usr/bin/env python
#
# Create a full-time result list for matches in a matchday.
#

import sys
from soccermetrics.rest import SoccermetricsRestClient

if __name__ == "__main__":

    # Create a SoccermetricsRestClient object.  This call assumes that
    # SOCCERMETRICS_APP_ID and SOCCERMETRICS_APP_KEY are in your environment
    # variables, which we recommend.
    client = SoccermetricsRestClient()

    # Get starting and ending matchdays from command-line arguments.
    # Both numbers must be entered.
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python %s <matchday_start> <matchday_end>\n" % sys.argv[0])
        raise SystemExit(1)
    matchday_start = int(sys.argv[1])
    matchday_end = int(sys.argv[2])

    # We will publish the match fixtures for the matchday range.
    for day in range(matchday_start,matchday_end+1):

        # Get match info data from all matches associated with a matchday.  We
        # will make use of the sorting functionality in the Soccermetrics API.
        matches = client.natl.information.get(matchday=day,
                    sort='match_date,kickoff_time').all()

        # Now we can iterate over the sorted match list and we grab goal and
        # penalty kick events for each team.
        for match in matches:
            match_goals = []
            # We use the hyperlinks in the match representation to retrieve goal and
            # penalty kick events under certain conditions.
            for team in [match.homeTeamName,match.awayTeamName]:
                goals = client.link.get(match.link.goals,scoring_team_name=team).all()
                pens = client.link.get(match.link.penalties,player_team_name=team,
                                       outcome_type="Goal").all()

                match_goals.append(len(goals)+len(pens))

            print "Matchday %02s %s %s %30s %d-%d %-30s" % (match.matchday,
                match.matchDate, match.kickoffTime, match.homeTeamName,
                match_goals[0],match_goals[1],match.awayTeamName)
        # A newline to separate the matchdays.
        print

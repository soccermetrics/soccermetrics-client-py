#!/usr/bin/env python
#
# Create a fixture list by retrieving match dates, kickoff times,
# and home/away teams, and other info for matches in a matchday.
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
        matches = client.club.information.get(matchday=day,
                    sort='match_date,kickoff_time').all()

        # Now we can iterate over the sorted match list and print information
        # associated with the match, like the date, time, the two teams, the
        # venue and the referee.  We'll format the string so that it looks nice.
        for match in matches:
            print "Matchday %02s %s %s %30s v %-30s \t%s (%s)" % (match.matchday,
                match.matchDate, match.kickoffTime, match.homeTeamName,
                match.awayTeamName, match.venueName, match.refereeName)
        # A newline to separate the matchdays.
        print


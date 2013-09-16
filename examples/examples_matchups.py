#!/usr/bin/env python
#
# Create a fixture list by retrieving match dates, kickoff times,
# and home/away teams, and other info for matches in a matchday.
#

from soccermetrics.rest import SoccermetricsRestClient

# A closure that we've written to page through the resource
# representation.  We'll add the functionality in a future
# release of the client so that you won't have to write this,
# but we want to make sure you can run this example now.
def iter(resp):
    while True:
        yield (resp.data)
        if not resp.meta.next:
            raise StopIteration
        else:
            resp = client.link.get(resp.meta.next)

if __name__ == "__main__":

    # Create a SoccermetricsRestClient object.  This call assumes that
    # SOCCERMETRICS_APP_ID and SOCCERMETRICS_APP_KEY are in your environment
    # variables, which we recommend.
    client = SoccermetricsRestClient()

    # We will publish the match fixtures for matchdays 2-4.
    for day in range(2,5):
 
        # Get match info data from all matches associated with a matchday.  We
        # will make use of the sorting functionality in the Soccermetrics API.
        matches = []
        for page in iter(client.match.information.get(matchday=day,
                sort='match_date,kickoff_time')):
            matches.extend(page)

        # Now we can iterate over the sorted match list and print information
        # associated with the match, like the date, time, the two teams, the
        # venue and the referee.  We'll format the string so that it looks nice.
        for match in matches:
            print "Matchday %02s %s %s %30s v %-30s \t%s (%s)" % (match.matchday, 
                match.match_date, match.kickoff_time, match.home_team_name, 
                match.away_team_name, match.venue_name, match.referee_name)
        # A newline to separate the matchdays.        
        print
        

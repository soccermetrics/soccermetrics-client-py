#!/usr/bin/env python
#
# Create a full-time result list for matches in a matchday.
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

        # Now we can iterate over the sorted match list and we grab goal and
        # penalty kick events for each team.
        for match in matches:
            match_goals = []
            # We use the hyperlinks in the match representation to retrieve goal and
            # penalty kick events under certain conditions.
            for team in [match.home_team_name,match.away_team_name]:
                goals = client.link.get(match.link.events.goals,scoring_team_name=team).data
                pens = client.link.get(match.link.events.penalties,player_team_name=team,
                                       outcome_type="Goal").data
                    
                match_goals.append(len(goals)+len(pens))
            
            print "Matchday %02s %s %s %30s %d-%d %-30s" % (match.matchday, 
                match.match_date, match.kickoff_time, match.home_team_name, 
                match_goals[0],match_goals[1],match.away_team_name)
        # A newline to separate the matchdays.        
        print

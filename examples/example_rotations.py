#!/usr/bin/env python
#
# Calculate squad rotation in Liverpool's league matches
# in 2011-12 Premier League season.
#

from apiclient.rest import SoccermetricsRestClient

# Create a SoccermetricsRestClient object.  This call assumes that
# SOCCERMETRICS_APP_ID and SOCCERMETRICS_APP_KEY are in your environment
# variables, which we recommend.
client = SoccermetricsRestClient()

# Get unique IDs of all of Liverpool's matches.  We want the matches in order,
# so we do a few things:
#   (1) We query all of Liverpool's home matches, then all of their away matches
#       and join the results together.
#   (2) We sort the results by match date.
#   (3) The unique ID is all we need, so let's iterate through the list of
#       results and create a new list of IDs.
matches = client.match.information.get(home_team_name="Liverpool") + \
          client.match.information.get(away_team_name="Liverpool")
sorted_matches = sorted(matches, key=lambda k: k['match_date'])
matchIDs = [x['id'] for x in sorted_matches]

# Get all starting lineup information for Liverpool's matches.  We are interested
# in just the starting players for Liverpool, so we make player_team = 'Liverpool'
# and set is_starting to True.
starters = []
for matchID in matchIDs:
    lineup_data = client.match.lineups.get(match=matchID,
        player_team_name="Liverpool",is_starting=True)
    player_list = [x['player'] for x in lineup_data]
    starters.append(player_list)

rotation_list = []
for day in range(1,len(matches)):
    rotation_list.append(11 - len(set(starters[day-1]).intersection(starters[day])))
#!/usr/bin/env python
#
# Calculate squad rotation in Liverpool's league matches
# in 2011-12 Premier League season.
#

from soccermetrics.rest import SoccermetricsRestClient

client = SoccermetricsRestClient()

home_club = "Liverpool"
away_club = "Everton"

# get match information
match = client.information.get(home_team_name=home_club, away_team_name=away_club)


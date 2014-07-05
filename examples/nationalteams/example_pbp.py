#!/usr/bin/env python
#
# Compute changes in on-field composition during
# a 2012-13 Premier League match.
#

from soccermetrics.rest import SoccermetricsRestClient

client = SoccermetricsRestClient()

home_club = "Brazil"
away_club = "Croatia"

# get match information
match = client.natl.information.get(home_team_name=home_club,
                                    away_team_name=away_club).all()

# collect name and ID of all players in lineups
lineup = client.link.get(match[0].link.lineups).all()
players = {x.player:x.playerName for x in lineup}

# get all segments of the match
segments = client.link.get(match[0].link.analytics.segments).all()

# loop over all segments
# return players in each segment
platoon = lambda rec: ', '.join([players[_id] for _id in rec])

for segment in segments:
    if segment.startStoppageMins > 0:
        match_time = "%d+%d" % (segment.startTimeMins,
                                segment.startStoppageMins)
    else:
        match_time = "%d" % segment.startTimeMins
    print "Start segment: %s" % match_time
    print "Home Players: %s" % platoon(segment.homePlayersOn)
    print "Away Players: %s" % platoon(segment.awayPlayersOn)
    print "Duration: %s mins" % segment.duration
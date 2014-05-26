#!/usr/bin/env python
#
# Calculate squad rotation in Liverpool's league matches
# in 2011-12 Premier League season.
#

from soccermetrics.rest import SoccermetricsRestClient

if __name__ == "__main__":

    # Create a SoccermetricsRestClient object.  This call assumes that
    # SOCCERMETRICS_APP_ID and SOCCERMETRICS_APP_KEY are in your environment
    # variables, which we recommend.
    client = SoccermetricsRestClient()

    # Create STARTING_XI constant and set it to 11.
    # It's not necessary, but we don't like to hard-code numbers.
    STARTING_XI = 11

    # Set club variable to Liverpool.  Enables reuse if we want to
    # repeat this analysis with other clubs.
    club_name = "Liverpool"

    # Get unique IDs of all of Liverpool's matches.  We want the matches in order,
    # so we do a few things:
    #   (1) We query all of Liverpool's home matches, then all of their away matches
    #       and join the results together.
    #   (2) We sort the results by match date.
    matches = []
    for key in ['home_team_name','away_team_name']:
        param = {key: club_name}
        matches.extend(client.match.information.get(**param).all())
    sorted_matches = sorted(matches, key=lambda k: k.matchDate)

    starters = []
    rotation_list = []
    for match in sorted_matches:
        # Get all starting lineup information for Liverpool's matches.  We are interested
        # in just the starting players for Liverpool, so we make player_team = 'Liverpool'
        # and set is_starting to True.
        lineup_data = client.link.get(match.link.lineups,player_team_name=club_name,
            is_starting=True).all()
        player_list = [x.player for x in lineup_data]
        starters.append(player_list)
        # After the first match, compute the number of players who are in the current
        # lineup and the previous one.  Subtract that number from STARTING_XI to
        # get the number of squad rotations.
        if len(starters) > 1:
            num_no_changes = len(set(starters[-2]).intersection(starters[-1]))
            rotation_list.append(dict(date=match.matchDate,
                matchday=match.matchday,
                rotations=STARTING_XI-num_no_changes))

    # Display the rotation history and a running total of squad rotations.
    print "Match\tMatch Date\tRotations\tTotal Rotations"
    cumul = []
    for datum in rotation_list:
        cumul.append(datum['rotations'])
        print "%d\t%s\t%d\t%d" % (datum['matchday'],datum['date'],datum['rotations'],
                                  sum(cumul))
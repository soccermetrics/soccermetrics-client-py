#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Create a statistical record of a team' performance
# under a manager.
#

from soccermetrics.rest import SoccermetricsRestClient

if __name__ == "__main__":

    # Create a SoccermetricsRestClient object.  This call assumes that
    # SOCCERMETRICS_APP_ID and SOCCERMETRICS_APP_KEY are in your environment
    # variables, which we recommend.
    client = SoccermetricsRestClient()

    # Get data for one manager.
    manager = client.managers.get(full_name=u'Luiz Scolari').data[0]

    # Get lists of home and away matches in which manager was involved, using
    # the hyperlinks in the manager representation.  Combine both lists and
    # sort by match date.
    hmatches = client.link.get(manager.link.natl.homeMatches,sort="match_date").all()
    amatches = client.link.get(manager.link.natl.awayMatches,sort="match_date").all()
    matches = sorted(hmatches + amatches,key=lambda k: k.matchDate)

    # Create a list of match substitution timings
    sub_list = []
    for match in matches:
        # The team key is either home_team_name or away_team_name depending on
        # whether the manager is the home or away manager. This ternary statement
        # assigns the team key.
        team_key = 'home_team_name' if match.homeManagerName == manager.fullName \
            else 'away_team_name'

        # We use the hyperlinks in the match representation to retrieve all
        # substitution data for one of the two teams involved, sorted by match time
        # and then stoppage time.
        subs = client.link.get(match.link.substitutions,
            team_name=getattr(match,team_key),sort="time_mins,stoppage_mins").data

        # Create a dictionary of substitution times in order.  Fortunately
        # 'first', 'second', and 'third' are in alphabetical order!  Initialize
        # all values in the dictionary to None, which allows us to account for
        # unused subs.
        sub_dict = dict(first=None,second=None,third=None)
        subkeys = sorted(sub_dict.keys())
        # Loop over the ordered match substitution data and assign the match
        # times to the ordered keys.
        for k, sub in enumerate(subs):
            sub_dict[subkeys[k]] = int(sub.timeMins)

        # This is a diagnostic to the user.  Display the matchday, the teams,
        # and the substitutions made by the manager.
        print "Matchday %2s: %s v %s: " % (match.matchday, match.homeTeamName,
            match.awayTeamName),
        print sub_dict['first'],sub_dict['second'],sub_dict['third']

        # Append the substitution dictionary to the list.
        sub_list.append(sub_dict)

    # Create a temporary function to convert a list of dictionary key/values
    # to a list of values, given a specific key.  If a value is None,
    # ignore it.
    dict2list = lambda vec,k: [x[k] for x in vec if x[k]]

    # Calculate the average time of the first, second, and third substitution.
    avg1st = sum(dict2list(sub_list,'first'))/len(dict2list(sub_list,'first'))
    avg2nd = sum(dict2list(sub_list,'second'))/len(dict2list(sub_list,'second'))
    avg3rd = sum(dict2list(sub_list,'third'))/len(dict2list(sub_list,'third'))

    print avg1st, avg2nd, avg3rd
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
    manager = client.managers.get(full_name=u'Roberto Mancini').data[0]

    # get list of matches in which manager was involved
    hmatches = client.link.get(manager.link.home_matches,sort="match_date").all()
    amatches = client.link.get(manager.link.away_matches,sort="match_date").all()

    matches = sorted(hmatches + amatches,key=lambda k: k.match_date)

    sub_list = []
    for match in matches:
        team_key = 'home_team_name' if match.home_manager_name == manager.full_name \
            else 'away_team_name'

        subs = client.link.get(match.link.events.substitutions,
            team_name=getattr(match,team_key),sort="time_mins,stoppage_mins").data

        sub_dict = dict(first=None,second=None,third=None)
        subkeys = sorted(sub_dict.keys())
        for k, sub in enumerate(subs):
            sub_dict[subkeys[k]] = int(sub.time_mins)

        print "Matchday %2s: %s v %s: " % (match.matchday, match.home_team_name,
            match.away_team_name),
        print sub_dict['first'],sub_dict['second'],sub_dict['third']

        sub_list.append(sub_dict)

    dict2list = lambda vec,k: [x[k] for x in vec if x[k]]

    avg1st = sum(dict2list(sub_list,'first'))/len(dict2list(sub_list,'first'))
    avg2nd = sum(dict2list(sub_list,'second'))/len(dict2list(sub_list,'second'))
    avg3rd = sum(dict2list(sub_list,'third'))/len(dict2list(sub_list,'third'))

    print avg1st, avg2nd, avg3rd
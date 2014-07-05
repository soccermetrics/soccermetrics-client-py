#!/usr/bin/env python
#
# Create a statistical record of a referee's performance,
# from time added on to cards shown to fouls called.
#

from soccermetrics.rest import SoccermetricsRestClient

if __name__ == "__main__":

    # Create a SoccermetricsRestClient object.  This call assumes that
    # SOCCERMETRICS_APP_ID and SOCCERMETRICS_APP_KEY are in your environment
    # variables, which we recommend.
    client = SoccermetricsRestClient()

    # Get data for one referee.
    referee = client.referees.get(full_name="Howard Webb").data[0]

    # Get list of matches that referee directed
    matches = client.link.get(referee.link.natl.matches,sort="match_date").all()

    # Use lengths of match halves to create list of time added on by referee
    timeon = [dict(first=45-match.firsthalfLength,second=45-match.secondhalfLength)
              for match in matches]

    # Iterate over list of matches and access penalty and disciplinary events
    # associated with each match.  Report the number of penalties, yellow cards,
    # yellow/red and red cards to the screen, as well as time added on.
    penalties = []
    yellows = []
    reds = []
    for match in matches:
        match_pens = client.link.get(match.link.penalties).all()
        match_yellows = client.link.get(match.link.offenses,card_type="Yellow").all()
        match_2ndyellows = client.link.get(match.link.offenses,card_type="Yellow/Red").all()
        match_reds = client.link.get(match.link.offenses,card_type="Red").all()

        penalties.extend(match_pens)
        yellows.extend(match_yellows)
        reds.extend(match_2ndyellows + match_reds)

        print """%s,%s v %s,%d,%d,%d,%d,%d,%d""" % (match.matchday,
                    match.homeTeamName, match.awayTeamName, len(match_pens),
                    len(match_yellows), len(match_2ndyellows), len(match_reds),
                    match.firsthalfLength, match.secondhalfLength)

    # Create a temporary function to convert list of dictionaries to a list
    # of values associated with a key.
    dict2list = lambda vec,k: [x[k] for x in vec]

    # Create a unique list of fouls called by the referee.
    foul_list = set(dict2list(yellows,'foulType')+dict2list(reds,'foulType'))

    # Print list of fouls and number of yellow and red cards given for them.
    print "Foul Type,Yellows,Reds"
    for foul in foul_list:
        print "%30s,%2d,%2d" % (foul,
            sum([1 for x in yellows if x['foulType'] == foul]),
            sum([1 for x in reds if x['foulType'] == foul]))



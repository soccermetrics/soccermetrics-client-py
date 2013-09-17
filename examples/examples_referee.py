#!/usr/bin/env python
#
# Create a statistical record of a referee's performance,
# from time added on to cards shown to fouls called.
#

from soccermetrics.rest import SoccermetricsRestClient

# A closure that we've written to page through the resource
# representation.  We'll add the functionality in a future
# release of the client so that you won't have to write this,
# but we want to make sure you can run this example now.
def iter(resp):
    while True:
        yield (resp.data)
        if not resp.meta or not resp.meta.next:
            raise StopIteration
        else:
            resp = client.link.get(resp.meta.next)

if __name__ == "__main__":

    # Create a SoccermetricsRestClient object.  This call assumes that
    # SOCCERMETRICS_APP_ID and SOCCERMETRICS_APP_KEY are in your environment
    # variables, which we recommend.
    client = SoccermetricsRestClient()

    # Get data for one referee.
    referee = client.referees.get(full_name="Howard Webb").data[0]

    # get list of matches that referee directed
    matches = []
    for page in iter(client.link.get(referee.link.matches,sort="match_date")):
        matches.extend(page)

    # iterate through matches, pull out time added on
    timeon = []
    penalties = []
    yellows = []
    reds = []
    for match in matches:
        timeon.append(dict(first=match.firsthalf_length,second=match.secondhalf_length))

        match_pens = client.link.get(match.link.events.penalties).data
        match_yellows = []
        for page in iter(client.link.get(match.link.events.offenses,card_type="Yellow")):
            match_yellows.extend(page)
        match_2ndyellows = client.link.get(match.link.events.offenses,card_type="Yellow/Red").data
        match_reds = client.link.get(match.link.events.offenses,card_type="Red").data

        penalties.extend(match_pens)
        yellows.extend(match_yellows)
        reds.extend(match_2ndyellows + match_reds)

        print """Matchday %s: %s v %s: Penalties %d Yellow %d Yellow/Red %d Red %d  1st Half %d  2nd Half %d""" % (match.matchday,
                    match.home_team_name, match.away_team_name, len(match_pens),
                    len(match_yellows), len(match_2ndyellows), len(match_reds),
                    match.firsthalf_length, match.secondhalf_length)

    dict2list = lambda vec,k: [x[k] for x in vec]

    foul_list = set(dict2list(yellows,'foul_type')+dict2list(reds,'foul_type'))

    print "Foul Type\tYellows\tReds"
    for foul in foul_list:
        print "%30s\t%2d\t%2d" % (foul,
            sum([1 for x in yellows if x['foul_type'] == foul]),
            sum([1 for x in reds if x['foul_type'] == foul]))



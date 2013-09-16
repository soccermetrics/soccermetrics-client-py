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
    for page in iter(client.link.get(referee.link.matches)):
        matches.extend(page)
    
    # iterate through matches, pull out time added on
    timeon = []
    penalties = []
    yellows = []
    reds = []
    for match in matches:
        timeon.append(dict(first=match.firsthalf_length,second=match.secondhalf_length))
        penalties.extend(client.link.get(match.link.events.penalties).data)
        for page in iter(client.link.get(match.link.events.offenses,card_type="Yellow")):
            yellows.extend(page)
        reds.extend(client.link.get(match.link.events.offenses,card_type="Yellow/Red").data +
                    client.link.get(match.link.events.offenses,card_type="Red").data)

    dict2list = lambda vec,k: [x[k] for x in vec]
    
    first_half_avg = sum(dict2list(timeon,'first'))/len(dict2list(timeon,'first'))
    second_half_avg = sum(dict2list(timeon,'second'))/len(dict2list(timeon,'second'))
    
    foul_list = set(dict2list(yellows,'foul_type'))
    
    print foul_list


import os

from apiclient import SoccermetricsException
from apiclient.rest.resources import Root
from apiclient.rest.resources import Link
from apiclient.rest.resources import Validation
from apiclient.rest.resources import Personnel
from apiclient.rest.resources import Match
from apiclient.rest.resources import MatchEvents
from apiclient.rest.resources import MatchStatistics

def find_credentials():
    """
    Search for API credentials in current environment.
    """
    try:
        account = os.environ["SOCCERMETRICS_APP_ID"]
        api_key = os.environ["SOCCERMETRICS_APP_KEY"]
        return account, api_key
    except KeyError:
        return None, None

class SoccermetricsRestClient(object):
    """
    A client for accessing the Soccermetrics REST API.
    """
    def __init__(self, account=None, api_key=None,
        base_uri="http://api-summary.soccermetrics.net"):
        super(SoccermetricsRestClient, self).__init__()

        if not account or api_key:
            account, api_key = find_credentials()
            if not (account and api_key):
                raise SoccermetricsException("""
Soccermetrics API could not find your credentials.  Pass them into
the SoccermetricsRestClient like this:

    client = SoccermetricsRestClient(account='xxxxxxxxxxx',
                              key='yyyyyyyyyyyyyyyyy')

Or, add your credentials to your shell environment. From the terminal, run

    echo "export SOCCERMETRICS_APP_ID=xxxxxxxxxxx" >> ~/.bashrc
    echo "export SOCCERMETRICS_APP_KEY=yyyyyyyyyyyyyyyyy" >> ~/.bashrc

and be sure to replace the values for the application ID and auth key with the
values from your Soccermetrics API Account at http://soccermetrics.3scale.net
""")

        auth = {'app_id': account, 'app_key': api_key}

        # Service root
        self.root = Root(base_uri, auth)

        # Access to links in API responses
        self.link = Link(base_uri, auth)

        # Validation objects
        self.confederations = Validation("confederations", base_uri, auth)
        self.countries = Validation("countries", base_uri, auth)
        self.seasons = Validation("seasons", base_uri, auth)
        self.teams = Validation("teams", base_uri, auth)
        self.venues = Validation("venues", base_uri, auth)
        self.persons = Validation("persons", base_uri, auth)
        self.positions = Validation("positions", base_uri, auth)
        self.fouls = Validation("fouls", base_uri, auth)
        self.cards = Validation("cards", base_uri, auth)
        self.bodyparts = Validation("bodyparts", base_uri, auth)
        self.shotevents = Validation("shotevents", base_uri, auth)
        self.penalty_outcomes = Validation("penalty_outcomes", base_uri, auth)
        self.weather = Validation("weather", base_uri, auth)
        self.surfaces = Validation("surfaces", base_uri, auth)

        # Personnel objects
        self.players = Personnel("players", base_uri, auth)
        self.managers = Personnel("managers", base_uri, auth)
        self.referees = Personnel("referees", base_uri, auth)

        # Match objects
        self.match = Match(base_uri, auth)

        # Match Event objects
        self.events = MatchEvents(base_uri, auth)

        # Match Statistics objects
        self.stats = MatchStatistics(base_uri, auth)
import os

from soccermetrics import SoccermetricsException
from soccermetrics.rest.resources import Root
from soccermetrics.rest.resources import Link
from soccermetrics.rest.resources import Validation
from soccermetrics.rest.resources import Personnel
from soccermetrics.rest.resources import Match
from soccermetrics.rest.resources import MatchEvents
from soccermetrics.rest.resources import MatchStatistics
from soccermetrics.rest.resources import MatchAnalytics

def find_credentials():
    """
    Search for API credentials in current environment.

    Looks for ``SOCCERMETRICS_APP_ID`` and ``SOCCERMETRICS_APP_KEY``
    among the environment variables.  Returns a KeyError if
    either variable is not present in the environment.

    :returns: (account, api_key) or (None, None)
    """
    try:
        account = os.environ["SOCCERMETRICS_APP_ID"]
        api_key = os.environ["SOCCERMETRICS_APP_KEY"]
        return account, api_key
    except KeyError:
        return None, None

class SoccermetricsRestClient(object):
    """A client object for accessing the Soccermetrics REST API.

    +------------------+----------------------------+
    | Attribute        | Description                |
    +==================+============================+
    | root             | Service root               |
    +------------------+----------------------------+
    | link             | Link to resources          |
    +------------------+----------------------------+
    | confederations   | Confederations             |
    +------------------+----------------------------+
    | countries        | Countries                  |
    +------------------+----------------------------+
    | seasons          | Seasons                    |
    +------------------+----------------------------+
    | teams            | Teams                      |
    +------------------+----------------------------+
    | venues           | Venues                     |
    +------------------+----------------------------+
    | persons          | Persons                    |
    +------------------+----------------------------+
    | positions        | Positions                  |
    +------------------+----------------------------+
    | fouls            | Fouls                      |
    +------------------+----------------------------+
    | cards            | Cards                      |
    +------------------+----------------------------+
    | bodyparts        | Body parts                 |
    +------------------+----------------------------+
    | shotevents       | Shot events                |
    +------------------+----------------------------+
    | penaltyOutcomes  | Penalty outcomes           |
    +------------------+----------------------------+
    | weather          | Weather conditions         |
    +------------------+----------------------------+
    | surfaces         | Surfaces                   |
    +------------------+----------------------------+
    | players          | Players                    |
    +------------------+----------------------------+
    | managers         | Managers                   |
    +------------------+----------------------------+
    | referees         | Referees                   |
    +------------------+----------------------------+
    | match            | Match resources            |
    +------------------+----------------------------+
    | events           | Match event resources      |
    +------------------+----------------------------+
    | stats            | Match stat resources       |
    +------------------+----------------------------+
    | analytics        | Match analytics resources  |
    +------------------+----------------------------+

    :param account: Soccermetrics API Application ID.
    :type account: string or None
    :param api_key: Soccermetrics API Application key.
    :type api_key: string or None
    """
    def __init__(self, account=None, api_key=None,
        base_uri="http://api-summary.soccermetrics.net"):
        super(SoccermetricsRestClient, self).__init__()

        if not (account or api_key):
            account, api_key = find_credentials()
            if not (account and api_key):
                raise SoccermetricsException("""
Soccermetrics API could not find your credentials.  Pass them into
the SoccermetricsRestClient like this:

    client = SoccermetricsRestClient(account='xxxxxxxxxxx',
                              api_key='yyyyyyyyyyyyyyyyy')

Or, add your credentials to your shell environment. From the terminal, run

    echo "export SOCCERMETRICS_APP_ID=xxxxxxxxxxx" >> ~/.bashrc
    echo "export SOCCERMETRICS_APP_KEY=yyyyyyyyyyyyyyyyy" >> ~/.bashrc

and be sure to replace the values for the application ID and auth key with the
values from your Soccermetrics API Account at http://soccermetrics.3scale.net.
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
        self.penaltyOutcomes = Validation("penalty_outcomes", base_uri, auth)
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

        # Match Analytics objects
        self.analytics = MatchAnalytics(base_uri, auth)
import os

from soccermetrics import SoccermetricsException
from soccermetrics.rest.resources import Root
from soccermetrics.rest.resources import Link
from soccermetrics.rest.resources import Validation
from soccermetrics.rest.resources import Personnel
from soccermetrics.rest.resources import MatchPlay
from soccermetrics.rest.resources import MatchAnalytics

def find_credentials():
    """
    Search for API credentials in current environment.

    Looks for ``SOCCERMETRICS_APP_ID`` and ``SOCCERMETRICS_APP_KEY``
    among the environment variables.  Returns a ``(None, None)``
    tuple if neither variable is not present in the environment.

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
    | validation       | Validation resources       |
    +------------------+----------------------------+
    | players          | Players resource           |
    +------------------+----------------------------+
    | managers         | Managers resource          |
    +------------------+----------------------------+
    | referees         | Referees resource          |
    +------------------+----------------------------+
    | club             | Club match resources       |
    +------------------+----------------------------+
    | natl             | Nat'l team match resources |
    +------------------+----------------------------+
    | analytics        | Match analytics resources  |
    +------------------+----------------------------+

    :param account: Soccermetrics API Application ID from `your account
        dashboard <https://developer.soccermetrics.net/admin/access_details>`_.
    :type account: string or None
    :param api_key: Soccermetrics API Application key from `your account
        dashboard <https://developer.soccermetrics.net/admin/access_details>`_.
    :type api_key: string or None
    """
    def __init__(self, account=None, api_key=None,
        base_uri="https://api-connect.soccermetrics.net"):
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
values from your Soccermetrics API Account at https://developer.soccermetrics.net/admin/access_details.
""")

        auth = {'app_id': account, 'app_key': api_key}

        # Service root
        self.root = Root(base_uri, auth)

        # Access to links in API responses
        self.link = Link(base_uri, auth)

        # Validation objects
        self.validation = Validation(base_uri, auth)

        # Personnel objects
        self.players = Personnel("players", base_uri, auth)
        self.managers = Personnel("managers", base_uri, auth)
        self.referees = Personnel("referees", base_uri, auth)

        # Match objects for club/national team play
        self.club = MatchPlay("clubs", base_uri, auth)
        self.natl = MatchPlay("national", base_uri, auth)

        # Match Analytics objects
        self.analytics = MatchAnalytics(base_uri, auth)
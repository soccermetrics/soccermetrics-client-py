import unittest
from os import environ

import soccermetrics
from soccermetrics import SoccermetricsException
from soccermetrics.rest import SoccermetricsRestClient, find_credentials

class NoCredentialsTest(unittest.TestCase):
    """
    Test outcome of find_credentials() given absence of environment variables.
    """

    def setUp(self):
        if 'SOCCERMETRICS_APP_KEY' in environ.keys():
            del environ['SOCCERMETRICS_APP_KEY']
        if 'SOCCERMETRICS_APP_ID' in environ.keys():
            del environ['SOCCERMETRICS_APP_ID']

    def test_no_credentials(self):
        account, api_key = find_credentials()
        self.assertEqual(account, None)
        self.assertEqual(api_key,None)

class PartialCredentialsTest(unittest.TestCase):
    """
    Test outcome of find_credentials() given partial presence of environment variables.
    """

    def setUp(self):
        environ['SOCCERMETRICS_APP_KEY'] = 'AUTH_TOKEN'
        if 'SOCCERMETRICS_APP_ID' in environ.keys():
            del environ['SOCCERMETRICS_APP_ID']

    def test_partial_credentials(self):
        account, api_key = find_credentials()
        self.assertEqual(account, None)
        self.assertEqual(api_key,None)

class FullCredentialsTest(unittest.TestCase):
    """
    Test outcome of find_credentials() given presence of environment variables.
    """

    def setUp(self):
        environ['SOCCERMETRICS_APP_KEY'] = 'AUTH_TOKEN'
        environ['SOCCERMETRICS_APP_ID'] = 'APP_ID'

    def test_full_credentials(self):
        account, api_key = find_credentials()
        self.assertEqual(account, 'APP_ID')
        self.assertEqual(api_key,'AUTH_TOKEN')

class RestClientTest(unittest.TestCase):
    """
    Test for successful connection to SoccermetricsRestClient.
    """

    def setUp(self):
        if 'SOCCERMETRICS_APP_KEY' in environ.keys():
            del environ['SOCCERMETRICS_APP_KEY']
        if 'SOCCERMETRICS_APP_ID' in environ.keys():
            del environ['SOCCERMETRICS_APP_ID']

    def test_fail_connect(self):
        self.assertRaises(SoccermetricsException, SoccermetricsRestClient)

    def test_connect(self):
        self.client = SoccermetricsRestClient(account="APP_ID",api_key="APP_KEY")
        self.assertIsInstance(self.client, SoccermetricsRestClient)

class RestClientAttributeTest(unittest.TestCase):
    """
    Test for presence of attributes in SoccermetricsRestClient object.
    """

    def setUp(self):
        self.client = SoccermetricsRestClient(account="APP_ID",api_key="APP_KEY")

    def test_https_endpoint(self):
        self.assertTrue(self.client.root.base_uri.startswith("https"))

    def test_service_root(self):
        self.assertIsInstance(self.client.root, soccermetrics.rest.resources.Root)

    def test_link(self):
        self.assertIsInstance(self.client.link, soccermetrics.rest.resources.Link)

    def test_validation(self):
        self.assertIsInstance(self.client.validation.confederations,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.countries,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.seasons,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.teams,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.venues,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.persons,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.positions,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.fouls,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.cards,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.bodyparts,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.shotevents,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.penaltyOutcomes,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.weather,
            soccermetrics.rest.resources.validation.ValidationResource)
        self.assertIsInstance(self.client.validation.surfaces,
            soccermetrics.rest.resources.validation.ValidationResource)


    def test_personnel(self):
        self.assertIsInstance(self.client.players,
            soccermetrics.rest.resources.Personnel)
        self.assertIsInstance(self.client.managers,
            soccermetrics.rest.resources.Personnel)
        self.assertIsInstance(self.client.referees,
            soccermetrics.rest.resources.Personnel)

    def test_club(self):

        self.assertIsInstance(self.client.club,
            soccermetrics.rest.resources.MatchPlay)

        self.assertIsInstance(self.client.club.information,
            soccermetrics.rest.resources.match.MatchInformation)

        self.assertIsInstance(self.client.club.lineups,
            soccermetrics.rest.resources.match.MatchLineups)

        self.assertIsInstance(self.client.club.conditions,
            soccermetrics.rest.resources.match.MatchConditions)

        self.assertIsInstance(self.client.club.goals,
            soccermetrics.rest.resources.match.MatchGoals)

        self.assertIsInstance(self.client.club.penalties,
            soccermetrics.rest.resources.match.MatchPenalties)

        self.assertIsInstance(self.client.club.offenses,
            soccermetrics.rest.resources.match.MatchOffenses)

        self.assertIsInstance(self.client.club.substitutions,
            soccermetrics.rest.resources.match.MatchSubstitutions)

        self.assertIsInstance(self.client.club.stats,
            soccermetrics.rest.resources.statistics.MatchStatistics)

        self.assertIsInstance(self.client.club.events,
            soccermetrics.rest.resources.events.MatchEvents)

    def test_natl(self):

        self.assertIsInstance(self.client.natl,
            soccermetrics.rest.resources.MatchPlay)

        self.assertIsInstance(self.client.natl.information,
            soccermetrics.rest.resources.match.MatchInformation)

        self.assertIsInstance(self.client.natl.lineups,
            soccermetrics.rest.resources.match.MatchLineups)

        self.assertIsInstance(self.client.natl.conditions,
            soccermetrics.rest.resources.match.MatchConditions)

        self.assertIsInstance(self.client.natl.goals,
            soccermetrics.rest.resources.match.MatchGoals)

        self.assertIsInstance(self.client.natl.penalties,
            soccermetrics.rest.resources.match.MatchPenalties)

        self.assertIsInstance(self.client.natl.offenses,
            soccermetrics.rest.resources.match.MatchOffenses)

        self.assertIsInstance(self.client.natl.substitutions,
            soccermetrics.rest.resources.match.MatchSubstitutions)

        self.assertIsInstance(self.client.natl.stats,
            soccermetrics.rest.resources.statistics.MatchStatistics)

        self.assertIsInstance(self.client.natl.events,
            soccermetrics.rest.resources.events.MatchEvents)

    def test_analytics(self):
        self.assertIsInstance(self.client.analytics,
            soccermetrics.rest.resources.MatchAnalytics)



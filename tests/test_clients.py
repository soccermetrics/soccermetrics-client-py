import unittest
from os import environ

import soccermetrics
from soccermetrics import SoccermetricsException
from soccermetrics.rest import SoccermetricsRestClient, find_credentials

class NoCredentialsTest(unittest.TestCase):

    def setUp(self):
        if environ.has_key('SOCCERMETRICS_APP_KEY'):
            del environ['SOCCERMETRICS_APP_KEY']
        if environ.has_key('SOCCERMETRICS_APP_ID'):
            del environ['SOCCERMETRICS_APP_ID']

    def test_no_credentials(self):
        account, api_key = find_credentials()
        self.assertEqual(account, None)
        self.assertEqual(api_key,None)

class PartialCredentialsTest(unittest.TestCase):

    def setUp(self):
        environ['SOCCERMETRICS_APP_KEY'] = 'AUTH_TOKEN'
        if environ.has_key('SOCCERMETRICS_APP_ID'):
            del environ['SOCCERMETRICS_APP_ID']

    def test_partial_credentials(self):
        account, api_key = find_credentials()
        self.assertEqual(account, None)
        self.assertEqual(api_key,None)

class FullCredentialsTest(unittest.TestCase):

    def setUp(self):
        environ['SOCCERMETRICS_APP_KEY'] = 'AUTH_TOKEN'
        environ['SOCCERMETRICS_APP_ID'] = 'APP_ID'

    def test_full_credentials(self):
        account, api_key = find_credentials()
        self.assertEqual(account, 'APP_ID')
        self.assertEqual(api_key,'AUTH_TOKEN')

class RestClientTest(unittest.TestCase):

    def setUp(self):
        if environ.has_key('SOCCERMETRICS_APP_KEY'):
            del environ['SOCCERMETRICS_APP_KEY']
        if environ.has_key('SOCCERMETRICS_APP_ID'):
            del environ['SOCCERMETRICS_APP_ID']

    def test_fail_connect(self):
        self.assertRaises(SoccermetricsException, SoccermetricsRestClient)

    def test_connect(self):
        self.client = SoccermetricsRestClient(account="APP_ID",api_key="APP_KEY")
        self.assertIsInstance(self.client, SoccermetricsRestClient)

class RestClientAttributeTest(unittest.TestCase):

    def setUp(self):
        self.client = SoccermetricsRestClient(account="APP_ID",api_key="APP_KEY")

    def test_service_root(self):
        self.assertIsInstance(self.client.root, soccermetrics.rest.resources.Root)

    def test_link(self):
        self.assertIsInstance(self.client.link, soccermetrics.rest.resources.Link)

    def test_validation(self):
        self.assertIsInstance(self.client.confederations,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.countries,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.seasons,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.teams,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.venues,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.persons,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.positions,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.fouls,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.cards,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.bodyparts,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.shotevents,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.penalty_outcomes,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.weather,
            soccermetrics.rest.resources.Validation)
        self.assertIsInstance(self.client.surfaces,
            soccermetrics.rest.resources.Validation)


    def test_personnel(self):
        self.assertIsInstance(self.client.players,
            soccermetrics.rest.resources.Personnel)
        self.assertIsInstance(self.client.managers,
            soccermetrics.rest.resources.Personnel)
        self.assertIsInstance(self.client.referees,
            soccermetrics.rest.resources.Personnel)

    def test_match(self):
        self.assertIsInstance(self.client.match,
            soccermetrics.rest.resources.Match)

    def test_events(self):
        self.assertIsInstance(self.client.events,
            soccermetrics.rest.resources.MatchEvents)

    def test_stats(self):
        self.assertIsInstance(self.client.stats,
            soccermetrics.rest.resources.MatchStatistics)

if __name__ == '__main__':
    unittest.main()
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
        self.client = SoccermetricsRestClient(account="APP_ID",api_key="API_KEY")
        # self.assertIsInstance(self.client, SoccermetricsRestClient)

if __name__ == '__main__':
    unittest.main()
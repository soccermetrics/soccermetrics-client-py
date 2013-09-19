import unittest

import soccermetrics
from soccermetrics import __api_version__
from soccermetrics.rest import SoccermetricsRestClient
from soccermetrics.rest.resource import Resource

class ResourceTest(unittest.TestCase):

    def setUp(self):
        base_url = "http://api-summary.soccermetrics.net"
        auth = dict(account="APP_ID",api_key="APP_KEY")
        self.resource = Resource(base_url, auth)

    def test_initialization(self):
        self.assertEqual(self.resource.auth['account'],"APP_ID")
        self.assertEqual(self.resource.auth['api_key'],"APP_KEY")
        self.assertEqual(self.resource.endpoint,'/%s' % __api_version__)
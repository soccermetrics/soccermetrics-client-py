import unittest

from soccermetrics.rest import SoccermetricsRestClient

class ClientEndpointTest(unittest.TestCase):
    """
    Test endpoints of API resources in client.
    """

    def setUp(self):
        self.client = SoccermetricsRestClient(account="APP_ID",api_key="APP_KEY")

    def test_service_root(self):
        self.assertEqual(self.client.root.endpoint, "/v1/")
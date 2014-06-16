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

    def test_base_endpoints(self):
        self.assertEqual(self.client.validation.phases.endpoint, "/v1/phases")
        self.assertEqual(self.client.validation.groupRounds.endpoint, '/v1/grouprounds')
        self.assertEqual(self.client.validation.knockoutRounds.endpoint, '/v1/knockoutrounds')
        self.assertEqual(self.client.validation.confederations.endpoint, '/v1/confederations')
        self.assertEqual(self.client.validation.countries.endpoint, '/v1/countries')
        self.assertEqual(self.client.validation.seasons.endpoint, '/v1/seasons')
        self.assertEqual(self.client.validation.teams.endpoint, '/v1/teams')
        self.assertEqual(self.client.validation.venues.endpoint, '/v1/venues')
        self.assertEqual(self.client.validation.timezones.endpoint, '/v1/timezones')
        self.assertEqual(self.client.validation.persons.endpoint, '/v1/persons')
        self.assertEqual(self.client.validation.positions.endpoint, '/v1/positions')
        self.assertEqual(self.client.validation.fouls.endpoint, '/v1/fouls')
        self.assertEqual(self.client.validation.cards.endpoint, '/v1/cards')
        self.assertEqual(self.client.validation.bodyparts.endpoint, '/v1/bodyparts')
        self.assertEqual(self.client.validation.shotevents.endpoint, '/v1/shotevents')
        self.assertEqual(self.client.validation.penaltyOutcomes.endpoint, '/v1/penalty_outcomes')
        self.assertEqual(self.client.validation.weather.endpoint, '/v1/weather')
        self.assertEqual(self.client.validation.surfaces.endpoint, '/v1/surfaces')

    def test_personnel_endpoints(self):
        self.assertEqual(self.client.players.endpoint, '/v1/personnel/players')
        self.assertEqual(self.client.managers.endpoint, '/v1/personnel/managers')
        self.assertEqual(self.client.referees.endpoint, '/v1/personnel/referees')

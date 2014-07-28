import unittest

from soccermetrics.rest import SoccermetricsRestClient

class ClientEndpointTest(unittest.TestCase):
    """
    Test endpoints of API resources in client.
    """

    def setUp(self):
        self.client = SoccermetricsRestClient(account="APP_ID",api_key="APP_KEY")

    def test_service_root(self):
        """Verify service root endpoint."""
        self.assertEqual(self.client.root.endpoint, "/v1/")

    def test_validation_endpoints(self):
        """Verify validation resource endpoints without ID."""
        self.assertEqual(self.client.validation.phases.endpoint, "/v1/phases")
        self.assertEqual(self.client.validation.groupRounds.endpoint, '/v1/grouprounds')
        self.assertEqual(self.client.validation.knockoutRounds.endpoint, '/v1/knockoutrounds')
        self.assertEqual(self.client.validation.confederations.endpoint, '/v1/confederations')
        self.assertEqual(self.client.validation.countries.endpoint, '/v1/countries')
        self.assertEqual(self.client.validation.competitions.endpoint, '/v1/competitions')
        self.assertEqual(self.client.validation.domesticCompetitions.endpoint, '/v1/domestic_competitions')
        self.assertEqual(self.client.validation.intlCompetitions.endpoint, '/v1/intl_competitions')
        self.assertEqual(self.client.validation.seasons.endpoint, '/v1/seasons')
        self.assertEqual(self.client.validation.teams.endpoint, '/v1/teams')
        self.assertEqual(self.client.validation.venues.endpoint, '/v1/venues')
        self.assertEqual(self.client.validation.timezones.endpoint, '/v1/timezones')
        self.assertEqual(self.client.validation.nameOrder.endpoint, '/v1/name_order')
        self.assertEqual(self.client.validation.persons.endpoint, '/v1/persons')
        self.assertEqual(self.client.validation.positions.endpoint, '/v1/positions')
        self.assertEqual(self.client.validation.fouls.endpoint, '/v1/fouls')
        self.assertEqual(self.client.validation.cards.endpoint, '/v1/cards')
        self.assertEqual(self.client.validation.bodyparts.endpoint, '/v1/bodyparts')
        self.assertEqual(self.client.validation.shotevents.endpoint, '/v1/shotevents')
        self.assertEqual(self.client.validation.penaltyOutcomes.endpoint, '/v1/penalty_outcomes')
        self.assertEqual(self.client.validation.actions.endpoint, '/v1/actions')
        self.assertEqual(self.client.validation.modifiers.endpoint, '/v1/modifiers')
        self.assertEqual(self.client.validation.modifierCategories.endpoint, '/v1/modifier_categories')
        self.assertEqual(self.client.validation.weather.endpoint, '/v1/weather')
        self.assertEqual(self.client.validation.surfaces.endpoint, '/v1/surfaces')

    def test_personnel_endpoints(self):
        """Verify personnel resource endpoints without ID."""
        self.assertEqual(self.client.players.endpoint, '/v1/personnel/players')
        self.assertEqual(self.client.managers.endpoint, '/v1/personnel/managers')
        self.assertEqual(self.client.referees.endpoint, '/v1/personnel/referees')

    def test_club_match_endpoints(self):
        """Verify club match resource endpoints without match ID."""
        self.assertEqual(self.client.club.information.EndpointURI(), '/v1/clubs/matches/info')
        self.assertEqual(self.client.club.lineups.EndpointURI(), '/v1/clubs/matches/lineups')
        self.assertEqual(self.client.club.conditions.EndpointURI(), '/v1/clubs/matches/conditions')
        self.assertEqual(self.client.club.goals.EndpointURI(), '/v1/clubs/matches/goals')
        self.assertEqual(self.client.club.penalties.EndpointURI(), '/v1/clubs/matches/penalties')
        self.assertEqual(self.client.club.offenses.EndpointURI(), '/v1/clubs/matches/offenses')
        self.assertEqual(self.client.club.substitutions.EndpointURI(), '/v1/clubs/matches/substitutions')
        self.assertEqual(self.client.club.shootouts.EndpointURI(), '/v1/clubs/matches/shootouts')

    def test_national_team_match_endpoints(self):
        """Verify national team match resource endpoints without match ID."""
        self.assertEqual(self.client.natl.information.EndpointURI(), '/v1/national/matches/info')
        self.assertEqual(self.client.natl.lineups.EndpointURI(), '/v1/national/matches/lineups')
        self.assertEqual(self.client.natl.conditions.EndpointURI(), '/v1/national/matches/conditions')
        self.assertEqual(self.client.natl.goals.EndpointURI(), '/v1/national/matches/goals')
        self.assertEqual(self.client.natl.penalties.EndpointURI(), '/v1/national/matches/penalties')
        self.assertEqual(self.client.natl.offenses.EndpointURI(), '/v1/national/matches/offenses')
        self.assertEqual(self.client.natl.substitutions.EndpointURI(), '/v1/national/matches/substitutions')
        self.assertEqual(self.client.natl.shootouts.EndpointURI(), '/v1/national/matches/shootouts')

    def test_analytics_endpoints(self):
        """Verify analytics endpoints without match ID."""
        self.assertEqual(self.client.analytics.state.EndpointURI(), '/v1/analytics/match/state')
        self.assertEqual(self.client.analytics.segment.EndpointURI(), '/v1/analytics/match/segment')
        self.assertEqual(self.client.analytics.tsr.EndpointURI(), '/v1/analytics/match/tsr')

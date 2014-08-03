import unittest
import mock

from soccermetrics.rest import SoccermetricsRestClient

@mock.patch('soccermetrics.rest.resources.base.EasyDict')
@mock.patch('soccermetrics.rest.resources.base.Response')
@mock.patch('soccermetrics.rest.resources.base.requests')
class ClientCanonicalEndpointTest(unittest.TestCase):
    """
    Test canonical endpoints of API resources in client.
    """

    def setUp(self):
        self.client = SoccermetricsRestClient(base_uri="https://foo.uri", account="ID", api_key="KEY")

    def create_patch(self, name):
        patcher = mock.patch(name)
        thing = patcher.start()
        self.addCleanup(patcher.stop)
        return thing

    def test_validation_endpoints_integer_id_get(self, mock_resp, resp_obj, mock_dict):
        """Verify URI of Validation resources with integer UIDs passed to GET."""
        mock_resp.get.return_value.status_code = 200

        value = self.client.validation.phases.get(2)
        mock_resp.get.assert_called_with('https://foo.uri/v1/phases/2',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.groupRounds.get(20)
        mock_resp.get.assert_called_with('https://foo.uri/v1/grouprounds/20',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.knockoutRounds.get(20)
        mock_resp.get.assert_called_with('https://foo.uri/v1/knockoutrounds/20',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.confederations.get(10)
        mock_resp.get.assert_called_with('https://foo.uri/v1/confederations/10',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.seasons.get(200)
        mock_resp.get.assert_called_with('https://foo.uri/v1/seasons/200',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.timezones.get(20)
        mock_resp.get.assert_called_with('https://foo.uri/v1/timezones/20',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.nameOrder.get(2)
        mock_resp.get.assert_called_with('https://foo.uri/v1/name_order/2',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.positions.get(20)
        mock_resp.get.assert_called_with('https://foo.uri/v1/positions/20',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.fouls.get(20)
        mock_resp.get.assert_called_with('https://foo.uri/v1/fouls/20',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.cards.get(2)
        mock_resp.get.assert_called_with('https://foo.uri/v1/cards/2',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.bodyparts.get(2)
        mock_resp.get.assert_called_with('https://foo.uri/v1/bodyparts/2',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.shotevents.get(20)
        mock_resp.get.assert_called_with('https://foo.uri/v1/shotevents/20',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.penaltyOutcomes.get(2)
        mock_resp.get.assert_called_with('https://foo.uri/v1/penalty_outcomes/2',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.actions.get(200)
        mock_resp.get.assert_called_with('https://foo.uri/v1/actions/200',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.modifiers.get(200)
        mock_resp.get.assert_called_with('https://foo.uri/v1/modifiers/200',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.modifierCategories.get(20)
        mock_resp.get.assert_called_with('https://foo.uri/v1/modifier_categories/20',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.weather.get(20)
        mock_resp.get.assert_called_with('https://foo.uri/v1/weather/20',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.surfaces.get(20)
        mock_resp.get.assert_called_with('https://foo.uri/v1/surfaces/20',
            params={'app_id': 'ID', 'app_key': 'KEY'})

    def test_validation_endpoints_uuid_get(self, mock_resp, resp_obj, mock_dict):
        """Verify URI of Validation resources with UUIDs passed to GET."""
        mock_resp.get.return_value.status_code = 200

        uid = "420aa27ce815499c85ec0301aff61ec4"

        value = self.client.validation.countries.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/countries/420aa27ce815499c85ec0301aff61ec4',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.competitions.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/competitions/420aa27ce815499c85ec0301aff61ec4',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.domesticCompetitions.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/domestic_competitions/420aa27ce815499c85ec0301aff61ec4',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.intlCompetitions.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/intl_competitions/420aa27ce815499c85ec0301aff61ec4',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.teams.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/teams/420aa27ce815499c85ec0301aff61ec4',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.venues.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/venues/420aa27ce815499c85ec0301aff61ec4',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.validation.persons.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/persons/420aa27ce815499c85ec0301aff61ec4',
            params={'app_id': 'ID', 'app_key': 'KEY'})

    def test_personnel_endpoints_canonical_get(self, mock_resp, resp_obj, mock_dict):
        """Verify personnel resource endpoints with ID passed to GET."""

        mock_resp.get.return_value.status_code = 200

        uid = "807f2a61bcea4a1bb98d66fface88b44"

        value = self.client.players.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/personnel/players/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.managers.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/personnel/managers/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.referees.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/personnel/referees/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

    def test_club_match_endpoints_canonical_get(self, mock_resp, resp_obj, mock_dict):
        """Verify club match resource endpoints with ID passed to GET."""

        mock_resp.get.return_value.status_code = 200

        match = "420aa27ce815499c85ec0301aff61ec4"
        uid = "807f2a61bcea4a1bb98d66fface88b44"

        value = self.client.club.information.get(match)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/matches/420aa27ce815499c85ec0301aff61ec4/info',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.club.conditions.get(match)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/matches/420aa27ce815499c85ec0301aff61ec4/conditions',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.club.lineups.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/matches/420aa27ce815499c85ec0301aff61ec4/lineups/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.club.goals.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/matches/420aa27ce815499c85ec0301aff61ec4/goals/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.club.penalties.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/matches/420aa27ce815499c85ec0301aff61ec4/penalties/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.club.offenses.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/matches/420aa27ce815499c85ec0301aff61ec4/offenses/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.club.substitutions.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/matches/420aa27ce815499c85ec0301aff61ec4/substitutions/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.club.shootouts.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/matches/420aa27ce815499c85ec0301aff61ec4/shootouts/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

    def test_natl_match_endpoints_canonical_get(self, mock_resp, resp_obj, mock_dict):
        """Verify national team match resource endpoints with ID passed to GET."""

        mock_resp.get.return_value.status_code = 200

        match = "420aa27ce815499c85ec0301aff61ec4"
        uid = "807f2a61bcea4a1bb98d66fface88b44"

        value = self.client.natl.information.get(match)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/matches/420aa27ce815499c85ec0301aff61ec4/info',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.conditions.get(match)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/matches/420aa27ce815499c85ec0301aff61ec4/conditions',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.lineups.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/matches/420aa27ce815499c85ec0301aff61ec4/lineups/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.goals.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/matches/420aa27ce815499c85ec0301aff61ec4/goals/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.penalties.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/matches/420aa27ce815499c85ec0301aff61ec4/penalties/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.offenses.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/matches/420aa27ce815499c85ec0301aff61ec4/offenses/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.substitutions.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/matches/420aa27ce815499c85ec0301aff61ec4/substitutions/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.shootouts.get(match, uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/matches/420aa27ce815499c85ec0301aff61ec4/shootouts/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

    def test_club_events_endpoints_canonical_get(self, mock_resp, resp_obj, mock_dict):
        """Verify club match micro-event resource endpoints with ID passed to GET."""

        mock_resp.get.return_value.status_code = 200

        uid = "807f2a61bcea4a1bb98d66fface88b44"

        value = self.client.club.events.all.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/events/all/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.club.events.touches.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/events/touches/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.club.events.actions.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/events/actions/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

    def test_natl_events_endpoints_canonical_get(self, mock_resp, resp_obj, mock_dict):
        """Verify national team match micro-event resource endpoints with ID passed to GET."""

        mock_resp.get.return_value.status_code = 200

        uid = "807f2a61bcea4a1bb98d66fface88b44"

        value = self.client.natl.events.all.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/events/all/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.events.touches.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/events/touches/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.events.actions.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/events/actions/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

    def test_club_stats_endpoints_canonical_get(self, mock_resp, resp_obj, mock_dict):
        """Verify club match statistical resource endpoints with ID passed to GET."""

        mock_resp.get.return_value.status_code = 200

        uid = "807f2a61bcea4a1bb98d66fface88b44"

        value = self.client.club.stats.crosses.corners.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/clubs/stats/crosses/corners/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

    def test_natl_stats_endpoints_canonical_get(self, mock_resp, resp_obj, mock_dict):
        """Verify national team match statistical resource endpoints with ID passed to GET."""

        mock_resp.get.return_value.status_code = 200

        uid = "807f2a61bcea4a1bb98d66fface88b44"

        value = self.client.natl.stats.crosses.corners.get(uid)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/national/stats/crosses/corners/807f2a61bcea4a1bb98d66fface88b44',
            params={'app_id': 'ID', 'app_key': 'KEY'})

    def test_analytics_endpoints_canonical_get(self, mock_resp, resp_obj, mock_dict):
        """Verify match analytics resource endpoints with ID passed to GET."""

        mock_resp.get.return_value.status_code = 200

        match = "420aa27ce815499c85ec0301aff61ec4"

        value = self.client.analytics.state.get(match)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/analytics/match/420aa27ce815499c85ec0301aff61ec4/state',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.analytics.segment.get(match)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/analytics/match/420aa27ce815499c85ec0301aff61ec4/segment',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.analytics.tsr.get(match)
        mock_resp.get.assert_called_with(
            'https://foo.uri/v1/analytics/match/420aa27ce815499c85ec0301aff61ec4/tsr',
            params={'app_id': 'ID', 'app_key': 'KEY'})

    def test_validation_endpoints_head(self, mock_resp, resp_obj, mock_dict):
        """Verify URI of Validation resource HEAD request."""
        mock_resp.head.return_value.status_code = 200

        value = self.client.validation.phases.head()
        mock_resp.head.assert_called_with('https://foo.uri/v1/phases',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        mock_resp.reset_mock()
        self.assertRaises(TypeError, self.client.validation.phases.head, 5)

    def test_validation_endpoints_options(self, mock_resp, resp_obj, mock_dict):
        """Verify URI of Validation resource OPTIONS request."""
        mock_resp.options.return_value.status_code = 200

        value = self.client.validation.phases.options()
        mock_resp.options.assert_called_with('https://foo.uri/v1/phases',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        mock_resp.reset_mock()
        self.assertRaises(TypeError, self.client.validation.phases.head, 5)

    def test_personnel_endpoints_head(self, mock_resp, resp_obj, mock_dict):
        """Verify URI of Personnel resource HEAD request."""
        mock_resp.head.return_value.status_code = 200

        value = self.client.players.head()
        mock_resp.head.assert_called_with('https://foo.uri/v1/personnel/players',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        mock_resp.reset_mock()
        self.assertRaises(TypeError, self.client.players.head, "807f2a61bcea4a1bb98d66fface88b44")

    def test_personnel_endpoints_options(self, mock_resp, resp_obj, mock_dict):
        """Verify URI of Personnel resource OPTIONS request."""
        mock_resp.options.return_value.status_code = 200

        value = self.client.managers.options()
        mock_resp.options.assert_called_with('https://foo.uri/v1/personnel/managers',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        mock_resp.reset_mock()
        self.assertRaises(TypeError, self.client.managers.head, "807f2a61bcea4a1bb98d66fface88b44")

    def test_match_endpoints_head(self, mock_resp, resp_obj, mock_dict):
        """Verify URI of Match resource HEAD request."""
        mock_resp.head.return_value.status_code = 200

        value = self.client.club.information.head()
        mock_resp.head.assert_called_with('https://foo.uri/v1/clubs/matches/info',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.information.head()
        mock_resp.head.assert_called_with('https://foo.uri/v1/national/matches/info',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        mock_resp.reset_mock()
        self.assertRaises(TypeError, self.client.club.information.head, "807f2a61bcea4a1bb98d66fface88b44")
        self.assertRaises(TypeError, self.client.natl.information.head, "807f2a61bcea4a1bb98d66fface88b44")

    def test_match_endpoints_options(self, mock_resp, resp_obj, mock_dict):
        """Verify URI of Match resource OPTIONS request."""
        mock_resp.options.return_value.status_code = 200

        value = self.client.club.goals.options()
        mock_resp.options.assert_called_with('https://foo.uri/v1/clubs/matches/goals',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        value = self.client.natl.goals.options()
        mock_resp.options.assert_called_with('https://foo.uri/v1/national/matches/goals',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        mock_resp.reset_mock()
        self.assertRaises(TypeError, self.client.club.goals.options, "807f2a61bcea4a1bb98d66fface88b44")
        self.assertRaises(TypeError, self.client.natl.goals.options, "807f2a61bcea4a1bb98d66fface88b44")

    def test_analytics_endpoints_head(self, mock_resp, resp_obj, mock_dict):
        """Verify URI of Match Analytics resource HEAD request."""
        mock_resp.head.return_value.status_code = 200

        value = self.client.analytics.state.head()
        mock_resp.head.assert_called_with('https://foo.uri/v1/analytics/match/state',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        mock_resp.reset_mock()
        self.assertRaises(TypeError, self.client.analytics.state.head, "807f2a61bcea4a1bb98d66fface88b44")

    def test_analytics_endpoints_options(self, mock_resp, resp_obj, mock_dict):
        """Verify URI of Match Analytics resource OPTIONS request."""
        mock_resp.options.return_value.status_code = 200

        value = self.client.analytics.segment.options()
        mock_resp.options.assert_called_with('https://foo.uri/v1/analytics/match/segment',
            params={'app_id': 'ID', 'app_key': 'KEY'})

        mock_resp.reset_mock()
        self.assertRaises(TypeError, self.client.analytics.segment.options, "807f2a61bcea4a1bb98d66fface88b44")


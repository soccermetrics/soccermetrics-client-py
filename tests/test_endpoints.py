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

    def test_club_events_endpoints(self):
        """Verify club match micro-event endpoints without match or record IDs."""
        self.assertEqual(self.client.club.events.all.endpoint, '/v1/clubs/events/all')
        self.assertEqual(self.client.club.events.touches.endpoint, '/v1/clubs/events/touches')
        self.assertEqual(self.client.club.events.actions.endpoint, '/v1/clubs/events/actions')

    def test_natl_events_endpoints(self):
        """Verify national team match micro-event endpoints without match or record IDs."""
        self.assertEqual(self.client.natl.events.all.endpoint, '/v1/national/events/all')
        self.assertEqual(self.client.natl.events.touches.endpoint, '/v1/national/events/touches')
        self.assertEqual(self.client.natl.events.actions.endpoint, '/v1/national/events/actions')

    def test_club_statistics_endpoints(self):
        """Verify club match statistics endpoints without match or record IDs."""
        self.assertEqual(self.client.club.stats.crosses.corners.endpoint, '/v1/clubs/stats/crosses/corners')
        self.assertEqual(self.client.club.stats.crosses.totals.endpoint, '/v1/clubs/stats/crosses/totals')

        self.assertEqual(self.client.club.stats.defense.actions.endpoint, '/v1/clubs/stats/defense/actions')
        self.assertEqual(self.client.club.stats.defense.blocks.endpoint, '/v1/clubs/stats/defense/blocks')
        self.assertEqual(self.client.club.stats.defense.clearances.endpoint, '/v1/clubs/stats/defense/clearances')
        self.assertEqual(self.client.club.stats.defense.goalline.endpoint, '/v1/clubs/stats/defense/goalline')
        self.assertEqual(self.client.club.stats.defense.tackles.endpoint, '/v1/clubs/stats/defense/tackles')

        self.assertEqual(self.client.club.stats.fouls.cards.endpoint, '/v1/clubs/stats/fouls/cards')
        self.assertEqual(self.client.club.stats.fouls.wins.endpoint, '/v1/clubs/stats/fouls/wins')

        self.assertEqual(self.client.club.stats.goals.assists.endpoint, '/v1/clubs/stats/goals/assists')
        self.assertEqual(self.client.club.stats.goals.bodyparts.endpoint, '/v1/clubs/stats/goals/bodyparts')
        self.assertEqual(self.client.club.stats.goals.locations.endpoint, '/v1/clubs/stats/goals/locations')
        self.assertEqual(self.client.club.stats.goals.penalties.endpoint, '/v1/clubs/stats/goals/penalties')
        self.assertEqual(self.client.club.stats.goals.totals.endpoint, '/v1/clubs/stats/goals/totals')

        self.assertEqual(self.client.club.stats.goalkeeper.actions.endpoint, '/v1/clubs/stats/goalkeeper/actions')
        self.assertEqual(self.client.club.stats.goalkeeper.goals.endpoint, '/v1/clubs/stats/goalkeeper/goals')
        self.assertEqual(self.client.club.stats.goalkeeper.shots.endpoint, '/v1/clubs/stats/goalkeeper/shots')
        self.assertEqual(self.client.club.stats.goalkeeper.saves.endpoint, '/v1/clubs/stats/goalkeeper/saves')

        self.assertEqual(self.client.club.stats.passes.directions.endpoint, '/v1/clubs/stats/passes/directions')
        self.assertEqual(self.client.club.stats.passes.lengths.endpoint, '/v1/clubs/stats/passes/lengths')
        self.assertEqual(self.client.club.stats.passes.locations.endpoint, '/v1/clubs/stats/passes/locations')
        self.assertEqual(self.client.club.stats.passes.totals.endpoint, '/v1/clubs/stats/passes/totals')

        self.assertEqual(self.client.club.stats.setpieces.corners.endpoint, '/v1/clubs/stats/setpieces/corners')
        self.assertEqual(self.client.club.stats.setpieces.freekicks.endpoint, '/v1/clubs/stats/setpieces/freekicks')
        self.assertEqual(self.client.club.stats.setpieces.throwins.endpoint, '/v1/clubs/stats/setpieces/throwins')

        self.assertEqual(self.client.club.stats.shots.bodyparts.endpoint, '/v1/clubs/stats/shots/bodyparts')
        self.assertEqual(self.client.club.stats.shots.locations.endpoint, '/v1/clubs/stats/shots/locations')
        self.assertEqual(self.client.club.stats.shots.plays.endpoint, '/v1/clubs/stats/shots/plays')
        self.assertEqual(self.client.club.stats.shots.totals.endpoint, '/v1/clubs/stats/shots/totals')

        self.assertEqual(self.client.club.stats.touches.duels.endpoint, '/v1/clubs/stats/touches/duels')
        self.assertEqual(self.client.club.stats.touches.locations.endpoint, '/v1/clubs/stats/touches/locations')
        self.assertEqual(self.client.club.stats.touches.totals.endpoint, '/v1/clubs/stats/touches/totals')

    def test_natl_statistics_endpoints(self):
        """Verify national team match statistics endpoints without match or record IDs."""
        self.assertEqual(self.client.natl.stats.crosses.corners.endpoint, '/v1/national/stats/crosses/corners')
        self.assertEqual(self.client.natl.stats.crosses.totals.endpoint, '/v1/national/stats/crosses/totals')

        self.assertEqual(self.client.natl.stats.defense.actions.endpoint, '/v1/national/stats/defense/actions')
        self.assertEqual(self.client.natl.stats.defense.blocks.endpoint, '/v1/national/stats/defense/blocks')
        self.assertEqual(self.client.natl.stats.defense.clearances.endpoint, '/v1/national/stats/defense/clearances')
        self.assertEqual(self.client.natl.stats.defense.goalline.endpoint, '/v1/national/stats/defense/goalline')
        self.assertEqual(self.client.natl.stats.defense.tackles.endpoint, '/v1/national/stats/defense/tackles')

        self.assertEqual(self.client.natl.stats.fouls.cards.endpoint, '/v1/national/stats/fouls/cards')
        self.assertEqual(self.client.natl.stats.fouls.wins.endpoint, '/v1/national/stats/fouls/wins')

        self.assertEqual(self.client.natl.stats.goals.assists.endpoint, '/v1/national/stats/goals/assists')
        self.assertEqual(self.client.natl.stats.goals.bodyparts.endpoint, '/v1/national/stats/goals/bodyparts')
        self.assertEqual(self.client.natl.stats.goals.locations.endpoint, '/v1/national/stats/goals/locations')
        self.assertEqual(self.client.natl.stats.goals.penalties.endpoint, '/v1/national/stats/goals/penalties')
        self.assertEqual(self.client.natl.stats.goals.totals.endpoint, '/v1/national/stats/goals/totals')

        self.assertEqual(self.client.natl.stats.goalkeeper.actions.endpoint, '/v1/national/stats/goalkeeper/actions')
        self.assertEqual(self.client.natl.stats.goalkeeper.goals.endpoint, '/v1/national/stats/goalkeeper/goals')
        self.assertEqual(self.client.natl.stats.goalkeeper.shots.endpoint, '/v1/national/stats/goalkeeper/shots')
        self.assertEqual(self.client.natl.stats.goalkeeper.saves.endpoint, '/v1/national/stats/goalkeeper/saves')

        self.assertEqual(self.client.natl.stats.passes.directions.endpoint, '/v1/national/stats/passes/directions')
        self.assertEqual(self.client.natl.stats.passes.lengths.endpoint, '/v1/national/stats/passes/lengths')
        self.assertEqual(self.client.natl.stats.passes.locations.endpoint, '/v1/national/stats/passes/locations')
        self.assertEqual(self.client.natl.stats.passes.totals.endpoint, '/v1/national/stats/passes/totals')

        self.assertEqual(self.client.natl.stats.setpieces.corners.endpoint, '/v1/national/stats/setpieces/corners')
        self.assertEqual(self.client.natl.stats.setpieces.freekicks.endpoint, '/v1/national/stats/setpieces/freekicks')
        self.assertEqual(self.client.natl.stats.setpieces.throwins.endpoint, '/v1/national/stats/setpieces/throwins')

        self.assertEqual(self.client.natl.stats.shots.bodyparts.endpoint, '/v1/national/stats/shots/bodyparts')
        self.assertEqual(self.client.natl.stats.shots.locations.endpoint, '/v1/national/stats/shots/locations')
        self.assertEqual(self.client.natl.stats.shots.plays.endpoint, '/v1/national/stats/shots/plays')
        self.assertEqual(self.client.natl.stats.shots.totals.endpoint, '/v1/national/stats/shots/totals')

        self.assertEqual(self.client.natl.stats.touches.duels.endpoint, '/v1/national/stats/touches/duels')
        self.assertEqual(self.client.natl.stats.touches.locations.endpoint, '/v1/national/stats/touches/locations')
        self.assertEqual(self.client.natl.stats.touches.totals.endpoint, '/v1/national/stats/touches/totals')

    def test_analytics_endpoints(self):
        """Verify analytics endpoints without match ID."""
        self.assertEqual(self.client.analytics.state.EndpointURI(), '/v1/analytics/match/state')
        self.assertEqual(self.client.analytics.segment.EndpointURI(), '/v1/analytics/match/segment')
        self.assertEqual(self.client.analytics.tsr.EndpointURI(), '/v1/analytics/match/tsr')

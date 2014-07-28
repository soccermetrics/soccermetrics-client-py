from soccermetrics.rest.resources import Resource

class ValidationResource(Resource):
    """
    Establish access to Validation resources (/ endpoint).

    Derived from :class:`base.Resource`.
    """

    def __init__(self, resource, base_uri, auth):
        """
        Constructor of ValidationResource class.

        :param resource: Name of resource.
        :type resource: string
        :param base_uri: Base URI of API.
        :type base_uri: string
        :param auth: Authentication credential.
        :type auth: tuple
        """
        super(ValidationResource, self).__init__(base_uri,auth)

        self.endpoint += "/%s" % resource

class Validation(object):
    """Access to Validation objects.

    +----------------------+----------------------------+
    | Attribute            | Description                |
    +======================+============================+
    | phases               | Competition Phases         |
    +----------------------+----------------------------+
    | groupRounds          | Group Rounds               |
    +----------------------+----------------------------+
    | knockoutRounds       | Knockout Rounds            |
    +----------------------+----------------------------+
    | confederations       | Confederations             |
    +----------------------+----------------------------+
    | countries            | Countries                  |
    +----------------------+----------------------------+
    | competitions         | Competitions               |
    +----------------------+----------------------------+
    | domesticCompetitions | Domestic Competitions      |
    +----------------------+----------------------------+
    | intlCompetitions     | International Competitions |
    +----------------------+----------------------------+
    | seasons              | Seasons                    |
    +----------------------+----------------------------+
    | teams                | Teams                      |
    +----------------------+----------------------------+
    | venues               | Match Venues               |
    +----------------------+----------------------------+
    | timezones            | Time Zones                 |
    +----------------------+----------------------------+
    | nameOrder            | Name Order                 |
    +----------------------+----------------------------+
    | persons              | Persons                    |
    +----------------------+----------------------------+
    | positions            | Positions                  |
    +----------------------+----------------------------+
    | fouls                | Fouls                      |
    +----------------------+----------------------------+
    | cards                | Cards                      |
    +----------------------+----------------------------+
    | bodyparts            | Body parts                 |
    +----------------------+----------------------------+
    | shotevents           | Shot events                |
    +----------------------+----------------------------+
    | penaltyOutcomes      | Penalty Outcomes           |
    +----------------------+----------------------------+
    | actions              | Event Actions              |
    +----------------------+----------------------------+
    | modifiers            | Action Modifiers           |
    +----------------------+----------------------------+
    | modifierCategories   | Action Modifier Categories |
    +----------------------+----------------------------+
    | weather              | Weather Conditions         |
    +----------------------+----------------------------+
    | surfaces             | Surfaces                   |
    +----------------------+----------------------------+
    """

    def __init__(self, base_uri, auth):
        self.phases = ValidationResource("phases", base_uri, auth)
        self.groupRounds = ValidationResource("grouprounds", base_uri, auth)
        self.knockoutRounds = ValidationResource("knockoutrounds", base_uri, auth)
        self.confederations = ValidationResource("confederations", base_uri, auth)
        self.countries = ValidationResource("countries", base_uri, auth)
        self.competitions = ValidationResource("competitions", base_uri, auth)
        self.domesticCompetitions = ValidationResource("domestic_competitions", base_uri, auth)
        self.intlCompetitions = ValidationResource("intl_competitions", base_uri, auth)
        self.seasons = ValidationResource("seasons", base_uri, auth)
        self.teams = ValidationResource("teams", base_uri, auth)
        self.venues = ValidationResource("venues", base_uri, auth)
        self.timezones = ValidationResource("timezones", base_uri, auth)
        self.nameOrder = ValidationResource("name_order", base_uri, auth)
        self.persons = ValidationResource("persons", base_uri, auth)
        self.positions = ValidationResource("positions", base_uri, auth)
        self.fouls = ValidationResource("fouls", base_uri, auth)
        self.cards = ValidationResource("cards", base_uri, auth)
        self.bodyparts = ValidationResource("bodyparts", base_uri, auth)
        self.shotevents = ValidationResource("shotevents", base_uri, auth)
        self.penaltyOutcomes = ValidationResource("penalty_outcomes", base_uri, auth)
        self.actions = ValidationResource("actions", base_uri, auth)
        self.modifiers = ValidationResource("modifiers", base_uri, auth)
        self.modifierCategories = ValidationResource("modifier_categories", base_uri, auth)
        self.weather = ValidationResource("weather", base_uri, auth)
        self.surfaces = ValidationResource("surfaces", base_uri, auth)

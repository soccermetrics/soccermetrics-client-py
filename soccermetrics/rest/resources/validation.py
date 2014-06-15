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

    +------------------+----------------------------+
    | Attribute        | Description                |
    +==================+============================+
    | phases           | Competition phases         |
    +------------------+----------------------------+
    | groupRounds      | Group Rounds               |
    +------------------+----------------------------+
    | knockoutRounds   | Knockout Rounds            |
    +------------------+----------------------------+
    | confederations   | Confederations             |
    +------------------+----------------------------+
    | countries        | Countries                  |
    +------------------+----------------------------+
    | seasons          | Seasons                    |
    +------------------+----------------------------+
    | teams            | Teams                      |
    +------------------+----------------------------+
    | venues           | Venues                     |
    +------------------+----------------------------+
    | timezones        | Time zones                 |
    +------------------+----------------------------+
    | persons          | Persons                    |
    +------------------+----------------------------+
    | positions        | Positions                  |
    +------------------+----------------------------+
    | fouls            | Fouls                      |
    +------------------+----------------------------+
    | cards            | Cards                      |
    +------------------+----------------------------+
    | bodyparts        | Body parts                 |
    +------------------+----------------------------+
    | shotevents       | Shot events                |
    +------------------+----------------------------+
    | penaltyOutcomes  | Penalty outcomes           |
    +------------------+----------------------------+
    | weather          | Weather conditions         |
    +------------------+----------------------------+
    | surfaces         | Surfaces                   |
    +------------------+----------------------------+
    """

    def __init__(self, base_uri, auth):
        self.phases = ValidationResource("phases", base_uri, auth)
        self.groupRounds = ValidationResource("grouprounds", base_uri, auth)
        self.knockoutRounds = ValidationResource("knockoutrounds", base_uri, auth)
        self.confederations = ValidationResource("confederations", base_uri, auth)
        self.countries = ValidationResource("countries", base_uri, auth)
        self.seasons = ValidationResource("seasons", base_uri, auth)
        self.teams = ValidationResource("teams", base_uri, auth)
        self.venues = ValidationResource("venues", base_uri, auth)
        self.timezones = ValidationResource("timezones", base_uri, auth)
        self.persons = ValidationResource("persons", base_uri, auth)
        self.positions = ValidationResource("positions", base_uri, auth)
        self.fouls = ValidationResource("fouls", base_uri, auth)
        self.cards = ValidationResource("cards", base_uri, auth)
        self.bodyparts = ValidationResource("bodyparts", base_uri, auth)
        self.shotevents = ValidationResource("shotevents", base_uri, auth)
        self.penaltyOutcomes = ValidationResource("penalty_outcomes", base_uri, auth)
        self.weather = ValidationResource("weather", base_uri, auth)
        self.surfaces = ValidationResource("surfaces", base_uri, auth)

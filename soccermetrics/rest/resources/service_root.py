from soccermetrics.rest.resources import Resource

class Root(Resource):
    """Service root endpoint."""

    def __init__(self, base_uri, auth):
        super(Root, self).__init__(base_uri, auth)

        self.endpoint += '/'
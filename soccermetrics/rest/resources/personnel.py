from soccermetrics.rest.resources import Resource

class Personnel(Resource):
    """
    Represents a Personnel REST resource.
    """
    def __init__(self, resource, base_uri, auth):
        super(Personnel, self).__init__(base_uri,auth)

        self.endpoint += "/personnel/%s" % resource
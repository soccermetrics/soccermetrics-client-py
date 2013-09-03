from apiclient.rest.resources import Resource

class Validation(Resource):
    """Validation resources."""

    def __init__(self, resource, base_uri, auth):
        super(Validation, self).__init__(base_uri,auth)

        self.endpoint += "/%s" % resource
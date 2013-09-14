import unittest

from soccermetrics import SoccermetricsRestException

class RestExceptionFormatTest(unittest.TestCase):

    def setUp(self):
        self.exc = SoccermetricsRestException(404,"/path/to/resource")

    def test_exception_status(self):
        self.assertEqual(self.exc.status, 404)

    def test_exception_uri(self):
        self.assertEqual(self.exc.uri, "/path/to/resource")

    def test_exception_msg(self):
        self.assertEqual(self.exc.msg, "")

    def test_exception_string(self):
        self.assertEqual(str(self.exc), "HTTP ERROR 404:  \n /path/to/resource")

    def test_exception_with_msg(self):
        local = SoccermetricsRestException(404,"/path/to/resource",msg="Invalid resource request.")

        self.assertEqual(str(local), "HTTP ERROR 404: Invalid resource request. \n /path/to/resource")

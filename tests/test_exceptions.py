import unittest

from soccermetrics import SoccermetricsRestException

class RestExceptionFormatTest(unittest.TestCase):
    """
    Test format of client exception messages.
    """

    def setUp(self):
        self.exc = SoccermetricsRestException(404,"/path/to/resource")

    def test_exception_status(self):
        """Verify status code of exception is an integer."""
        self.assertEqual(self.exc.status, 404)

    def test_exception_uri(self):
        """Verify that URI in exception is URI sent through client."""
        self.assertEqual(self.exc.uri, "/path/to/resource")

    def test_exception_msg(self):
        """Verify that exception message is empty."""
        self.assertEqual(self.exc.msg, "")

    def test_exception_string(self):
        """Verify construction of string expression of exception."""
        self.assertEqual(str(self.exc), "HTTP ERROR 404:  \n /path/to/resource")

    def test_exception_with_msg(self):
        """Verify construction of string expression of exception with message."""
        local = SoccermetricsRestException(404,"/path/to/resource",msg="Invalid resource request.")

        self.assertEqual(str(local), "HTTP ERROR 404: Invalid resource request. \n /path/to/resource")

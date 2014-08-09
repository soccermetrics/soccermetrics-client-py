__version_info__ = ('0','8','0')
__version__ = '.'.join(__version_info__)

__api_version__ = 'v1'

class SoccermetricsException(Exception):
    """Base class for exceptions in Soccermetrics applications.

    Derived from :class:`Exception`.
    """
    pass

class SoccermetricsRestException(SoccermetricsException):
    """Custom exception for Soccermetrics REST API errors.

    The exception is raised with the following message::

        **HTTP ERROR** <error code>: <error message>
        <URI>

    """

    def __init__(self,status,uri,msg=""):
        """Constructor of SoccermetricsRestException.

        :param status: HTTP status code
        :type status: int
        :param uri: URI sent when exception was raised
        :type uri: string
        :param msg: Detailed error message
        :type msg: string or ""
        """
        self.uri = uri
        self.status = status
        self.msg = msg

    def __str__(self):
        """String representation of exception."""
        return "HTTP ERROR %s: %s \n %s" % (self.status, self.msg, self.uri)
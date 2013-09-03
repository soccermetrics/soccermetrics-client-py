__version_info__ = ('0','5','0')
__version__ = '.'.join(__version_info__)

__api_version__ = 'v0'

class SoccermetricsException(Exception):
    pass

class SoccermetricsRestException(SoccermetricsException):

    def __init__(self,status,uri,msg=""):
        self.uri = uri
        self.status = status
        self.msg = msg

    def __str__(self):
        return "HTTP ERROR %s: %s \n %s" % (self.status, self.msg, self.uri)
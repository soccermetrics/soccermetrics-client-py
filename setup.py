import sys
from soccermetrics import __version__
from setuptools import setup, find_packages

# To install the soccermetrics-client-py library, open a Terminal shell,
# then run this file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools
REQUIRES = ["requests >= 1.2.3", "easydict >= 1.4"]

if sys.version_info >= (3,0):
    REQUIRES.append('unittest2py3k')
else:
    REQUIRES.append('unittest2')

setup(
    name = "soccermetrics",
    version = __version__,
    description = "Soccermetrics API Client",
    author = "Soccermetrics Research",
    author_email = "api-support@soccermetrics.net",
    url = "http://github.com/soccermetrics/soccermetrics-client-py",
    keywords = ["soccer", "football", "soccermetrics", "soccer analytics", "API client"],
    install_requires = REQUIRES,
    packages = find_packages(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
    Soccermerics API Python Client Library
    --------------------------------------

    DESCRIPTION
    The Soccermetrics API Client simplifies the process of makes calls to the
    Soccermetrics REST APIs.

    The Soccermetrics REST API are sports modeling and analytics layers on top
    of in-match soccer (football) data sources at varying levels of complexity.
    See http://www.github.com/soccermetrics/soccermetrics-client-py for more
    information.

    LICENSE The Soccermetrics API Python Client Library is distributed under
    the MIT License.""" )

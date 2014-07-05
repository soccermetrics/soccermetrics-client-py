Soccermetrics API Python Client
===============================

This is a Python module for using the Soccermetrics REST API.

Installation
============

The Soccermetrics API Python client library depends on the
`Requests <http://docs.python-requests.org/en/latest/>`_ and
`easydict <http://pypi.python.org/pypi/easydict/>`_ libraries. You can
install the client library within a virtual environment on your
computer, or install it system-wide.

Python 2.6+ is required. The module *might* work with Python 3, but we
haven't tested it and give no guarantees.

It's not required, but
`autoenv <https://github.com/kennethreitz/autoenv>`_ is very nice to
have.

Virtual Environment Install
---------------------------

We recommend installing ``soccermetrics-client-py`` within a virtual
environment using ``virtualenv``. That way you can run different
versions of Python installations and libraries without dealing with
conflicting dependencies.

Here is a link to `a nice tutorial on
Virtualenv <http://simononsoftware.com/virtualenv-tutorial/>`_.

To install ``virtualenv`` on MacOS or Linux, create a folder and run one
of these two commands as ``sudo``:

::

    $ sudo easy_install virtualenv

or

::

    $ sudo pip install virtualenv

If you are on Windows, `this
link <http://flask.pocoo.org/docs/installation/#windows-easy-install>`_
will show you how to install ``pip`` and ``distribute``, which you will
use to install ``virtualenv``.

Download [the current zipped version of the source code]
(https://github.com/soccermetrics/soccermetrics-client-py/archive/master.zip)
from GitHub, unzip the folder and run:

::

    $ make install

System-Wide Install
-------------------

If you want to install ``soccermetrics-client-py`` system-wide -- not
recommended because of possible library conflicts -- download [the
current zipped version of the source code]
(https://github.com/soccermetrics/soccermetrics-client-py/archive/master.zip)
from GitHub, unzip the folder and run:

::

    $ make install

Getting Started
===============

To start using the Soccermetrics API, create a
``SoccermetricsRestClient``.

API Credentials
---------------

You'll need your Soccermetrics API credentials to use the
``SoccermetricsRestClient``. These get passed to the constructor
directly or via environment variables.

::

    from soccermetrics.rest import SoccermetricsRestClient

    appID = "f53baabb"
    appKey = "demo1234567890demo1234567890"

    client = SoccermetricsRestClient(account=appID,api_key=appKey)

If you call ``SoccermetricsRestClient`` without any parameters, the
constructor will look for ``SOCCERMETRICS_APP_ID`` and
``SOCCERMETRICS_APP_KEY`` variables inside the current environment.

We recommend that you keep your credentials in environment variables.
That way you won't have to worry about accidentally posting your
credentials in a public place.

::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

Get Match Information
---------------------

::

    from soccermetrics.rest import SoccermetricsRestClient

    appID = "f53baabb"
    appKey = "demo1234567890demo1234567890"
    client = SoccermetricsRestClient()

    match = client.club.information.get(home_team_name="Everton",
                                         away_team_name="Liverpool").data[0]
    print match.matchday, match.matchDate, match.kickoffTime

    lineup_data = client.link.get(match.link.lineups, is_starting=True).all()
    for datum in lineup_data:
        print datum.playerName, datum.playerTeamName

Get Player Statistical Data
---------------------------

::

    from soccermetrics.rest import SoccermetricsRestClient

    appID = "f53baabb"
    appKey = "demo1234567890demo1234567890"
    client = SoccermetricsRestClient()

    player = client.players.get(full_name=u'Robin van Persie').data[0]
    # goals at club level
    goals = client.link.get(player.link.club.goals)
    penalties = client.link.get(player.link.club.penalties,outcome_type="Goal")
    # goals at national team level
    natl_team_goals = client.link.get(player.link.natl.goals)
    natl_team_pens = client.link.get(player.link.natl.penalties,outcome_type="Goal")

Get Advanced Analytics
----------------------

::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    match = client.club.information.get(home_team_name='Manchester United', away_team_name='Stoke City').data[0]

    match_state_46 = client.link.get(match.link.analytics.club.state,time_mins=46)
    match_state_75 = client.link.get(match.link.analytics.club.state,time_mins=75)
    match_state_final = client.link.get(match.link.analytics.club.state)
    match_segments = client.link.get(match.link.analytics.club.segment)

Learn More
==========

-  `Link to API
   documentation <http://soccermetrics.github.io/fmrd-summary-api>`_.
-  `Link to full client documentation
   here <http://soccermetrics.github.io/soccermetrics-client-py>`_.


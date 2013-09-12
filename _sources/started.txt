.. _gettingstarted:

Getting Started
===============

To start using the Soccermetrics API, create a ``SoccermetricsRestClient``.

API Credentials
---------------

You'll need your Soccermetrics API credentials to use the ``SoccermetricsRestClient``.
These get passed to the constructor or via environment variables.
::

    from soccermetrics.rest import SoccermetricsRestClient

    appID = "f53baabb"
    appKey = "demo1234567890demo1234567890"

    client = SoccermetricsRestClient(account=appID,api_key=appKey)

.. note::

    Copy the code snippet into a text file and run it as a Python script.  The
    code uses a live API credential for demonstration purposes.

If you call ``SoccermetricsRestClient`` without any parameters, the constructor
will look for ``SOCCERMETRICS_APP_ID`` and ``SOCCERMETRICS_APP_KEY`` variables
inside the current environment.

We recommend that you keep your credentials in environment variables.
That way you won't have to worry about accidentally posting your credentials
in a public place.
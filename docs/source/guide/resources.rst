.. _access-resources:

Accessing Resources
===================

To access Soccermetrics REST resources, you must first create a ``SoccermetricsRestClient`` object.

Authentication
--------------

The ``SoccermetricsRestClient`` requires the Soccermetrics API credentials.  These credentials are
passed directly to the constructor or through environment variables.  We recommend that you keep your
credentials in environment variables so that there is less of a chance of posting them in a public place.

The ``SoccermetricsRestClient`` searches for the credentials in the ``SOCCERMETRICS_APP_ID`` and
``SOCCERMETRICS_APP_KEY`` variables inside the current environment.  If they are present, a new
object is created.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

Alternatively, you can pass the credentials directly to the constructor.
::

    from soccermetrics.rest import SoccermetricsRestClient

    APP_ID = "f53baabb"
    APP_KEY = "demo1234567890demo1234567890"
    client = SoccermetricsRestClient(account=APP_ID,api_key=APP_KEY)

Making Requests
---------------

The ``SoccermetricsRestClient`` gives you access to over 20 resources that contain
historical match data and advanced analytics.  Several resources have sub-resources
that reach into the entire API.  You can make GET, HEAD, or OPTIONS
requests to these resources.

GET Requests
^^^^^^^^^^^^

To make a GET request, use the ``get()`` method associated with each resource.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    response = client.teams.get()

HEAD Requests
^^^^^^^^^^^^^

To make a HEAD request, use the ``head()`` method associated with each resource.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    response = client.teams.head()

OPTIONS Requests
^^^^^^^^^^^^^

To make an OPTIONS request, use the ``options()`` method associated with each resource.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    response = client.match.information.options()


Processing Responses
--------------------
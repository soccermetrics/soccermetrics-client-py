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

.. _get-request:

GET Requests
^^^^^^^^^^^^

To make a GET request, use the ``get()`` method associated with each resource.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    response = client.teams.get()

For many requests you might want to filter results by one or more parameters.
To do so, send keyword arguments to the ``get()`` method.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    response = client.club.match.information.get(home_team_name="Liverpool",away_team_name="Everton")

GET requests also accept paging arguments.  The following example will return
page 4 of the match information resource with 20 matches per page.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    response = client.club.match.information.get(page=4,records=20)

.. _head-request:

HEAD Requests
^^^^^^^^^^^^^

To make a HEAD request, use the ``head()`` method associated with each resource.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    response = client.validation.teams.head()

.. _options-request:

OPTIONS Requests
^^^^^^^^^^^^^^^^

To make an OPTIONS request, use the ``options()`` method associated with each resource.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    response = client.natl.match.information.options()

.. response-obj:

Processing Responses
--------------------

If your request is successful, your response will return a ``Response`` object.
This object returns the following attributes:

+------------+------------------------+
| Attribute  | Description            |
+============+========================+
| status     | Response status        |
+------------+------------------------+
| headers    | Response headers       |
+------------+------------------------+
| data       | Resource data          |
+------------+------------------------+

The following example handles the response from a resource request:
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    response = client.natl.match.information.get(home_team_name="Brazil",away_team_name="Germany")

    status_code = response.status
    headers = response.headers
    data = response.data

All resource responses are paged.  Each response object has the following properties:

+--------------+-------------------------+
| Attribute    | Description             |
+==============+=========================+
| page         | Current page number     |
+--------------+-------------------------+
| pages        | Total number of pages   |
+--------------+-------------------------+
| records_page | Records per page        |
+--------------+-------------------------+
| records      | Total number of records |
+--------------+-------------------------+

The following methods permit paging through the response:

+---------+---------------------------+
| Method  | Description               |
+=========+===========================+
| first   | First page of response    |
+---------+---------------------------+
| prev    | Previous page of response |
+---------+---------------------------+
| next    | Next page of response     |
+---------+---------------------------+
| last    | Last page of response     |
+---------+---------------------------+

If you wish to retrieve all of the records at once, use the ``all()`` method.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    goals = client.club.goals.get(matchday=5).all()

.. _hyperlink-resources:

Accessing Hyperlinked Resources
-------------------------------

Many of the resources contain references to other subresources through hyperlinks.
The client provides a ``link`` object to access these hyperlinks without
having to reconstruct the data manually.  You can then make ``get()``, ``head()``,
and ``options()`` calls just as you would for any other resource.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    match = client.club.information.get(home_team_name="Liverpool",away_team_name="Everton")

    goals = client.link.get(match.link.goals)
    pens = client.link.get(match.link.penalties,outcome_type="Goal")

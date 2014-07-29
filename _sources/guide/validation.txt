.. _validation-resources:

Validation Resources
====================

For more information, consult the `Validation Resource`_ documentation.

The Validation resources are used to validate data inputted into the database,
therefore ensuring data consistency and integrity.  You might use these resources
to populate dropdown boxes in an application or augment an API request.

Validation resources are grouped into two categories: Match Overview resources,
and Match Event resources.  However, Match Overview and Match Event resources
are accessed in the same way.  There is also a Persons resource that supports
all of the Personnel resources in the API.


Retrieving Resources
--------------------

To access the full representation of the Validation resource, make a ``get()`` call.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    confeds = client.confederations.get()
    for confed in confeds:
        print confed.name

Results are paged, which is irrelevant for most of the Validation resources
except the Countries resource.  If you wish to receive all of the results
at once, use the ``all()`` method on the response.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    resp = client.countries.get()
    countries = resp.all()


Retrieving a Specific Record in a Resource
------------------------------------------

To access a specific resource, call ``get()`` with the unique ID of the record.
You can also use the keyword ``uid`` in the function call.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    england = client.validation.countries.get("70570246789640e2a629d9b668df4c17")
    brazil = client.validation.countries.get(uid="70ce7b6218a24e1d94c21ed8b5cd070c")

You can also use the query parameters associated with each resource to search
for a specific record.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    cloudy_wx = client.validation.weather.get(desc='Cloudy')
    grass = client.validation.surfaces.get(name='Natural Grass')
    left_foot = client.validation.bodyparts.get(name='Left Foot')
    red_card = client.validation.cards.get(desc='Red')
    saved_penalty = client.validation.penalty_outcomes.get(desc='Saved')
    rooney = client.validation.persons.get(first_name='Wayne', last_name='Rooney')

.. warning::

    When retrieving records with the query parameter, there
    must be an exact match.

Retrieving Records from the Persons Resource
--------------------------------------------

The ``Persons`` resource provides access to biographical and demographical data
of all people involved with a football match, such as managers, referees, and
players.

You can retrieve all of the records using the ``get()`` method, but it is not
recommended because of the large size of the data returned.

In practice you will use the query parameters to filter the records returned by
the resource.  Keep in mind that all of the fields are populated except for
the ``nickname`` field, which is sometimes ``null``.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    argentina = client.validation.countries.get(name='Argentina').data
    argentines = client.validations.persons.get(country=argentina[0].id)

If you search by string, it must match **exactly**, including any diacritical
markings.  So a search for ``Arsène Wenger``
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    wenger_ok = client.validation.persons.get(first_name=u'Arsène',last_name=u'Wenger')

will create a match, but a search for ``Arsene Wenger``
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    wenger_err = client.validation.persons.get(first_name=u'Arsene',last_name=u'Wenger')

will result in an ``SoccermetricsRestException``.

.. _`Validation Resource`: http://soccermetrics.github.io/fmrd-summary-api/resources/validation/main.html
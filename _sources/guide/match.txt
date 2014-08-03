.. _match-resources:

Match Resources
===============

The Match resources are a collection of macro-events, micro-events, and summary
statistics resources in the Connect API.

For more information, consult the `Match Resource`_ documentation for the API.

Clubs or National Teams?
------------------------

The Connect API client divides Match resources into club and national team matches.  The
fact that countries are the "teams" in national team play introduces subtle but ultimately
significant differences to match modeling, in particular match lineups.

You can access club match data through the ``club`` object of the client:
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    club_matches = client.club

National team match data are accessed through the ``natl`` object of the client:
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    natl_matches = client.natl

Within the ``club`` and ``natl`` objects are sub-objects that permit access to macro-event,
micro-event, and statistical resources of the API.

Retrieving Match Resources
--------------------------

As with other resources you can ``get()`` match records, but in the case of match
records you can also use the unique ID of the football match to get data.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    match_info = client.natl.information.get('420aa27ce815499c85ec0301aff61ec4')

If only one variable is passed to ``get()``, it is assumed to be the unique match ID.  If
two variables are passed without keywords, the first variable is assumed to be the
unique match ID and the second the unique record ID.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    match_goal = client.natl.information.get('420aa27ce815499c85ec0301aff61ec4',
                                             '807f2a61bcea4a1bb98d66fface88b44')

Using Phase Detail Information to Retrieve Match Data
-----------------------------------------------------

In addition to using the match and record IDs to retrieve match records, you can use
information on a match's `phase details`_ to perform similar retrievals.  To do so,
perform the search as keyword arguments in the ``get()`` call.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    # league matches -- use matchday
    matches = client.club.information.get(competition_name="Premier League",
                                          season_name="2011-12", matchday=5)

    # group matches -- use round_name and group
    matches = client.natl.goals.get(competition_name="FIFA World Cup", season_name="2014",
                                    round_name="Group Stage", group='B', matchday=1)

    # knockout matches -- use round_name
    matches = client.club.offenses.get(competition_name="UEFA Champions League", season_name="2010",
                                       round_name="Second Qualifying Round", matchday=1)

Unique to other query parameters, you can insert an "*" to retrieve partial matches of
``round_name``.  This is beneficial for knockout round names such as ``Round of 32 (1/16)``,
``Quarterfinal (1/4)``, or ``Semi-Final (1/2)``, where alternate descriptions of the
round appear between parentheses.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    # knockout matches -- quarterfinal round
    matches = client.natl.information.get(competition_name="FIFA World Cup", season_name="2014",
                                          round_name="*1/4*")

.. warning:: You cannot use phase details to filter Match Micro-Events or Statistics resources.

Retrieving Match Information and Conditions
-------------------------------------------

To access high-level data on a specific match or its environmental conditions, pass the
unique ID through the ``match`` parameter in the ``get()`` call.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    match = client.natl.information.get('6b063a7370ee438da8a36a79ab10c9b7')
    conditions = client.natl.conditions.get('6b063a7370ee438da8a36a79ab10c9b7')

There is only one ``information`` and ``conditions`` record per match ID, so a unique
record ID is redundant.  In fact, passing a record ID will result in a ``SoccermetricsRestException``.

.. _match-macro:

Retrieving Match Macro-Events
-----------------------------

Match macro-events are the following:

    * ``lineups``: Match lineups
    * ``goals``: Goals
    * ``penalties``: Penalties
    * ``offenses``: Disciplinary offenses
    * ``substitutions``: Substitutions
    * ``shootouts``: Penalty shootouts

If you want to access all of a specific type of macro-event that occurs in a match,
pass the match ID to the ``get()`` call:
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    match_goals = client.natl.goals.get('6b063a7370ee438da8a36a79ab10c9b7')
    match_subs = client.natl.substitutions.get('6b063a7370ee438da8a36a79ab10c9b7')

If you want to access a *specific* macro-event from a match, pass the match ID **and**
the record ID to the ``get()`` call:
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    match_lineup_record = client.natl.lineups.get('6b063a7370ee438da8a36a79ab10c9b7',
                                                  'fcd53312a88c4e33b2a932746df0d3a8')
    match_goal = client.natl.goals.get('6b063a7370ee438da8a36a79ab10c9b7',
                                       '23d29e0d107f47068d8b85231b7f21c9')
    match_subs = client.natl.substitutions.get('6b063a7370ee438da8a36a79ab10c9b7',
                                               '05c62a4ceafb4dcd83d5a95a6b77baee')

Of course, you don't have to use the match IDs to retrieve data -- you can also use
query parameters such as ``home_team_name``, ``away_team_name``, or ``match_date``.
Check the API documentation to find out which query parameters apply for the resource
you're interested in.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    usa_goals = client.natl.goals.get(home_team_name="USA").all() + \
                client.natl.goals.get(away_team_name="USA").all()

    june_25_matches = client.natl.information.get(match_date="2014-06-25")

    successful_pens = client.natl.penalties.get(outcome_type="Goal").all()

.. _match-micro:

Retrieving Match Micro-Events
-----------------------------

Match micro-events are data on every event that occurs on the pitch during a match, whether
non-touch events in which the ball is not touched (e.g. start/end period, injury stoppage,
offside) or a ball touch event (e.g. pass, tackle, shot).

There are three sub-objects attached to the ``events`` object:

    * ``all``: all micro-events
    * ``touches``: all touch-events
    * ``actions``: contextual data for a micro-event

If you want to retrieve all of the micro-events for a match, pass the match ID to the
``get()`` call as a keyword parameter.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    match_events = client.natl.events.all.get(match='6b063a7370ee438da8a36a79ab10c9b7')

To retrieve a specific micro-event, pass the unique record ID.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    pass_event = client.natl.events.all.get('1ab8728733454bd7942a5711518e7366')

You can also use the query parameters to filter by specific types of events and match period.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    pass_events_2nd_half = client.natl.events.all.get(period=2, action_desc="Pass")

.. warning:: At this time you cannot filter micro-events by time or space intervals.

Almost every micro-event is associated with an event action, which will be included as a
hyperlink in the response.  We recommend that you use the ``link.get()`` call to access
the action (for more information see :ref:`hyperlink-resources`).
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    pass_event = client.natl.events.all.get('1ab8728733454bd7942a5711518e7366')
    pass_detail = client.link.get(pass_event.link.actions)

Buf if you must, you can use the ``actions`` sub-object and the unique ID of the event action
to retrieve **all** of the contextual data associated with an event action.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    pass_event = client.natl.events.all.get('1ab8728733454bd7942a5711518e7366')
    pass_detail = client.natl.events.actions.get('453baf79a6a742328e790bf29b01de57')

.. _match-stats:

Retrieving Match Statistics
---------------------------

`Match Statistics`_ resources provide access to in-match statistical data of participating
players in soccer matches.  There are nine sub-objects of the ``statistics`` object
in the client:

    * ``crosses``: Crossing statistics
    * ``defense``: Defensive statistics
    * ``fouls``: Foul statistics
    * ``goals``: Goal statistics
    * ``goalkeeper``: Goalkeeping statistics
    * ``passes``: Passing statistics
    * ``setpieces``: Set-piece statistics
    * ``shots``: Shot statistics
    * ``touches``: Ball touch statistics

A specific statistical record is one tied to a player who appears in the match lineup.
Use the lineup ID to access this record:
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    total_passes = client.natl.stats.passes.totals.get('5815554e70e24a7cad674cc410f9da82')
    total_crosses = client.natl.stats.crosses.totals.get('5815554e70e24a7cad674cc410f9da82')

You can also use the list of allowed query parameters to filter the statistics resources:
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    total_passes = client.natl.stats.passes.totals.get(player_name=u"James Rodríguez").all()


.. _`phase details`: http://soccermetrics.github.io/connect-api/resources/match/macros.html
.. _`Match Resource`: http://soccermetrics.github.io/connect-api/resources/match/main.html
.. _`Match Statistics`: http://soccermetrics.github.io/connect-api/resources/match/stats/main.html
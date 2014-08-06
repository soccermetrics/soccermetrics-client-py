.. _personnel-resources:

Personnel Resources
===================

For more information, consult the `Personnel Resource`_ documentation.


Retrieving a Player Record
--------------------------

With the client you can ``get()`` a player record and use the ``link.get()`` method
to access linked data, such as match appearances and actions.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    rvp = client.players.get(full_name='Robin Van Persie').all()
    rvp_matches = client.link.get(rvp.link.matches)
    rvp_goals = client.link.get(rvp.link.goals)

Some players have nicknames:
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    nani = client.players.get(full_name='Nani')

.. note::

    We recommend that you pass a Unicode string when searching on names
    or countries.  For example, ``full_name=u"Roberto Martínez"`` .

Retrieving a Manager Record
---------------------------

As with players you can retrieve a manager record and linked data such as
nationality, biographical data, and home and away matches managed.  Some
managers have nicknames (especially those who were former players), but
that's very rare.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    saf = client.managers.get(full_name='Alex Ferguson')
    saf_scotland = client.link.get(saf.link.country)
    saf_home_matches = client.link.get(saf.link.homeMatches)


Retrieving a Referee Record
---------------------------

You can retrieve a referee record and data linked to it, which include
biographical data and all matches officiated by the referee.  Referees
aren't considered special enough to merit nicknames (ones that you can print,
anyway).
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    webb = client.referees.get(full_name='Howard Webb')
    webb_england = client.link.get(webb.link.country)
    webb_matches = client.link.get(webb.link.matches)

.. _`Personnel Resource`: http://soccermetrics.github.io/connect-api/resources/personnel.html
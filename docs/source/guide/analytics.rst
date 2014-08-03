.. _analytics-resources:

Match Analytics Resources
=========================

The Match Analytics resources are a collection of advanced player and team analytics
related to events in a soccer match and derived from basic match data.

For more information consult the `Match Analytics Resource`_ documentation for the
Connect API.

Retrieving Match Analytics
--------------------------

At present there are three sub-objects attached to the ``analytics`` object:

    * ``state``: Match state
    * ``segment``: Match segment
    * ``tsr``: Match Total Shot Ratio

To retrieve analytics, you must pass the match ID to the ``get()`` call of the sub-object.
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    state = client.analytics.state.get('6b063a7370ee438da8a36a79ab10c9b7')

For most of the analytics sub-objects, no query parameters are permitted except for a
few exceptions:
::

    from soccermetrics.rest import SoccermetricsRestClient
    client = SoccermetricsRestClient()

    state = client.analytics.state.get('6b063a7370ee438da8a36a79ab10c9b7', time='60')

.. _`Match Analytics Resource`: http://soccermetrics.github.io/connect-api/resources/analytics.html
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

.. warning::

    This is a fictitious API ID and key. We ask all interested users to request
    access to the API in order to receive credentials.

If you call ``SoccermetricsRestClient`` without any parameters, the constructor
will look for ``SOCCERMETRICS_APP_ID`` and ``SOCCERMETRICS_APP_KEY`` variables
inside the current environment.

We recommend that you keep your credentials in environment variables.
That way you won't have to worry about accidentally posting your credentials
in a public place.

Match Information
-----------------

Let's get information from all matches for a specific matchday.  We'll use it to
access lineups and eventually match statistics.
::

    matches = client.match.information.get(matchday=10)
    for match in matches:
        print "%s: %s vs %s" % (match.match_date, match.home_team_name,
                                match.away_team_name)

Almost all of the resources have hyperlinks that refer to related resources, so
we can use those to access lineup data for each match.  We revise the above
code so that we can get starting lineups:
::

    matches = client.match.information.get(matchday=10)
    for match in matches:
        for team_name in [match.home_team_name, match.away_team_name]:
            lineup_data = client.link.get(
                match.link.lineups, player_team_name=team_name,
                is_starting=True).all()
            starters = [x.player_name for x in lineup_data]
            print "%s: %s" % (team_name, starters)

Match Statistics
----------------

We can go further and extract match statistics for each game, and create new
types of statistics from those.  Let's collect total shot data to develop
Total Shot Ratios for each team.  Again we use the hyperlinks associated
with each match to access the statistical data.  Revising the above code once more:
::

    ratio = []
    matches = client.match.information.get(matchday=10)
    for match in matches:
        total_shots = []
        for team_name in [match.home_team_name, match.away_team_name]:
            shot_data = client.link.get(
                match.link.stats.shots.totals, player_team_name=team_name).all()
            total_shots.append(sum([x.ontarget+x.offtarget for x in shots_data]))
        tsr = lambda k: total_shots[k]/float(sum(total_shots))
        ratio.append(dict(team=match.home_team_name,tsr=tsr(0)))
        ratio.append(dict(team=match.away_team_name,tsr=tsr(1)))

    for data in ratio:
        print "%s: %0.3f" % (data['team'],data['tsr'])

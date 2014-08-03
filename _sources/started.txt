.. _gettingstarted:

Getting Started
===============

To start using the Soccermetrics API, create a ``SoccermetricsRestClient``.

Get Your API Credentials
------------------------

In order to use the Soccermetrics API Client, you must have a Soccermetrics API account.

To get an account, go to the
`Soccermetrics Connect API website <https://developer.soccermetrics.net>`_
where you will fill in your contact information and select a usage plan.

You will receive your API ID and secret key in a few minutes, unless you signed up
for one of our student plans that require approval.

Using Your API Credentials
--------------------------

You'll need your Soccermetrics API credentials to use the ``SoccermetricsRestClient``.
These get passed to the constructor or via environment variables.
::

    from soccermetrics.rest import SoccermetricsRestClient

    appID = "f53baabb"
    appKey = "demo1234567890demo1234567890"

    client = SoccermetricsRestClient(account=appID,api_key=appKey)

.. warning:: This is a fictitious API ID and key.  DO NOT USE IT!!

If you call ``SoccermetricsRestClient`` without any parameters, the constructor
will look for ``SOCCERMETRICS_APP_ID`` and ``SOCCERMETRICS_APP_KEY`` variables
inside the current environment.

We recommend that you keep your credentials in environment variables.
That way you won't have to worry about accidentally posting your credentials
in a public place.

Match Information
-----------------

Let's get information from all matches for a specific matchday in a league competition.
We'll use it to access lineups and eventually match statistics.
::

    matches = client.club.match.information.get(matchday=10)
    for match in matches:
        print "%s: %s vs %s" % (match.match_date, match.home_team_name,
                                match.away_team_name)

.. warning::

    In reality, you would pass the name of the competition in the call.  Otherwise,
    you would receive all of the league matches for that matchday, over *all* of the
    competitions in the Soccermetrics database.

To access matches from the group stage of a competition, we need to include *at minimum* the
group round and group name:
::

    matches = client.natl.match.information.get(round_name='Group Stage', group=A, matchday=2)
    for match in matches:
        print "%s: %s vs %s" % (match.match_date, match.home_team_name,
                                match.away_team_name)

If we want to retrieve match from the knockout phase of a competition, we must pass
the round name:
::

    matches = client.club.match.information.get(round_name="Third Round")
    for match in matches:
        print "%s: %s vs %s" % (match.match_date, match.home_team_name,
                                match.away_team_name)

Almost all of the resources have hyperlinks that refer to related resources.  In this
case we use the hyperlinks to access lineup data related to each match.  We revise the
above code so that we can get starting lineups:
::

    matches = client.club.match.information.get(matchday=10)
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
    matches = client.club.match.information.get(matchday=10)
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

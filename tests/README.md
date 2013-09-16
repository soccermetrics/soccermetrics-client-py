API Client Unit Tests
=====================

This directory contains unit tests for the Soccermetrics API client.

Setup
-----

From root directory of the repository:

    $ python setup.py develop
    $ pip install -r tests/requirements.txt

Run Tests
---------

From root directory of the repository:

    $ nosetests -v tests/

Test Coverage Reports
---------------------

We use `coverage` to create coverage reports for the package.

From root directory of the repository:

    $ nosetests -v --with-coverage --cover-package=soccermetrics tests/

.PHONY: clean venv install test test-install coverage

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install -r requirements.txt; python setup.py install

test-install:
	. venv/bin/activate; pip install -r test/requirements.txt

test:
	. venv/bin/activate; nosetests

coverage:
	. venv/bin/activate; nosetests -v --with-coverage --cover-package=soccermetrics

clean:
	rm -rf venv/

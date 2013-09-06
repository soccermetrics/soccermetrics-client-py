.PHONY clean venv install

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install -r requirements.txt; python setup.py install

clean:
	rm -rf venv/
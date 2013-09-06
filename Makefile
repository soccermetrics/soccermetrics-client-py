.PHONY clean cenv install

cenv:
	virtualenv cenv

install: cenv
	. cenv/bin/activate; pip install -r requirements.txt

clean:
	rm -rf cenv/
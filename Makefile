PIP=@`which pip`
PYTHON=@`which python`
COVERAGE=@`which coverage`

clean:
	@find ./src -name *.pyc -delete

install:
	test -d venv || virtualenv venv
	$(PIP) install -r src/requirements.txt
	$(PIP) install -r requirements.txt
	$(PYTHON) src/manage.py migrate
	$(PYTHON) src/manage.py loaddata characters.json

serve:
	$(PYTHON) src/manage.py runserver

test:
	$(COVERAGE) run src/manage.py test src
	$(COVERAGE) report -m
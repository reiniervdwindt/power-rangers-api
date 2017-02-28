COVERAGE=@`which coverage`
ISORT=@`which isort`
PIP=@`which pip`
PROSPECTOR=@`which prospector`
PYTHON=@`which python`

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
	$(PIP) install -q coverage mock isort prospector
	$(PROSPECTOR) --messages-only --full-pep8
	$(ISORT) --recursive --check-only --quiet src/$*
	$(COVERAGE) run src/manage.py test src
	$(COVERAGE) report -m
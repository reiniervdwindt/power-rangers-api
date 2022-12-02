COVERAGE=@`which coverage`
FLAKE8=@`which flake8`
ISORT=@`which isort`
PIP=@`which pip`
PYTHON=@`which python`

clean:
	@find ./src -name *.pyc -delete

install:
	$(PYTHON) src/manage.py migrate
	$(PYTHON) src/manage.py loaddata allies.json civilians.json monsters.json rangers.json series.json villains.json weapons.json zords.json

flake8:
	$(FLAKE8) src

isort:
	$(ISORT) --check --quiet src

tests:
	$(COVERAGE) erase
	$(COVERAGE) run --source=src src/manage.py test src
	$(COVERAGE) report -m

quality: isort flake8 tests

safety:
	$(POETRY) export -f requirements.txt | $(SAFETY) check --stdin

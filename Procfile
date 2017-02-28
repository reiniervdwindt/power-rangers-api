release: python src/manage.py migrate
web: gunicorn main.wsgi --log-file - --chdir src

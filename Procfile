release: python manage.py migrate
web: daphne fpt.asgi:application
worker: python manage.py runworker channels --settings=fpt.settings -v2
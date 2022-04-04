release: python manage.py migrate
web: gunicorn -k uvicorn.workers.UvicornWorker fpt.asgi:application



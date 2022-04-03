import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fpt.settings')

app = Celery('fpt')
app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {

    'get_rtdata_5s': {
        'task': 'live.tasks.get_rtdata',
        'schedule': 5.0
    }
}
app.autodiscover_tasks(settings.INSTALLED_APPS)

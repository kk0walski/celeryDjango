from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapper.settings')
app = Celery('scrapper')

app.conf.broker_url = 'redis://127.0.0.1:6379'
app.conf.result_backend = 'django-db'
app.config_from_object(settings)

app.conf.beat_shedule = {
    
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
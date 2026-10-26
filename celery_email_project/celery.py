from __future__ import absolute_import, unicode_literals
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_email_project.settings')

from celery import Celery
from django.conf import settings


app = Celery('celery_email_project')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self, *args, **kwargs):
    print('Request: {0!r}'.format(self.request))
    
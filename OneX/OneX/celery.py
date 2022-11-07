from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OneX.settings')

app = Celery('OneX')

# platforms.C_FORCE_ROOT = True

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
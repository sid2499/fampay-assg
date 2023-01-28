import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay.settings')

app = Celery('fampay')
app.conf.enable_utc = False

app.conf.update(timezone='Aisa/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# CELERY BEAT SETTINGS
app.conf.beat_schedule = {

}

app.autodiscover_tasks()

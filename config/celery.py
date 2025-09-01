from celery import Celery
import os
from config.settings.celery_conf import CELERY

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

app = Celery('habit-tracker')

app.config_from_object(CELERY)

app.autodiscover_tasks()


from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fitness.settings')
app = Celery('Fitness')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-subscription-expiry-email': {
        'task': 'myapp.tasks.send_subscription_expiry_email',
        'schedule': crontab(hour=0, minute=0),
    },
}


#celery -A Fitness worker -l info
#celery -A Fitness beat -l info
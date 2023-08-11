from __future__ import absolute_import

from datetime import timedelta

from celery import Celery, signals
from celery.schedules import crontab

from .constants import CELERY_APP
from .services.sentry import init_sentry
from .settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

celery_app = Celery(
    __name__,
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL,
)


publish_temperature_data_task = "publish_temperature_data"
ingest_temperature_data_task = "ingest_temperature_data"

# Setting up Sentry for Celery
@signals.celeryd_init.connect
def init_sentry_for_celery(**kwargs):
    init_sentry(app=CELERY_APP)


celery_app.conf.result_expires = timedelta(hours=1)  # TTL for celery task results
celery_app.conf.task_create_missing_queues = True
celery_app.conf.timezone = "UTC"
celery_app.autodiscover_tasks(["IoTDashboard"])
celery_app.conf.beat_schedule = {
    "run-every-minute": {
        "task": publish_temperature_data_task,
        "schedule": crontab(),  # Default 60 seconds (1 minute)
    },
}

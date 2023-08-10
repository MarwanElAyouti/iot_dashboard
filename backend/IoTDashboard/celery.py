from __future__ import absolute_import

from datetime import timedelta

from celery import Celery, signals

from IoTDashboard.constants import CELERY_APP
from IoTDashboard.services.sentry import init_sentry
from IoTDashboard.settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

celery_app = Celery(
    __name__,
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL,
)


# Setting up Sentry for Celery
@signals.celeryd_init.connect
def init_sentry_for_celery(**kwargs):
    init_sentry(app=CELERY_APP)


celery_app.conf.result_expires = timedelta(hours=1)  # TTL for celery task results
celery_app.conf.task_create_missing_queues = True
celery_app.conf.timezone = "UTC"
celery_app.autodiscover_tasks(["IoTDashboard"])

import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration

from IoTDashboard.constants import CELERY_APP, FAST_API_APP
from IoTDashboard.settings import APP_ENV, SENTRY_DSN

integrations_dict: dict = {CELERY_APP: CeleryIntegration, FAST_API_APP: FastApiIntegration}


def init_sentry(app: str) -> None:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[integrations_dict[app]()],
        before_send=lambda x, y: x if APP_ENV == "PRODUCTION" else None,
        attach_stacktrace=True,
        send_default_pii=True,
    )

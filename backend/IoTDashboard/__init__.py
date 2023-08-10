from __future__ import absolute_import

from typing import Sequence

from IoTDashboard.celery import celery_app  # noqa

__all__: Sequence = (celery_app,)  # to ignore 'imported but unused' warning

import logging
import sys

from IoTDashboard.settings import APP_ENV

log_level = logging.INFO if APP_ENV == "PRODUCTION" else logging.DEBUG

logger = logging.getLogger("app")
logger.setLevel(log_level)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(log_level)

logger.addHandler(handler)

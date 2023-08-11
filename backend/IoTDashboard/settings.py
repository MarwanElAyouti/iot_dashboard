import os

from dynaconf import Dynaconf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(load_dotenv=True, envvar_prefix=False)

DEFAULT_TIMEZONE = "UTC"

# Application environment
APP_ENV = settings.APP_ENV

# Database
DB_URL = settings.DB_URL

# Celery
CELERY_RESULT_BACKEND = settings.CELERY_RESULT_BACKEND
CELERY_BROKER_URL = settings.CELERY_BROKER_URL

# JWT
SECRET_KEY = settings.SECRET_KEY

# Sentry
SENTRY_DSN = settings.SENTRY_DSN


# MQTT
MQTT_BROKER_URL = settings.MQTT_BROKER_URL
MQTT_USERNAME = settings.MQTT_USERNAME
MQTT_PASSWORD = settings.MQTT_PASSWORD

#!/bin/bash

set -o errexit
set -o nounset

if [ -n "${SERVICE-}" ] && [ "$SERVICE" = "celery" ]
then
    while ! nc -z $RABBITMQ_HOST $RABBITMQ_PORT; do
        sleep 0.5
    done
    echo "${RABBITMQ_HOST} accepts connections..."
fi

exec "$@"
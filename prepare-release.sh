#!/usr/bin/env sh

poetry export -f requirements.txt -o openreservation/requirements.txt  --without-hashes
cd openreservation; poetry run python manage.py collectstatic --noinput

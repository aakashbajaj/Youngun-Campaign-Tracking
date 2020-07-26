#!/bin/sh

cd youngun

rm *.sqlite3

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --noinput

python manager.py runsevrer 0.0.0.0:8000 && python manage.py qcluster
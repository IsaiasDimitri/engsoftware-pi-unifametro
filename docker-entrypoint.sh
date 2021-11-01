#!/bin/bash

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py loaddata user.json
python manage.py runserver 0.0.0.0:8000
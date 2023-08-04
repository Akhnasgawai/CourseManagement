#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

celery -A CourseManagement worker --l info --pool=solo

flower -A CourseManagement

#!/bin/bash
set -e
python manage.py migrate
python manage.py makesuperuser
python manage.py load_seed_data

#!/bin/bash
echo 'hi'
python manage.py makemigrations
python manage.py migrate

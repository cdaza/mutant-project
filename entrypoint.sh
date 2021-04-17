#!/usr/bin/env bash
#Modify this export to change the environment

export BOILERPLATE_ENV=prod

python manage.py gunicorn
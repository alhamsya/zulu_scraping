#!/usr/bin/env bash

export FLASK_APP=app_main.py
export FLASK_ENV=production

flask run --host=192.168.0.101 --port=8000
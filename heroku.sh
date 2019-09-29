#!/bin/bash
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="test"

gunicorn app:app --daemon
python worker.py

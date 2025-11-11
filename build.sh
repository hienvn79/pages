#!/bin/bash
# Build/Deploy script for Django on Render Web Service

set -e  # stop script if any command fails

echo "Installing requirements..."
pip install -r requirements.txt

echo "Setting environment variables..."
export DJANGO_SETTINGS_MODULE=django_project.settings

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Build/Deploy completed successfully!"

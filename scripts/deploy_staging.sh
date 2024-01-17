#!/bin/bash

# deploy_staging.sh

# Exit script on any error
set -e

echo "Starting Staging Deployment..."

# Commands to run on the server

# Go to the application directory
mkdir cicd_tutorial && cd cicd_tutorial

# Pull the latest code from the repository
git pull $REPOSITORY_URL staging

# Install dependencies (if required)
pip install -r requirements.txt

# Run database migrations (if applicable)
# python manage.py migrate

# Restart the application server (e.g., using Gunicorn for a Python app)
# systemctl restart gunicorn

#echo "Application successfully deployed to staging!"

echo "Staging Deployment Completed Successfully!"

#!/bin/bash

# deploy_staging.sh

# Exit script on any error
set -e

# AWS Configuration
#AWS_ACCESS_KEY_ID=<your-aws-access-key-id>
#AWS_SECRET_ACCESS_KEY=<your-aws-secret-access-key>
#REGION=<your-aws-region>
#EC2_INSTANCE_ID=<your-ec2-instance-id>

# SSH Configuration
#SSH_KEY_PATH="<path-to-your-ssh-private-key>"
#SSH_USER=<ssh-user>
#SSH_HOST=<ec2-instance-public-dns-or-ip>

# Application Specifics
#APP_DIR="/path/to/your/app/on/server"
#REPO_URL="https://github.com/your-username/your-repo.git"
#BRANCH="main"

echo "Starting Staging Deployment..."

# SSH into the EC2 instance and perform deployment tasks
ssh -i ${EC2_SSH_KEY} "ec2-user@{$STAGING_EC2_IP}" << 'ENDSSH'
    # Commands to run on the server

    # Go to the application directory
    mkdir cicd_tutorial && cd cicd_tutorial

    # Pull the latest code from the repository
    git pull ${REPOSITORY_URL} staging

    # Install dependencies (if required)
    pip install -r requirements.txt

    # Run database migrations (if applicable)
    # python manage.py migrate

    # Restart the application server (e.g., using Gunicorn for a Python app)
    # systemctl restart gunicorn

    echo "Application successfully deployed to staging!"

ENDSSH

echo "Staging Deployment Completed Successfully!"

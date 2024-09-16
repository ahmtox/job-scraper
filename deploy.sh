#!/bin/bash
echo "Pulling latest changes from GitHub..."
git pull origin main

echo "Activating python environment"
source venv/bin/activate

echo "Installing updated dependencies..."
pip install -r requirements.txt

echo "Restarting Gunicorn..."
sudo systemctl restart job-scraper

echo "Deactivating python environment"
deactivate
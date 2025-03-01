#!/bin/bash

echo "BUILD START"

# Check Python version
python3.9 --version

# Install pip if it's not installed
python3.9 -m ensurepip --upgrade

# Upgrade pip
python3.9 -m pip install --upgrade pip

# Install dependencies from requirements.txt
python3.9 -m pip install --no-cache-dir -r requirements.txt


echo "MAKE MIGRATIONS..."
# Make and apply migrations
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect static files
python3.9 manage.py collectstatic --noinput

echo "BUILD END"

#!/bin/bash

# Define paths
VENV_PATH="env"
PROJECT_PATH="visualizer"
REQUIREMENTS_FILE="requirements.txt"

# Check if the virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment..."
    source "$VENV_PATH/bin/activate"
fi

# Install requirements if not already installed
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "requirements.txt not found. Make sure it exists in your project directory."
    exit 1
fi

pip3 install -r "$REQUIREMENTS_FILE"

echo "Starting Django server..."
cd $PROJECT_PATH
python3 manage.py runserver 0.0.0.0:8000    

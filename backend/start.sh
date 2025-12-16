#!/bin/bash

# Start the FastAPI application with uvicorn
# This script can be used for local development or in production

# Set default values if environment variables are not set
export HOST=${HOST:-"0.0.0.0"}
export PORT=${PORT:-"8000"}
export WORKERS=${WORKERS:-"1"}

# Check if requirements are installed
if [ ! -f "requirements.txt" ]; then
    echo "Error: requirements.txt not found"
    exit 1
fi

# Install dependencies if not already installed
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "Warning: .env file not found. Make sure environment variables are set."
fi

# Run the application
echo "Starting Chatbot API on $HOST:$PORT with $WORKERS workers"
uvicorn src.main:app --host $HOST --port $PORT --workers $WORKERS
#!/bin/bash

echo "Starting Workflow..."

# Dynamically get the directory of this script (works from anywhere)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Define the full path to requirements.txt
REQ_FILE="$SCRIPT_DIR/src/requirements.txt"

# Step 1: Install Dependencies
echo "Installing dependencies from $REQ_FILE..."
if [ -f "$REQ_FILE" ]; then
  pip install -r "$REQ_FILE" || { echo "Dependency installation failed"; exit 1; }
else
  echo "Could not find requirements.txt at $REQ_FILE"
  exit 1
fi

# Step 2: Run Unit Tests
echo "Running unit tests for time_parser..."
PYTHONPATH=. pytest -s "$SCRIPT_DIR/src/test_time_parser.py" || { echo "Tests failed"; exit 1; }

# Step 3: Run CLI App
echo "Running CLI app locally..."
PYTHONPATH=. python "$SCRIPT_DIR/src/app.py" || exit 1

# Step 4: Launch Web App
echo "Launching web app locally..."
PYTHONPATH=. python "$SCRIPT_DIR/src/web.py" || { echo "❌ Failed to launch web app"; exit 1; }

echo "All tasks completed successfully."




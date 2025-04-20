#!/bin/bash

echo "🚀 Starting Workflow..."

#1. Install Dependencies
echo "Installing dependencies..."
pip install -r src/requirements.txt || { echo "Dependency installation failed"; exit 1; }

# 2. Testing
echo "unit testing time_parser function..."
PYTHONPATH=. pytest -s src/test_time_parser.py || { echo "testing failed"; exit 1; }

# 3. run app in local
echo "runing app in local"
PYTHONPATH=. python src/app.py || exit 1

# 3. lunch web app in local
echo "runing web app in local"
PYTHONPATH=. python src/web.py || { echo "Failed to launch web app"; exit 1; }


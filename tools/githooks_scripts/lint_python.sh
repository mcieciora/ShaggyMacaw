#!/bin/sh

echo "Installing latest dependencies..."
python -m pip install -r requirements/requirements-testing.txt

echo "Running flake8 in src"
python -m flake8 --max-line-length 120 --max-complexity 10 src
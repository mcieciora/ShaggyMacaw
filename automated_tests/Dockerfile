FROM python:3.12.2-slim

WORKDIR /app
COPY requirements/testing/requirements.txt ./requirements-testing.txt
COPY requirements/example_app/requirements.txt pytest.ini ./

WORKDIR /app/automated_tests
COPY automated_tests .

WORKDIR /app/src
COPY src .

WORKDIR /app
RUN python3 -m pip install --no-cache-dir -r requirements.txt -r requirements-testing.txt
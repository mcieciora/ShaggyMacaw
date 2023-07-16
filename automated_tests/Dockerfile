FROM python:3.11-slim

COPY requirements.txt app/requirements.txt
COPY requirements/requirements-testing.txt app/requirements-testing.txt
COPY pytest.ini app/pytest.ini

COPY automated_tests app/automated_tests

COPY src app/src

WORKDIR app

RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install -r requirements-testing.txt
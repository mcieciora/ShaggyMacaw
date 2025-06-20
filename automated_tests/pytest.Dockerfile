ARG DEFAULT_IMAGE_TAG=3.9

FROM python:${DEFAULT_IMAGE_TAG}

RUN python3 -m pip install pytest

WORKDIR /app

ENTRYPOINT ["pytest", "--collect-only"]
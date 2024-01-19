#!/bin/bash

set -e

find "$(pwd)" -name "Dockerfile" | while read DOCKERFILE_VALUE
do
  echo "$DOCKERFILE_VALUE"
  docker run --rm -i hadolint/hadolint < "$DOCKERFILE_VALUE" || exit 1
done

#!/bin/bash

RETURN_VALUE=0
DOCKERHUB_REPO="mcieciora/careless_vaquita"

TAGS="latest test_image"
for TAG in $TAGS; do
  echo "Running docker scout on $TAG image"
  docker scout cves $DOCKERHUB_REPO:"$TAG" --exit-code --only-severity critical,high
  SCAN_RESULT=$?
  if [ "$SCAN_RESULT" -ne 0 ]; then
    echo "Vulnerabilities found. Running recommendations"
    docker scout recommendations $DOCKERHUB_REPO:"$TAG" > scan_"$TAG".txt
    RETURN_VALUE=1
  else
    echo "No vulnerabilities detected"
  fi
done

exit "$RETURN_VALUE"

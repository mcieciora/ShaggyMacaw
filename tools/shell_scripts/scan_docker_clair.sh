#!/bin/bash

DOCKERHUB_REPO="mcieciora/careless_vaquita"

TAGS="latest test_image"
for TAG in $TAGS; do
  echo "Running docker clair on $TAG image"
  docker run -d --name db arminc/clair-db &&
  sleep 10
  docker run -p 6060:6060 --link db:postgres -d --name clair arminc/clair-local-scan
  sleep 5
  wget -qO clair-scanner https://github.com/arminc/clair-scanner/releases/download/v8/clair-scanner_linux_amd64 && chmod +x clair-scanner
  ./clair-scanner $DOCKERHUB_REPO:"$TAG" > scan_clair_"$TAG".txt
done

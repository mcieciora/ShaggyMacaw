#!/bin/bash

CHECK_TIME=$1

docker compose up -d
echo "Sleeping for $CHECK_TIME"
sleep "$CHECK_TIME"

VALUE=$(docker ps -q | wc -l)

if [ "$VALUE" -eq 2 ]; then
  exit 0
else
  exit 1
fi

#!/bin/bash

TAG_NAME=$1
TAG_COMMENT=$2

git tag -a "$TAG_NAME" -m "$TAG_COMMENT" && git push origin "$TAG_NAME"

RETURN_VALUE=$?

if [ "$RETURN_VALUE" -eq 0 ]; then
  echo "Tag $TAG_NAME created and pushed."
  exit 0
else
  echo "Tag creation failed."
  exit 1
fi

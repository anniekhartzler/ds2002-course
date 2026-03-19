#!/bin/bash

FILE="$1"
BUCKET="$2"
EXPIRES="$3"

if [ $# -ne 3 ]; then
    echo "Usage: $0 <local_file> <bucket_name> <expires_in_seconds>"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "Error: file '$FILE' does not exist."
    exit 1
fi

aws s3 cp "$FILE" "s3://$BUCKET/"
aws s3 presign --expires-in "$EXPIRES" "s3://$BUCKET/$(basename "$FILE")"

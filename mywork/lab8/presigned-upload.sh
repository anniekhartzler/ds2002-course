#!/bin/bash

# Upload a file to a private S3 bucket, then generate a presigned URL.
# Usage:
#   ./presigned-upload.sh LOCAL_FILE BUCKET_NAME EXPIRATION_SECONDS

FILE="$1"
BUCKET="$2"
EXPIRES="$3"

if [ $# -ne 3 ]; then
    echo "Usage: $0 LOCAL_FILE BUCKET_NAME EXPIRATION_SECONDS"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "Error: file '$FILE' does not exist."
    exit 1
fi

aws s3 cp "$FILE" "s3://$BUCKET/"

if [ $? -ne 0 ]; then
    echo "Upload failed."
    exit 1
fi

aws s3 presign --expires-in "$EXPIRES" "s3://$BUCKET/$(basename "$FILE")"

import sys
import boto3


def upload_file(bucket_name: str, local_file: str, key: str, public: bool = False) -> None:
    """
    Upload a file to S3.
    If public is True, upload with ACL public-read.
    Otherwise upload as private.
    """
    s3 = boto3.client("s3", region_name="us-east-1")

    with open(local_file, "rb") as f:
        if public:
            s3.put_object(Bucket=bucket_name, Key=key, Body=f, ACL="public-read")
        else:
            s3.put_object(Bucket=bucket_name, Key=key, Body=f)

    print(f"Uploaded {local_file} to s3://{bucket_name}/{key}")


def presign_file(bucket_name: str, key: str, expires: int = 3600) -> None:
    """
    Generate a presigned URL for an S3 object.
    """
    s3 = boto3.client("s3", region_name="us-east-1")
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket_name, "Key": key},
        ExpiresIn=expires
    )
    print(url)


def main():
    """
    Usage:
      python s3_upload.py upload BUCKET LOCAL_FILE KEY [public]
      python s3_upload.py presign BUCKET KEY EXPIRES
    """
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python s3_upload.py upload BUCKET LOCAL_FILE KEY [public]")
        print("  python s3_upload.py presign BUCKET KEY EXPIRES")
        sys.exit(1)

    command = sys.argv[1]

    if command == "upload":
        if len(sys.argv) < 5:
            print("Usage: python s3_upload.py upload BUCKET LOCAL_FILE KEY [public]")
            sys.exit(1)

        bucket = sys.argv[2]
        local_file = sys.argv[3]
        key = sys.argv[4]
        public = len(sys.argv) > 5 and sys.argv[5].lower() == "public"

        upload_file(bucket, local_file, key, public)

    elif command == "presign":
        if len(sys.argv) != 5:
            print("Usage: python s3_upload.py presign BUCKET KEY EXPIRES")
            sys.exit(1)

        bucket = sys.argv[2]
        key = sys.argv[3]
        expires = int(sys.argv[4])

        presign_file(bucket, key, expires)

    else:
        print("Unknown command.")
        sys.exit(1)


if __name__ == "__main__":
    main()

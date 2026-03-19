import sys
import boto3


def upload_file(bucket_name: str, local_file: str, key: str) -> None:
    """
    Upload a private file to S3.
    """
    s3 = boto3.client("s3", region_name="us-east-1")
    with open(local_file, "rb") as f:
        s3.put_object(Bucket=bucket_name, Key=key, Body=f)
    print(f"Uploaded {local_file} to s3://{bucket_name}/{key}")


def presign_file(bucket_name: str, key: str, expires_in: int = 604800) -> str:
    """
    Generate a presigned URL for an S3 object.
    """
    s3 = boto3.client("s3", region_name="us-east-1")
    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket_name, "Key": key},
        ExpiresIn=expires_in,
    )


def main() -> None:
    if len(sys.argv) < 4:
        print("Usage: python s3_upload.py <bucket> <local_file> <key> [expires]")
        sys.exit(1)

    bucket = sys.argv[1]
    local_file = sys.argv[2]
    key = sys.argv[3]
    expires = int(sys.argv[4]) if len(sys.argv) == 5 else 604800

    upload_file(bucket, local_file, key)
    url = presign_file(bucket, key, expires)

    print("Presigned URL:")
    print(url)


if __name__ == "__main__":
    main()

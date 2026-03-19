import os
import glob
import argparse
import logging
import boto3
from botocore.exceptions import ClientError


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def parse_args():
    """
    Parse command line arguments and return the input folder and destination.
    """
    parser = argparse.ArgumentParser(description="Upload results-*.csv files to S3.")
    parser.add_argument("input_folder", help="Folder containing results-*.csv files")
    parser.add_argument("destination", help="Destination in the form bucket/prefix/")
    args = parser.parse_args()
    return args.input_folder, args.destination


def upload(input_folder, destination):
    """
    Upload results-*.csv files from input_folder to the S3 destination.
    """
    try:
        if "/" not in destination:
            raise ValueError("Destination must be in the form bucket/prefix/")

        bucket, prefix = destination.split("/", 1)
        s3 = boto3.client("s3", region_name="us-east-1")

        pattern = os.path.join(input_folder, "results-*.csv")
        files = glob.glob(pattern)

        if not files:
            logger.warning("No files found matching %s", pattern)
            return False

        for file_path in files:
            file_name = os.path.basename(file_path)
            key = f"{prefix.rstrip('/')}/{file_name}"
            logger.info("Uploading %s to s3://%s/%s", file_path, bucket, key)
            with open(file_path, "rb") as f:
                s3.put_object(Bucket=bucket, Key=key, Body=f)

        return True

    except (ClientError, OSError, ValueError) as e:
        logger.error("Upload failed: %s", e)
        return False


def main():
    """
    Run the upload workflow and log success or failure.
    """
    input_folder, destination = parse_args()
    success = upload(input_folder, destination)

    if success:
        logger.info("All matching files uploaded successfully.")
    else:
        logger.error("File upload process did not complete successfully.")


if __name__ == "__main__":
    main()

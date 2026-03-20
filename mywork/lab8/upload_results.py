import os
import sys
import glob
import logging
import boto3


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)
logger = logging.getLogger(__name__)


def parse_args():
    """
    Parse command line arguments and return the input folder
    and destination bucket/prefix.
    """
    if len(sys.argv) != 3:
        print("Usage: python upload_results.py INPUT_FOLDER BUCKET/PREFIX")
        sys.exit(1)

    input_folder = sys.argv[1]
    destination = sys.argv[2]
    return input_folder, destination


def upload(input_folder, destination):
    """
    Upload all results-*.csv files from the input folder
    to the specified S3 bucket/prefix destination.
    """
    try:
        if "/" not in destination:
            raise ValueError("Destination must be in the form bucket/prefix")

        bucket, prefix = destination.split("/", 1)

        s3 = boto3.client("s3", region_name="us-east-1")

        pattern = os.path.join(input_folder, "results-*.csv")
        files = glob.glob(pattern)

        if not files:
            logger.warning(f"No files matched {pattern}")
            return False

        for filepath in files:
            filename = os.path.basename(filepath)
            key = f"{prefix.rstrip('/')}/{filename}"

            with open(filepath, "rb") as f:
                s3.put_object(Bucket=bucket, Key=key, Body=f)

            logger.info(f"Uploaded {filepath} to s3://{bucket}/{key}")

        return True

    except Exception as e:
        logger.error(f"Upload failed: {e}")
        return False


def main():
    """
    Main function to parse arguments, upload files,
    and log overall success or failure.
    """
    input_folder, destination = parse_args()
    success = upload(input_folder, destination)

    if success:
        logger.info("All matching files uploaded successfully.")
    else:
        logger.error("Upload process did not complete successfully.")


if __name__ == "__main__":
    main()

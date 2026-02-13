#!/usr/bin/env python3

"""
ISS Tracker ETL Pipeline
Extracts ISS location data from API,
transforms it into tabular format,
and loads it into a CSV file.
"""

import sys
import os
import requests
import pandas as pd
import logging


# -------------------------
# Logger Setup
# -------------------------

logger = logging.getLogger("iss_tracker")
logger.setLevel(logging.INFO)

# Console output
stream_handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
stream_handler.setFormatter(formatter)

# File output (optional challenge)
file_handler = logging.FileHandler("iss.log")
file_handler.setFormatter(formatter)

# Add both handlers
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


# -------------------------
# Extract
# -------------------------

def extract():
    """
    Extract ISS location JSON data from API.
    Returns parsed JSON dictionary.
    """
    url = "http://api.open-notify.org/iss-now.json"

    try:
        logger.info("Extracting data from ISS API...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.info("Data successfully extracted.")
        return data

    except requests.exceptions.RequestException as e:
        logger.error(f"Error during extraction: {e}")
        return None


# -------------------------
# Transform
# -------------------------

def transform(data):
    """
    Transform raw JSON into a single-row pandas DataFrame.
    Converts UNIX timestamp to readable datetime.
    """
    if data is None:
        logger.warning("No data to transform.")
        return None

    try:
        logger.info("Transforming data...")

        timestamp = data["timestamp"]
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]

        readable_time = pd.to_datetime(timestamp, unit='s')

        df = pd.DataFrame([{
            "timestamp": readable_time,
            "latitude": latitude,
            "longitude": longitude
        }])

        logger.info("Data successfully transformed.")
        return df

    except Exception as e:
        logger.error(f"Error during transformation: {e}")
        return None


# -------------------------
# Load
# -------------------------

def load(df, filename):
    """
    Append transformed DataFrame to CSV file.
    Creates file if it does not exist.
    """
    if df is None:
        logger.warning("No data to load.")
        return

    try:
        logger.info("Loading data to CSV...")

        if os.path.exists(filename):
            existing_df = pd.read_csv(filename)
            combined_df = pd.concat([existing_df, df], ignore_index=True)
            combined_df.to_csv(filename, index=False)
        else:
            df.to_csv(filename, index=False)

        logger.info(f"Data successfully written to {filename}")

    except Exception as e:
        logger.error(f"Error during loading: {e}")


# -------------------------
# Main
# -------------------------

def main():
    """
    Main ETL pipeline:
    Extract → Transform → Load
    """
    if len(sys.argv) != 2:
        logger.error("Usage: python iss.py <output_file.csv>")
        sys.exit(1)

    output_file = sys.argv[1]

    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data, output_file)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python github-events.py <github-username>")
        sys.exit(1)

    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}/events/public"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    events = response.json()

    for event in events:
        print(f"{event['type']} at {event['created_at']}")

if __name__ == "__main__":
    main()

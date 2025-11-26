#!/usr/bin/env python3

import sys
import json
import urllib.request
import urllib.error


# -------------------------------
# Fetch GitHub user activity
# -------------------------------
def fetch_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as response:
            data = response.read()
            return json.loads(data)

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("❌ Error: User not found. Check the username.")
        else:
            print(f"❌ HTTP Error: {e.code}")
        sys.exit(1)

    except urllib.error.URLError:
        print("❌ Network error: Unable to reach GitHub.")
        sys.exit(1)


# -------------------------------
# Parse GitHub events
# -------------------------------
def display_activity(events):
    if not events:
        print("No recent activity found.")
        return

    print("\nRecent GitHub Activity:\n")

    for event in events:
        event_type = event["type"]
        repo = event["repo"]["name"]

        # Push events
        if event_type == "PushEvent":
            commits = event["payload"].get("commits", [])
            commit_count = len(commits)
            print(f"- Pushed {commit_count} commits to {repo}")

        # Issues created
        elif event_type == "IssuesEvent" and event["payload"]["action"] == "opened":
            print(f"- Opened a new issue in {repo}")

        # Starred repo
        elif event_type == "WatchEvent":
            print(f"- Starred {repo}")

        # Forked repo
        elif event_type == "ForkEvent":
            print(f"- Forked {repo}")

        # Pull requests
        elif event_type == "PullRequestEvent":
            action = event["payload"]["action"]
            print(f"- {action.capitalize()} a pull request in {repo}")

        # Default
        else:
            print(f"- {event_type} in {repo}")


# -------------------------------
# Main CLI handler
# -------------------------------
def main():
    if len(sys.argv) < 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Fetching activity for GitHub user: {username} ...")

    events = fetch_activity(username)
    display_activity(events)


if __name__ == "__main__":
    main()

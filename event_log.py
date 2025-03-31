import subprocess

def search_event_logs():
    """Search the System Event Log for Level 2 events (errors) from the last 24 hours."""
    query = "*[System[(Level=2) and TimeCreated[timediff(@SystemTime) <= 86400000]]]"
    try:
        result = subprocess.run(
            ["wevtutil", "qe", "System", "/q:" + query, "/c:50", "/f:text"],
            capture_output=True, text=True, shell=True
        )
        logs = result.stdout.strip()
        if logs:
            print("Matched Logs:\n", logs)
            print(f"\nTotal Matches: {logs.count('Event ID:')}")
        else:
            print("No matches found.")
    except Exception as e:
        print(f"Error searching logs: {e}")

if __name__ == "__main__":
    search_event_logs()

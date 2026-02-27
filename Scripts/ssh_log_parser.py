import re
from collections import defaultdict
from datetime import datetime

LOG_FILE = "../logs/sample_auth.log"

failed_pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")
time_pattern = re.compile(r"^(\w+\s+\d+\s+\d+:\d+:\d+)")

ip_attempts = defaultdict(int)
ip_timestamps = defaultdict(list)

with open(LOG_FILE, "r") as file:
    for line in file:
        failed_match = failed_pattern.search(line)
        time_match = time_pattern.search(line)

        if failed_match and time_match:
            ip = failed_match.group(1)
            timestamp_str = time_match.group(1)

            timestamp = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")
            
            ip_attempts[ip] += 1
            ip_timestamps[ip].append(timestamp)

print("\n=== SSH Failed Login Summary ===\n")

for ip, count in ip_attempts.items():
    print(f"IP Address: {ip}")
    print(f"Failed Attempts: {count}")

    if count >= 5:
        print("⚠ Potential Brute Force Detected\n")
    else:
        print()
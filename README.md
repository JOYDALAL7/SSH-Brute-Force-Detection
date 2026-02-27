# 🔐 SSH Bruteforce Attack Investigation

## Overview

A SOC investigation into multiple failed SSH authentication attempts detected against a Linux system. The observed activity exhibited characteristics consistent with an automated brute-force attack, including repeated failures, username variation, and short intervals between attempts.

## Key Findings

- 9 failed SSH password attempts from the same source address
- 6 PAM authentication failures confirmed proper access control enforcement
- Attack targeted multiple invalid usernames (automated behavior)
- No successful authentication — unauthorized access was prevented

## Environment

| Detail     | Value                          |
| ---------- | ------------------------------ |
| OS         | Kali Linux                     |
| Platform   | UTM (macOS Host)               |
| Service    | SSH (Port 22)                  |
| Log Source | systemd journal (`journalctl`) |

## Repository Structure

```
├── investigation-report.md     # Full investigation report
├── Scripts/
│   └── ssh_log_parser.py       # Parses auth logs for failed SSH login attempts
├── Screenshots/
│   ├── ssh-service-running.png
│   ├── journalctl-ssh-failed-logins.png
│   ├── journalctl-authentication-failures.png
│   └── failed-attempt-count.png
├── logs/
│   └── sample_auth.log         # Sample authentication log for analysis
└── README.md
```

## Script Usage

```bash
cd Scripts
python3 ssh_log_parser.py
```

The script parses `logs/sample_auth.log` for failed SSH login attempts, groups them by source IP, and flags IPs with 5+ failures as potential brute-force indicators.

## Skills Demonstrated

- SSH service monitoring and log analysis
- Authentication failure detection using `journalctl`
- Brute-force attack pattern recognition
- PAM authentication analysis
- Incident documentation and remediation planning

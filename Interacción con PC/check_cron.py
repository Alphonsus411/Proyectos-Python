#!/usr/bin/env python3

"""
Write a script that checks the system log file and reports if there are any
cron jobs that are not run by root. The script should report the username of
the cron job and the command that is run by the cron job. The script should
report if there are no cron jobs that are not run by root.

"""


import re
import sys

logfile = sys.argv[1]
usernames = []
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        if name != "root":
            usernames.append(name)
        
print(usernames)
        
# Path: Interacción con PC\check_cron.py


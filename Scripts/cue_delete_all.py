#!/usr/bin/env python3
"""
Delete all reminders from cue.txt
Usage: cuedelete_all
"""

import os
from datetime import datetime

REMINDER_FILE = os.path.expanduser("~/Cue/Data/cue.txt")
LOGGING_FILE = os.path.expanduser("~/Cue/Data/cue_deletedReminders.txt")
now = datetime.now().astimezone().isoformat()

if os.path.exists(REMINDER_FILE):
    with open(REMINDER_FILE, "r", encoding="utf-8") as fr:
        lines = [line.strip() for line in fr if line.strip()]

    if lines:
        with open(LOGGING_FILE, "a", encoding="utf-8") as fa:
            fa.write(f"{now} | Deleted all reminders: \n")
            for line in lines:
                fa.write(f" {line}\n")

        with open(REMINDER_FILE, "w", encoding="utf-8"):
            pass
        print("All reminders deleted.")
    else:
        print("No Reminders found to delete.")
else:
    print("No reminders found.")

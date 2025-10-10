#!/usr/bin/env python3
import os
import subprocess

REMINDER_FILE = os.path.expanduser("~/Cue/Data/cue.txt")

if os.path.exists(REMINDER_FILE):
    with open(REMINDER_FILE, "r", encoding='utf-8') as f:
        note = f.read().strip()

    if note:
        subprocess.run([
            "notify-send",
            "Cue Reminder",
            f"Here’s what you planned:\n\n{note}",
            "-u", "normal",       # urgency: low, normal, critical
        ], check=True)

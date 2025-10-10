"""
This script will also help in calling the alias, 'cuedelete'.
"""

import os

REMINDER_FILE = os.path.expanduser("~/Cue/Data/cue.txt")
with open(REMINDER_FILE, "r", encoding="utf-8") as fr:
    for line_read in fr.readlines():
        print(line_read.strip())

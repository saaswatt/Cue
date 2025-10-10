"""
This script will help in calling the alias, 'cueadd'.
"""
#!/usr/bin/env python3
import sys
import os

REMINDER_FILE = os.path.expanduser("~/Cue/Data/cue.txt")
if len(sys.argv) > 1:
    with open(REMINDER_FILE, "a", encoding="utf-8") as f:
        f.write("-" + " ".join(sys.argv[1:]) + "\n")
        print("Added!")
else:
    print("Usage of cueadd: 'cueadd <your reminder>'")

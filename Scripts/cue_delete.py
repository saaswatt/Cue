"""
This script will also help in calling the alias, 'cuedelete'.
"""

import os
import sys
from datetime import datetime

now= datetime.now().astimezone().isoformat()
REMINDER_FILE = os.path.expanduser("~/Cue/Data/cue.txt")
LOGGING_FILE = os.path.expanduser("~/Cue/Data/cue_deletedReminders.txt")
if len(sys.argv) > 1:
    reminder_to_delete= "-"+sys.argv[1].strip()
    FOUND = False

    with open(REMINDER_FILE, "r", encoding="utf-8") as fr:
        lines = fr.readlines()

    with open(REMINDER_FILE, "w", encoding="utf-8") as fw:

        for line in lines:
            line_content = line.strip() #Removes whitespaces/new line.
            # Making sure the user enters valid 'cuedelete' commands, i.e, The text the
            # user wants to delete must be in 'cue.txt' file.
            if line_content == reminder_to_delete:
                FOUND = True
                #Writing the deleted reminders into 'cue_deletedReminders.txt'
                with open(LOGGING_FILE, 'a', encoding="utf-8") as fa:
                    fa.write(now + " | Deleted Reminder: " + line_content + "\n")
                continue
            newLine = line.replace("-" + sys.argv[1], "")
            if newLine.strip():
                fw.write(newLine)
    if FOUND:
        print(f"Deleted Reminder: {sys.argv[1]}.")
    else:
        print(f"Reminder: {sys.argv[1]} not found in reminder file.")
else:
    print("Usage of cuedelete: 'cuedelete <finished reminder>'")

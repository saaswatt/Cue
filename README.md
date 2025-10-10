# 💡 Cue - CLI Reminder & Notification System

![Build Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge)

>**Cue** is a lightweight, Linux-based command-line reminder and notification system developed in Python. It allows users to **popup, add, display, and delete reminders** through a simple CLI interface.

- Key features includes
    - **Automatic pop-up notifications** on user login
    - **Persistent logging** of reminders and user activity
    - **Modular, maintainable code structure** for easy extension

This project showcases **Python scripting, Linux automation, systemd integration, and project organization skills**, making it a strong **portfolio-ready project** for demonstrating practical Linux and automation expertise.

- Table of contents:
    1. **Features**
    2. **Project Architecture**
    3. **Installation**
    4. **Usage**
    5. **Systemd Integration**
    6. **Aliases**
    7. **Data Logging**
    8. **Future Enhancements**

## Features
- **Cue currently supports:**
    - **Add Reminders**  
        Add tasks and notes to `cue.txt` using a simple CLI command.
    - **Display Reminders**  
        View all current reminders directly from the terminal.
    - **Delete specific reminders**  
        Remove a single reminder with proper logging in `cue_deletedReminders.txt`
    - **Delete all reminders**  
        Clear all reminders at once, with timestamped logs for record-keeping.
    - **Popup Notifications**  
        Using `notify-send`, reminders are displayed as a pop-up **automatically on login** via systemd.
    - **Persistent Logging**  
        Deleted reminders are logged with **ISO timestamps** for traceability.
    - **Clean Project Structure**  
        Scripts, data and systemd files are organised into separate folders for maintainability.
    - **CLI Friendly**  
        Designed for terminal-based workflow with aliases for quick commands.

## Project Architecture
- Chronological Order of **files** in the project:

```bash
Cue/                              # Root project directory
├── Scripts/                      # Python scripts
│   ├── cue_add.py                # Add reminders
│   ├── cue_delete.py             # Delete specific reminder
│   ├── cue_delete_all.py         # Delete all reminders
│   ├── cue_display.py            # Display reminders
│   └── cue_popup.py              # Popup notifications
│
├── Data/                         # Persistent data & logs
│   ├── cue.txt                   # Active reminders
│   └── cue_deletedReminders.txt  # Deleted reminders log
│
├── systemd/                      # Optional: systemd service files
│   └── cue_popup.service
│
├── README.md                     # Project documentation
└── .gitignore                    # Files to ignore in Git
```
- **Workflow Diagram**
```bash
[User] --cueadd--> [cue.txt]
[User] --cuedisplay--> [cue.txt] --> Terminal Output
[User] --cuedelete--> [cue.txt] --> Deleted Reminder Logged --> cue_deletedReminders.txt
[cue_popup.py] --systemd--> On Login --> notify-send --> User Notification
```

## Installation
1. **Clone the Repository:**
```bash
git clone https://github.com/saaswatt/Cue.git
cd Cue
```
2. **Create a Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```
3. **Ensure `notify-send` is available:**
```bash
sudo apt install libnotify-bin
```
4. **Set up data folder:**
```bash
mkdir -p ~/Cue/data
touch ~/Cue/data/cue.txt
touch ~/Cue/data/cue_deletedReminders.txt
```

## Usage
#### **Aliases**
- For convenience, add these aliases in your `~/.zshrc` or `~/.bashrc`:
```bash
alias cueadd='python3 ~/Cue/scripts/cue_add.py'
alias cuedelete='python3 ~/Cue/scripts/cue_delete.py'
alias cuedisplay='python3 ~/Cue/scripts/cue_display.py'
alias cuedelete_all='python3 ~/Cue/scripts/cue_delete_all.py'
```
- Then reload:
```bash
source ~/.zshrc
```
or
```bash
source ~/.bashrc
```

## Commands
- **Add a reminder**
```bash
cueadd "Finish SSH-Module for the project"
```
- **Delete a specific reminder**
```bash
cuedelete "Finish SSH-Module for the project"
```
- **Delete all reminders**
```bash
cuedelete_all
```
- **Display reminders**
```bash
cuedisplay
```
## Systemd Integration
- **To have reminders automatically popup at login**:
1. Copy `cue.service` to `~/.config/systemd/user`:
```bash
mkdir -p ~/.config/systemd/user
cp ~/Cue/systemd/cue.service ~/.config/systemd/user/
```
> **Note: Make sure you give absolute path in the `cue.service`**

2. Enable and start the service:
```bash
systemctl --user daemon-reload
systemctl --user enable cue.service
systemctl --user start cue.service
```
> **Note: `cue_popup.py` uses `notify-send`. Make sure your system supports desktop notifications.**

## Data Logging
- **Active Reminders**: `~/Cue/Data/cue.txt`
- **Deleted Reminders Logs**: `~/Cue/Data/cue_deletedreminders.txt`
### Logs Include:
- **ISO TimeStamp**
- **Reminder Text**
- **Action Performed (deleted)**
### Example
```bash
2025-10-06T21:15:30+05:30 | Deleted Reminder: Finish SSH-Module for the project
```
## 📬 Contact
- If you encounter any issues with setup or have suggestions for improvements, feel free to reach out:
- LinkedIn: [Saswat Kumar Pandey](https://www.linkedin.com/in/saswatkumarpandey)
import json
import os
from datetime import datetime

JOURNAL_FILE = ".termiai/journal/actions.jsonl"

def log_action(action, file_path, details=""):
    """Har action ko journal me likhna"""
    os.makedirs(os.path.dirname(JOURNAL_FILE), exist_ok=True)
    
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,  # CREATE, DELETE, EDIT
        "file": file_path,
        "details": details
    }
    
    with open(JOURNAL_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    
    print(f"Logged: {action} - {file_path}")

def read_journal():
    """Journal parhna"""
    if not os.path.exists(JOURNAL_FILE):
        return []
    
    actions = []
    with open(JOURNAL_FILE, "r") as f:
        for line in f:
            actions.append(json.loads(line))
    return actions

def undo_last_action():
    """Akhir action ko undo karna"""
    actions

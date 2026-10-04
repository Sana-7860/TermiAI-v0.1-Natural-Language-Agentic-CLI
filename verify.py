import os
import json

JOURNAL_FILE = ".termiai/journal/actions.jsonl"

def verify_journal():
    """Check karna ke journal sahi hai"""
    if not os.path.exists(JOURNAL_FILE):
        print("Journal file nahi mili - OK for new project")
        return True
    
    try:
        with open(JOURNAL_FILE, "r") as f:
            for i, line in enumerate(f, 1):
                json.loads(line)  # check valid json
        print("Journal verified: All entries OK")
        return True
    except Exception as e:
        print(f"Journal error at line {i}: {e}")
        return False

if __name__ == "__main__":
    verify_journal()

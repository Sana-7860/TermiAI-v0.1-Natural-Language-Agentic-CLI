import os
import shutil
from datetime import datetime

SNAPSHOT_DIR = ".termiai/snapshots"

def create_snapshot():
    """Project ka backup banana"""
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_name = f"snapshot_{timestamp}"
    snapshot_path = os.path.join(SNAPSHOT_DIR, snapshot_name)
    
    # Current dir ka copy
    shutil.copytree(".", snapshot_path, ignore=shutil.ignore_patterns('.termiai', '__pycache__', '.git'))
    print(f"Snapshot created: {snapshot_path}")
    return snapshot_path

def list_snapshots():
    if not os.path.exists(SNAPSHOT_DIR):
        return []
    return os.listdir(SNAPSHOT_DIR)

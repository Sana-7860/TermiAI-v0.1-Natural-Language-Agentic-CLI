# Config and Packaging
# Owner: Sana-7860 - Workstream 6
import json
import os

DEFAULT_CONFIG = {
    "provider": "openai",
    "model": "gpt-4",
    "theme": "dark"
}

def load_config(path="~/.termiai/config.json"):
    full_path = os.path.expanduser(path)
    if os.path.exists(full_path):
        with open(full_path) as f:
            return json.load(f)
    return DEFAULT_CONFIG

def save_config(config, path="~/.termiai/config.json"):
    full_path = os.path.expanduser(path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        json.dump(config, f, indent=2)

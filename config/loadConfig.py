import json
import os

CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "update_interval": 5,
    "logging_enabled": True,
    "buzzer_pin": 21
    }

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as config_file:
            return json.load(config_file)
    else:
        return DEFAULT_CONFIG
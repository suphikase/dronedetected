import json
import loadConfig as CONFIG_FILE

def save_config(config):
    with open(CONFIG_FILE, "w") as config_file:
        json.dump(config, config_file, indent=4)

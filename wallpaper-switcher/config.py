import os
import json

CONFIG_DIR = os.path.expanduser("~/.config/wallpaper-switcher")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
CACHE_DIR = os.path.expanduser("~/.cache/wallpaper-switcher")
MAX_CACHE_SIZE_MB = 500  

def init_dirs():
    os.makedirs(CONFIG_DIR, exist_ok=True)
    os.makedirs(CACHE_DIR, exist_ok=True)

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_config(wallpaper_dir):
    init_dirs()
    config_data = {"wallpaper_dir": wallpaper_dir}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f, indent=2)
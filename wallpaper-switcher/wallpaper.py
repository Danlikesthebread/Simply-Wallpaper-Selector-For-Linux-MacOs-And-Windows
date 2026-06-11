import os
import subprocess
from PyQt6.QtGui import QImageReader

def get_supported_extensions():
    formats = QImageReader.supportedImageFormats()
    exts = set()
    for fmt in formats:
        exts.add(f".{fmt.data().decode().lower()}")
    exts.update(['.jpg', '.jpeg', '.png', '.webp', '.gif'])
    return tuple(exts)

def get_wallpapers(directory):
    if not directory or not os.path.isdir(directory):
        return []
    wallpapers = []
    valid_exts = get_supported_extensions()
    try:
        for file in os.listdir(directory):
            if file.lower().endswith(valid_exts):
                wallpapers.append(os.path.join(directory, file))
    except Exception:
        return []
    return sorted(wallpapers)

def apply_wallpaper(image_path):
    if not os.path.exists(image_path):
        return
    file_uri = f"file://{image_path}"
    subprocess.run(["gsettings", "set", "org.cinnamon.desktop.background", "picture-uri", file_uri], check=False)
    subprocess.run(["gsettings", "set", "org.cinnamon.desktop.background", "picture-uri-dark", file_uri], check=False)
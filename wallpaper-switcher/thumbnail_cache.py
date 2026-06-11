import os
import hashlib
from PIL import Image
from config import CACHE_DIR, MAX_CACHE_SIZE_MB

try:
    RESAMPLE_MODE = Image.Resampling.LANCZOS
except AttributeError:
    RESAMPLE_MODE = Image.LANCZOS

def get_thumbnail_path(image_path):
    try:
        mtime = os.path.getmtime(image_path) if os.path.exists(image_path) else 0
    except OSError:
        mtime = 0
    hash_src = f"{image_path}:{mtime}"
    hash_name = hashlib.md5(hash_src.encode('utf-8')).hexdigest()
    return os.path.join(CACHE_DIR, f"{hash_name}.png")

def create_thumbnail(image_path, width=220, height=124):
    thumb_path = get_thumbnail_path(image_path)
    if os.path.exists(thumb_path):
        return thumb_path
        
    try:
        with Image.open(image_path) as img:
            img.thumbnail((width * 2, height * 2), RESAMPLE_MODE)
            img.save(thumb_path, "PNG")
        return thumb_path
    except Exception:
        return image_path

def prune_cache_lru():
    if not os.path.exists(CACHE_DIR):
        return
    try:
        files = []
        total_size = 0
        for f in os.listdir(CACHE_DIR):
            if f.endswith(".png"):
                fp = os.path.join(CACHE_DIR, f)
                try:
                    stat_res = os.stat(fp)
                    files.append((fp, stat_res.st_atime, stat_res.st_size))
                    total_size += stat_res.st_size
                except OSError:
                    pass
                    
        max_bytes = MAX_CACHE_SIZE_MB * 1024 * 1024
        if total_size > max_bytes:
            files.sort(key=lambda x: x[1])
            for fp, _, fsize in files:
                try:
                    os.remove(fp)
                    total_size -= fsize
                    if total_size <= max_bytes:
                        break
                except OSError:
                    pass
    except Exception:
        pass
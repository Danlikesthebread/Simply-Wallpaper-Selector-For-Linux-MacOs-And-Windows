import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QLockFile, QDir
from config import load_config, init_dirs
from settings import SettingsWindow
from selector import SelectorWindow
from thumbnail_cache import prune_cache_lru

def main():
    app = QApplication(sys.argv)
    
    # Mutex de exclusión mutua para evitar múltiples ejecuciones colgadas
    global instance_lock
    lock_path = os.path.join(QDir.tempPath(), "wallpaper_switcher_v25.lock")
    instance_lock = QLockFile(lock_path)
    if not instance_lock.tryLock(100):
        print("Aviso: Ya existe una instancia de la aplicación activa.")
        return 0
        
    init_dirs()
    
    config = load_config()
    wallpaper_dir = config.get("wallpaper_dir")
    force_settings = "--settings" in sys.argv
    
    prune_cache_lru()
    
    global current_window
    
    if not wallpaper_dir or force_settings:
        current_window = SettingsWindow()
        
        def handle_post_config(selected_path):
            global current_window
            current_window = SelectorWindow(selected_path)
            current_window.show()
            
        current_window.configured.connect(handle_post_config)
        current_window.show()
    else:
        current_window = SelectorWindow(wallpaper_dir)
        current_window.show()
        
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
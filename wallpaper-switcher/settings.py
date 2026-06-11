import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from config import save_config

class SettingsWindow(QWidget):
    configured = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(580, 400)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.container = QWidget(self)
        self.container.setStyleSheet("""
            QWidget {
                background-color: #14121f;
                border: 1px solid rgba(139, 92, 246, 0.25);
                border-radius: 16px;
            }
        """)
        
        container_layout = QVBoxLayout(self.container)
        container_layout.setContentsMargins(35, 35, 35, 35)
        container_layout.setSpacing(20)
        
        title = QLabel("Wallpaper Switcher Config)
        title.setFont(QFont("sans-serif", 16, QFont.Weight.Bold))
        title.setStyleSheet("color: #ffffff; border: none; background: transparent;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container_layout.addWidget(title)
        
        self.btn_select = QPushButton("Seleccionar carpeta de fondos")
        self.btn_select.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_select.setStyleSheet("""
            QPushButton { 
                background-color: #ffffff; 
                color: #14121f; 
                border: none; 
                padding: 12px; 
                border-radius: 8px;
                font-size: 13px; 
                font-weight: bold; 
            }
            QPushButton:hover { background-color: #e2e0f0; }
        """)
        self.btn_select.clicked.connect(self.select_folder)
        container_layout.addWidget(self.btn_select)
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(base_dir, "main.py")
        
        shortcut_info = QLabel(
            "<span style='color: #94a3b8;'>Configura el atajo en Cinnamon dirigiéndote a:</span><br>"
            "<span style='color: #ffffff;'>Configuración de Sistema → Teclado → Atajos → Personalizados</span><br><br>"
            "<span style='color: #94a3b8;'>Comando de ejecución:</span><br>"
            f"<code style='color: #f1f5f9; background-color: rgba(255, 255, 255, 0.08); padding: 4px 8px; border-radius: 4px;'>python3 {script_path}</code>"
        )
        shortcut_info.setStyleSheet("color: #94a3b8; line-height: 1.5; border: none; background: transparent;")
        shortcut_info.setFont(QFont("sans-serif", 10))
        shortcut_info.setWordWrap(True)
        container_layout.addWidget(shortcut_info)
        
        layout.addWidget(self.container)
        self.center_window()

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta", os.path.expanduser("~"))
        if folder:
            save_config(folder)
            self.configured.emit(folder)
            self.close()

    def center_window(self):
        geo = self.frameGeometry()
        geo.moveCenter(self.screen().availableGeometry().center())
        self.move(geo.topLeft())

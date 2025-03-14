from pathlib import Path

import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow, QWidget


class StartupWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        # Set window settings
        self.setGeometry(PyQt5.QtWidgets.QDesktopWidget().screenGeometry().width() // 2 - 400,
                         PyQt5.QtWidgets.QDesktopWidget().screenGeometry().height() // 2 - 300,
                         800,
                         600)

        # add logo
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(str(Path("logo.png"))))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 0, 800, 600)
        
        # scale down image
        self.label.setScaledContents(True)

        # blur image
        self.Blur = PyQt5.QtWidgets.QGraphicsBlurEffect()
        self.Blur.setBlurRadius(128)
        self.label.setGraphicsEffect(self.Blur)

        # Show window
        self.show()

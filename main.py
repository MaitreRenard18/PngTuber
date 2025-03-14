import sys

from PyQt5.QtWidgets import QApplication

from classes.avatar import Avatar
from classes.manager import AvatarManager
from classes.startwindow import StartupWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    pablo = Avatar("pablo", "Pablo")
    pablo.show()

    pablo_manager = AvatarManager(pablo)
    pablo_manager.show()
    
    # start_window = StartupWindow()
    app.exec_()

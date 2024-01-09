import sys

from PyQt5.QtWidgets import QApplication

from classes.avatar import Avatar
from classes.manager import AvatarManager

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    pablo = Avatar("pablo", "Pablo")
    pablo.show()

    pablo_manager = AvatarManager(pablo)
    pablo_manager.show()
    
    app.exec_()

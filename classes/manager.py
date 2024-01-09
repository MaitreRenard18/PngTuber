from threading import Thread

from PyQt5.QtWidgets import QPushButton, QWidget


class AvatarManager(QWidget):
    def __init__(self, avatar):
        super().__init__()
        self.avatar = avatar

        self.setWindowTitle(f"{self.avatar.avatar_name} Manager")

        # Set up accessories
        self.accessories = ["None", "Cat ears", "Sombrero", "Glasses", "Halo"]
        self.setGeometry(0, 0, 5 + len(self.accessories) * 95, 100)
        for i, v in enumerate(self.accessories):
            button = QPushButton(v, self)
            button.setGeometry(0, 0, 90, 90)
            button.move(5 + i * 95, 5)
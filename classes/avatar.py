from pathlib import Path
from threading import Thread
from time import sleep

import numpy as np
import pyaudio
import PyQt5
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow


class Avatar(QMainWindow):
    def __init__(self, avatar, avatar_name="VTuber") -> None:
        super().__init__()
        self.avatar_name = avatar_name

        # Window settings
        self.setWindowTitle(self.avatar_name)
        self.setWindowFlag(PyQt5.QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(PyQt5.QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(PyQt5.QtCore.Qt.WA_TranslucentBackground)
        
        # Add pablo to window
        self.scale_factor = .15

        self.label = QLabel(self)
        self.pablo = QPixmap(str(Path(f"avatars/{avatar}.png")))
        self.label.setPixmap(self.pablo)

        self.pablo_size = (0, 0, int(self.pablo.width() * self.scale_factor), int(self.pablo.height() * self.scale_factor))

        self.label.setGeometry(*self.pablo_size)
        self.label.setScaledContents(True)
        self.pablo_size = (0, 0, self.pablo_size[2], int(self.pablo_size[3] * 1.5))
        self.setGeometry(*self.pablo_size)

        # Move window to bottom right
        self.move(PyQt5.QtWidgets.QDesktopWidget().screenGeometry().width() - self.width(),
                  PyQt5.QtWidgets.QDesktopWidget().screenGeometry().height() - self.height() - 64)

        # Move label at bottom of window
        self.label.move(0, self.height() - self.label.height())

        # Add click event
        self.mouse_hold = False
        self.mouse_offset = PyQt5.QtCore.QPoint(0, 0)
        self.label.mousePressEvent = self.on_click
        self.label.mouseReleaseEvent = self.on_click

        # Set up audio recognition
        self.audio_thread = Thread(target=self.listen_for_sound)
        self.audio_thread.start()

        # Set up animation thread
        self.animation_thread = Thread(target=self.animate)
        

    def on_click(self, event) -> None:
        self.mouse_hold = not self.mouse_hold
        self.mouse_offset = event.pos()


    def mouseMoveEvent(self, event) -> None:
        if not self.mouse_hold:
            return 
        
        self.move(event.globalPos() - self.mouse_offset)
    

    def animate(self) -> None:
        # Scales the jump animation to the size of the avatar
        step = (self.label.height() * 20) // 622
        jump_step = (self.label.height() * 2) // 622

        # Jump animation
        for _ in range(step):
            self.label.move(0, self.label.y() - jump_step)
            sleep(0.01)

        for _ in range(step):
            self.label.move(0, self.label.y() + jump_step)
            sleep(0.01)


    def is_sound(self, frame, threshold = 150) -> bool:
        energy = np.sum(np.abs(frame)) / len(frame)
        return energy > threshold


    def listen_for_sound(self) -> None:
        CHUNK = 1024
        
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNK)

        while True:
            # Read audio data
            data = stream.read(CHUNK)
            frame = np.frombuffer(data, dtype=np.int16)

            # Check if sound is loud enough
            if self.is_sound(frame) and not self.animation_thread.is_alive():
                    self.animation_thread = Thread(target=self.animate)
                    self.animation_thread.start()

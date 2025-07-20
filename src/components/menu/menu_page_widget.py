# from PySide6.QtWidgets import QWidget, QVBoxLayout
# from PySide6.QtCore import QTimer

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QPushButton, QVBoxLayout, QStackedWidget
)
from PySide6.QtCore import QTimer, QTime
import sys

class MenuPageWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        label = QLabel("Welcome to Desktop Assistant!")
        button = QPushButton("Go to Time Page")
        button.clicked.connect(switch_to_time_page)
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)
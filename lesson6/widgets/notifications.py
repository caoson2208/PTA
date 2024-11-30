from PyQt6.QtWidgets import QMessageBox
from PyQt6 import uic

class MessageBox(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lỗi")
        self.setIcon(QMessageBox.Icon.Warning)
        self.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
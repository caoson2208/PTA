from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys

class Login(QMainWindow):
    def __init__(self):
        super().__init__() #super gọi lên thằng cha
        uic.loadUi("./lesson5/ui/login.ui", self)


if __name__ == "__main__":  
    app = QApplication(sys.argv) # Tạo đối tượng QApplication từ lớp QApplication
    window = Login() # Tạo đối tượng Login từ lớp Login
    window.show() # Hiển thị UI
    app.exec()
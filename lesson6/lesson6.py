from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys

class Login(QMainWindow):
    def __init__(self):
        super().__init__() #super gọi lên thằng cha
        uic.loadUi("./lesson6/ui/register.ui", self)


if __name__ == "__main__":  
    app = QApplication(sys.argv) 
    window = Login() 
    window.show() 
    app.exec()
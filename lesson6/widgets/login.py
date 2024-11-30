from PyQt6.QtWidgets import QApplication, QMainWindow
from notifications import MessageBox
from PyQt6 import uic
import sys

class Login(QMainWindow):
    def __init__(self):
        super().__init__() #super gọi lên thằng cha
        self.ui = uic.loadUi("./lesson6/ui/login.ui", self)

        self.ui.btnLogin.clicked.connect(self.check_login)
        self.msg_box = MessageBox()

    def check_login(self):
        
        email = self.ui.txtEmail.text()
        password = self.ui.txtPassword.text()

        if not email:
            self.msg_box.setText("Vui lòng nhập email!")
            self.msg_box.exec()
            return
        if not password:
            self.msg_box.setText("Vui lòng nhập mật khẩu!")
            self.msg_box.exec()
            return
      

if __name__ == "__main__":  
    app = QApplication(sys.argv) 
    window = Login() 
    window.show() 
    app.exec()
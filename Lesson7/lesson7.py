from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6 import uic
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super gọi lên thằng cha
        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        self.setCentralWidget(button)
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked) 
        button.clicked.connect(self.the_button_was_toggle) 

    def the_button_was_clicked(self): 
        print("Clicked!")

    def the_button_was_toggle(self, checked): 
        print("Checked?", checked)

class MessageBox(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lỗi")
        self.setIcon(QMessageBox.Icon.Warning)
        self.setText("Vui lòng nhập email hoặc số điện thoại")
        self.setStyleSheet("background-color: #F8F2EC; color: #356a9c")        

if __name__ == "__main__":  
    app = QApplication(sys.argv) 
    # window = MainWindow() 
    # window.show() 
    # app.exec()
    msg_box = MessageBox()
    sys.exit(msg_box.exec())
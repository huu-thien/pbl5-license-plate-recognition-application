
# import sys
# from PyQt5.uic import loadUi
# from PyQt5 import QtWidgets, uic
# from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QVBoxLayout, QMainWindow
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow, QMessageBox
import MySQLdb as mdb
from main import Main
from register import RegisterScreen

# Cửa sổ login
class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('E:/BKDN/Season_3_Term_2/PBL5/pbl5_app/PBL5-Car-Lisence-Plate-Recognition-Application-v2/My-App-PBL5/UI/login.ui', self)
        self.btnLogin.clicked.connect(self.checkLogin)
        self.btnRegister.clicked.connect(self.checkRegister)
    def checkRegister(self):
        dialog = RegisterScreen()
        if dialog.exec_():
            self.checkRegister()
    def checkLogin(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        # password1 = self.txtPassword1.text()
        if not username or not password:
            QMessageBox.warning(self, "Lỗi", "Please fill in your login details !")
            return
        # if password == password1 :
        db = mdb.connect('localhost', 'root', '', 'pbl5_db')
        query = db.cursor()
        query.execute("SELECT * FROM account WHERE username = '" + username+"' and password = '" + password +"'")
        check = query.fetchone()
        if check:
            try:
                # self.form = LoadUser()
                # self.form.show()
                self.form = Main()
                self.form.show()
            except Exception as e:
                print(f"Lỗi: {str(e)}")
            self.close()
        else:
            QMessageBox.information(self, "Lỗi", "Login unsuccessful !!")
if __name__ == '__main__':
    app = QApplication([])
    login = LoginScreen()
    login.show()
    app.exec_()
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow, QMessageBox
import MySQLdb as mdb

class RegisterScreen(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('E:/BKDN/Season_3_Term_2/PBL5/pbl5_app/PBL5-Car-Lisence-Plate-Recognition-Application-v2/My-App-PBL5/UI/register.ui', self)
        self.btnRegister.clicked.connect(self.checkRegister)
        self.btnCancelRes.clicked.connect(self.reject)


    def checkRegister(self):
       username = self.txtUsername.text()
       password = self.txtPassword.text()
       password1 = self.txtPassword1.text()
       if not username or not password:
        QMessageBox.warning(self, "Lỗi", "Please complete registration information !!")
        return
       if password == password1 :
            db = mdb.connect('localhost', 'root', '', 'pbl5_db')
            query = db.cursor()
            try:
                 query.execute("INSERT INTO account (username, password) VALUES (%s, %s)", (username, password))
                 if query:
                  print('ok')
                  db.commit()
                  # self.close()
                  QMessageBox.warning(self, "Thành công ", "Successful account registration !!")
                  self.close()
                 else:
                  db.rollback()
                  QMessageBox.warning(self, "Lỗi", "Account registration failed !!")
                 db.close()
            except Exception as e:
                  QMessageBox.warning(self, "Lỗi", "This account has already existed !!")
                  print("Lỗi", e)
       else :
            QMessageBox.warning(self, "Lỗi", "Enter a password that does not match !!")
        

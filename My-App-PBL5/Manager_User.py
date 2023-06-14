from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QFileDialog
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow, QMessageBox,QTableWidget
from PyQt5.QtGui import QPixmap
import MySQLdb as mdb

class AddUser(QtWidgets.QDialog):
    def __init__(self):
        try:
            super().__init__()
            uic.loadUi('E:/BKDN/Season_3_Term_2/PBL5/pbl5_app/PBL5-Car-Lisence-Plate-Recognition-Application-v2/My-App-PBL5/UI/addUser.ui', self)
            self.btnCancel.clicked.connect(self.reject)
            self.btnSave.clicked.connect(self.Add)
            self.btnImagePlate.clicked.connect(self.chooseImagePlate)
            self.btnImageAvatar.clicked.connect(self.chooseImageAvatar)
        except Exception as e:
            print(f"Lỗi: {str(e)}")

    def chooseImagePlate(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Chọn tệp ảnh", "",
                                                   "All Files (*);;Image Files (*.jpg *.png *.jpeg)", options=options)
        if file_name:
            self.txtPlateImage.setText(file_name)

    def chooseImageAvatar(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Chọn tệp ảnh", "",
                                                   "All Files (*);;Image Files (*.jpg *.png *.jpeg)", options=options)
        if file_name:
            self.txtAvatar.setText(file_name)
    def Add(self):
        name = self.txtName.text()
        avatar = (self.txtAvatar.text())
        phoneNumber = (self.txtPhoneNumber.text())
        identityCard = self.txtIdentityCard.text()
        plate = self.txtLicensePlates.text()
        plateImage = self.txtPlateImage.text()
        db = mdb.connect('localhost', 'root', '', 'pbl5_db')
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users ( Name, PhoneNumber, IdentityCard, AvatarUrl, Plate, PlateImage) VALUES ( %s,%s,%s, %s, %s,%s)",
            (name, phoneNumber, identityCard, avatar, plate, plateImage))
        db.commit()
        cursor.close()
        db.close()
        self.accept()



class UpdateUser(QtWidgets.QDialog):
    def __init__(self,Id):
        try:
            super().__init__()
            self.Id= Id
            uic.loadUi('E:/BKDN/Season_3_Term_2/PBL5/pbl5_app/PBL5-Car-Lisence-Plate-Recognition-Application-v2/My-App-PBL5/UI/detailEdituser.ui', self)
            self.btnSave.clicked.connect(self.Update)
            self.btnCancel.clicked.connect(self.reject)
            self.btnImageAvatar.clicked.connect(self.chooseImageAvatar)
            self.btnImagePlate.clicked.connect(self.chooseImagePlate)
            self.Load()
        except Exception as e:
            print(f"Lỗi: {str(e)}")


    def chooseImagePlate(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Chooser Image", "",
                                                   "All Files (*);;Image Files (*.jpg *.png *.jpeg)", options=options)
        if file_name:
            self.txtPlateImage.setText(file_name)

    def chooseImageAvatar(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Chooser Image", "",
                                                   "All Files (*);;Image Files (*.jpg *.png *.jpeg)", options=options)
        if file_name:
            self.txtAvatarUrl.setText(file_name)
    def Load(self):
        try :
            db = mdb.connect('localhost', 'root', '', 'pbl5_db')
            cursor = db.cursor()
            query = "SELECT * FROM users WHERE IdUser = %s"
            values = (self.Id,)
            cursor.execute(query, values)
            row = cursor.fetchone()
            self.txtName.setText(row[1])
            self.txtAvatarUrl.setText(row[2])
            self.txtPhoneNumber.setText(str(row[3]))
            self.txtIdentityCard.setText(str(row[4]))
            self.txtPlateImage.setText(row[5])
            self.txtLicensePlates.setText(row[6])
            # self.lbAvatar.setStyleSheet(f"background-image: url('{ str(row[2])}');")
            # print(f"background-image: url('{ str(row[2])}');")
            self.lbAvatar.setPixmap(QPixmap(f'{ str(row[2])}'))
            self.lbPlate.setPixmap(QPixmap(f'{str(row[5])}'))
            db.commit()
            cursor.close()
            db.close()
            self.accept()
        except Exception as e:
            print(f"Lỗi: {str(e)}")
    def Update(self):
        try :
            name = self.txtName.text()
            avatar = (self.txtAvatarUrl.text())
            phoneNumber = (self.txtPhoneNumber.text())
            identityCard = (self.txtIdentityCard.text())
            plate = self.txtLicensePlates.text()
            plateImage = self.txtPlateImage.text()
            db = mdb.connect('localhost', 'root', '', 'pbl5_db')
            cursor = db.cursor()
            query = "UPDATE users SET Name = %s, PhoneNumber = %s,IdentityCard =%s , AvatarUrl = %s , Plate=%s , PlateImage=%s  WHERE IdUser = %s"
            values = (name, phoneNumber, identityCard, avatar, plate, plateImage, self.Id)
            cursor.execute(query, values)
            db.commit()
            cursor.close()
            db.close()
            self.accept()
        except Exception as e:
            print(f"Lỗi: {str(e)}")

class LoadUser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('E:/BKDN/Season_3_Term_2/PBL5/pbl5_app/PBL5-Car-Lisence-Plate-Recognition-Application-v2/My-App-PBL5/UI/main.ui', self)
        self.ShowListUser()
        self.btnAdd.clicked.connect(self.Add)
        self.btnUpdate.clicked.connect(self.Update)
        self.btnDelUser.clicked.connect(self.Delete)
        self.btnSearchUser.clicked.connect(self.Search)
        self.btnResetUser.clicked.connect(self.Reset)
        self.btnSortUserIncrease.clicked.connect(self.SortIncrease)
        self.btnSortUserDecrease.clicked.connect(self.SortDecrease)
    def ShowListUser(self):
        db = mdb.connect('localhost', 'root', '', 'pbl5_db')
        cursor = db.cursor()
        query = "SELECT *FROM users"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.tableUser.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.tableUser.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
                self.tableUser.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        cursor.close()
        db.close()


    def Add(self):
        dialog = AddUser()
        # true thì show
        if dialog.exec_():
            self.ShowListUser()

    idAction = None
    def Update(self):
           selectedRow = self.tableUser.currentRow()
           if selectedRow >= 0:
               id = self.tableUser.item(selectedRow, 0).text()
               int_id = int(id)
               self.idAction = int_id
               dialog = UpdateUser(self.idAction)
               if dialog.exec_():
                   self.ShowListUser()
           # else:
           #     msgBox = QMessageBox()
           #     msgBox.setText("Please choose user to update !!")
           #     msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
           #     msgBox.setDefaultButton(QMessageBox.No)
           #     msgBox.show()
    def Delete(self):
        try:
            selectedRow = self.tableUser.currentRow()
            if selectedRow >= 0:
                id = self.tableUser.item(selectedRow, 0).text()
                # Hiển thị form
                msgBox = QMessageBox()
                msgBox.setText("Do you want to delele this user ?")
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msgBox.setDefaultButton(QMessageBox.No)
                result = msgBox.exec_()
                if result == QMessageBox.Yes:
                    # Xóa khách hàng khỏi database
                    db = mdb.connect('localhost', 'root', '', 'pbl5_db')
                    cursor = db.cursor()
                    query = "DELETE FROM users WHERE IdUser = %s"
                    id_int = int(id)
                    values = (id_int,)
                    cursor.execute(query, values)
                    db.commit()
                    cursor.close()
                    db.close()
                    self.ShowListUser()
        except Exception as e:
            print(f"Lỗi: {str(e)}")
    def Search(self):
        try:
            input = self.txtSearchUser.text()
            db = mdb.connect('localhost', 'root', '', 'pbl5_db')
            cursor = db.cursor()
            query = "SELECT * FROM Users WHERE Name like '%" +input +"%' or PhoneNumber like '%"+input+"%' or Plate like'%" \
                    +input +"%' or IdentityCard like'%" + input + "%'"
            cursor.execute(query)
            rows = cursor.fetchall()
            self.tableUser.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, val in enumerate(row):
                    self.tableUser.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
                    self.tableUser.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            cursor.close()
            db.close()

        except Exception as e:
            print(f"Lỗi: {str(e)}")

    def Reset(self):
        self.ShowListUser()

    def SortIncrease(self):
        try:
            cbbSelectedValue = self.cbbSortUser.currentText()
            db = mdb.connect('localhost', 'root', '', 'pbl5_db')
            cursor = db.cursor()
            match cbbSelectedValue:
                case "ID":
                    query = "SELECT * FROM Users ORDER BY IdUser ASC"
                case "Name":
                    query = "SELECT * FROM Users ORDER BY Name ASC"
                case "Phone Number":
                    query = "SELECT * FROM Users ORDER BY PhoneNumber ASC"
                case "Lisence Plate":
                    query = "SELECT * FROM Users ORDER BY Plate ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            self.tableUser.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, val in enumerate(row):
                    self.tableUser.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
                    self.tableUser.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            cursor.close()
            db.close()
        except Exception as e:
            print(f"Lỗi: {str(e)}")

    def SortDecrease(self):
        try:
            cbbSelectedValue = self.cbbSortUser.currentText()
            db = mdb.connect('localhost', 'root', '', 'pbl5_db')
            cursor = db.cursor()
            match cbbSelectedValue:
                case "ID":
                    query = "SELECT * FROM Users ORDER BY IdUser DESC"
                case "Name":
                    query = "SELECT * FROM Users ORDER BY Name DESC"
                case "Phone Number":
                    query = "SELECT * FROM Users ORDER BY PhoneNumber DESC"
                case "Lisence Plate":
                    query = "SELECT * FROM Users ORDER BY Plate DESC"
            cursor.execute(query)
            rows = cursor.fetchall()
            self.tableUser.setRowCount(len(rows))
            for i, row in enumerate(rows):
                for j, val in enumerate(row):
                    self.tableUser.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
                    self.tableUser.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            cursor.close()
            db.close()
        except Exception as e:
            print(f"Lỗi: {str(e)}")




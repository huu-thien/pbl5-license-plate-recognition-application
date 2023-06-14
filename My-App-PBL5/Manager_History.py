from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow, QMessageBox,QTableWidget
from PyQt5.QtGui import QPixmap, QImage
import MySQLdb as mdb
import cv2
import numpy as np
from io import BytesIO

class DetailsHistory(QtWidgets.QDialog):
    def __init__(self,Id):
        try:
            super().__init__()
            self.Id= Id
            uic.loadUi('E:/BKDN/Season_3_Term_2/PBL5/pbl5_app/PBL5-Car-Lisence-Plate-Recognition-Application-v2/My-App-PBL5/UI/detailsHistory.ui', self)
            self.Load()
        except Exception as e:
            print(f"Lỗi: {str(e)}")
    def Load(self):
        try :
            db = mdb.connect('localhost', 'root', '', 'pbl5_db')
            cursor = db.cursor()
            query = "SELECT users.Name, users.Plate, history.Time, history.HistoryImage " \
                    "FROM Users INNER JOIN History ON users.IdUser = history.IdUser and history.IdHistory = '" + str(self.Id) +"'"
            cursor.execute(query)
            row = cursor.fetchone()
            self.txtName.setText(str(row[0]))
            self.txtLisencePlate.setText(str(row[1]))
            self.txtTime.setText(str(str(row[2])))
            # Decode the blob data into a numpy array
            frame_bytes = row[3]
            print(frame_bytes)
            buffer = BytesIO(frame_bytes)
            img = np.load(buffer)
            # Convert the numpy array into a QImage
            h, w, ch = img.shape
            print(h," ", w," ", ch)
            print(img.shape)
            q_img = QImage(img.data, w, h, ch * w, QImage.Format_BGR888)
            # Convert the QImage into a QPixmap
            pixmap = QPixmap.fromImage(q_img)
            # Set the QPixmap on a QLabel
            self.label_LicensePicture.setPixmap(pixmap)
            
            db.commit()
            cursor.close()
            db.close()
            self.accept()
        except Exception as e:
            print(f"Lỗi Details: {str(e)}")

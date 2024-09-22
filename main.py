import sys
import time
from tkinter import TRUE
import cv2
#import cv2.cv2 as cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import os
import Connection_manager
import face_training
#from cv2 import face
from threading import Thread
import schedule

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
font = cv2.FONT_HERSHEY_SIMPLEX
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#p1 = Process(target=face_training.train())
th1 = Thread(target=face_training.train, daemon=TRUE)
schedule.every(4).hours.do(face_training.train)


def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


def messagebox(title, message):
    mess = QtWidgets.QMessageBox()
    mess.setWindowTitle(title)
    mess.setText(message)
    mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
    mess.exec_()


def faceDataset(self, face_id, sample):
    face_id += 1
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")

    count = 0
    counta = 0

    path = 'dataSet'
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    for imagePath in imagePaths:
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        # print(id)
        if id == int(face_id):
            counta += 1
            print(counta)

    # start detect your face and take 30 pictures
    while(True):
        ret, img = cam.read()
        try:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except:
            break
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1
            counta += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("dataSet/User." + str(face_id) + '.' +
                        str(counta) + ".jpg", gray[y:y+h, x:x+w])

            # cv2.imshow('image', img)
        cv2.waitKey(1)
        Reg.displayimage(self, img)
        if count >= sample:  # Take "sample" face sample and stop video
            break
    cam.release()


class Reg(QDialog):
    def __init__(self):
        super(Reg, self).__init__()
        loadUi('registrasi.ui', self)
        th2 = Thread(target=scheduler, daemon=True)
        th2.start()

        self.Daftar.clicked.connect(self.regist)
        self.ButtonToAbsen.clicked.connect(self.toAbs)

    def toAbs(self):
        widget.setCurrentIndex(0)
        widget.setWindowTitle('Absensi')

    def regist(self):
        th1 = Thread(target=face_training.train, daemon=True)
        if (self.plainTextEdit_3.toPlainText() == '') and (self.plainTextEdit.toPlainText() == '') and (self.plainTextEdit_2.toPlainText() == ''):
            messagebox("Gagal", "Isi form dengan benar!")
        else:
            nip  = self.plainTextEdit_3.toPlainText()
            nama = self.plainTextEdit.toPlainText()
            dept = self.plainTextEdit_2.toPlainText()

            conMan = Connection_manager.connection()
            row_count = conMan.cur.execute("SELECT MAX(id) FROM karyawan")
            data = conMan.cur.fetchone()
            print(data)
            conMan.disconnect()
            if data[0] != None:
                id = data[0]
            else:
                id = 0
            faceDataset(self, id, 50)

            insert = (nip, nama, dept)
            sql = "INSERT INTO karyawan (nip, name, dept) VALUES (%s, %s, %s)"
            conMan = Connection_manager.connection()
            data = conMan.cur.execute(sql, insert)
            conMan.disconnect()
            if (data):
                messagebox("SUKSES", "Data karyawan tersimpan")
            else:
                messagebox("GAGAL", "Data karyawan gagal tersimpan")

            self.plainTextEdit_3.clear()
            self.plainTextEdit.clear()
            self.plainTextEdit_2.clear()
            self.imglbl.clear()
            time.sleep(0.5)
            th1.start()
            # p1.start()
            # p1.join()

    def displayimage(self, image):
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if (image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(image, image.shape[1], image.shape[0],
                     image.strides[0], qformat)
        img = img.rgbSwapped()
        self.imglbl.setPixmap(QPixmap.fromImage(img))
        self.imglbl.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.imglbl.setScaledContents(True)


class Abs(QMainWindow):
    def __init__(self):
        super(Abs, self).__init__()
        loadUi('absen.ui', self)
        self.ButtonToRegis.clicked.connect(self.toReg)
        self.Konfirmasi.clicked.connect(self.confirm)
        self.Start.clicked.connect(self.absen)
        self.data_absensi.clicked.connect(self.toData)
        th2 = Thread(target=scheduler, daemon=True)
        th2.start()
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 640)
        self.cam.set(4, 480)
        self.cam.release()

    def confirm(self):
        counta = 0
        path = 'dataSet'
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        for imagePath in imagePaths:
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            # print(id)
            if id == int(self.id):
                counta += 1
                print(counta)
        conMan = Connection_manager.connection()
        conMan.cur.execute(
            "SELECT count(*) FROM absensi_karyawan WHERE Tanggal = CURDATE() AND id = %s", self.id)
        data = conMan.cur.fetchone()
        jum = data[0]
        if jum == 0:
            conMan.cur.execute(
                "INSERT INTO absensi_karyawan (id, nip, name, dept, waktu_masuk) VALUES (%s, %s, %s, %s, NOW())", (self.id, self.nip, self.name, self.dept))
            messagebox("SUKSES", "Absen Masuk Berhasil")
        else:
            conMan.cur.execute(
                "UPDATE absensi_karyawan SET waktu_keluar = NOW() WHERE Tanggal = CURDATE() AND id = %s", (self.id))
            messagebox("SUKSES", "Absen Keluar Berhasil")
        self.imglbl.clear()
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        for i in range(5):
            cv2.imwrite("dataSet/User." + str(self.id) + '.' +
                        str(counta) + ".jpg", gray[self.y:self.y+self.h, self.x:self.x+self.w])
            counta += i
        #faceDataset(self, self.id, 5, 2)

    def toReg(self):
        widget.setCurrentIndex(1)
        widget.setWindowTitle('Registrasi')
        if(self.cam.isOpened()):
            self.cam.release()
        self.imglbl.clear()
        self.lblnip.setText('')
        self.lblNama.setText('')
        self.lblDept.setText('')

    def toData(self):
        widget.setCurrentIndex(2)
        widget.setWindowTitle('Data Absensi')

    def displayimage(self, image):
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if (image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(image, image.shape[1], image.shape[0],
                     image.strides[0], qformat)
        img = img.rgbSwapped()
        self.imglbl.setPixmap(QPixmap.fromImage(img))
        self.imglbl.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.imglbl.setScaledContents(True)

    def absen(self):
        conMan = Connection_manager.connection()
        conMan.cur.execute("SELECT * FROM karyawan")
        data = conMan.cur.fetchall()
        conMan.disconnect()
        nips  = ['']
        names = ['']
        depts = ['']
        id = ['']
        if(data):
            for tp in data:
                id.append(tp[0])
                nips.append(tp[1])
                names.append(tp[2])
                depts.append(tp[3])

        ids = len(id)

        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 640)  # set video widht
        self.cam.set(4, 480)  # set video height

        # Define min window size to be recognized as a face

        while True:

            ret, self.img = self.cam.read()

            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            if len(faces) == 0:
                self.lblnip.setText('')
                self.lblNama.setText('')
                self.lblDept.setText('')
            for(self.x, self.y, self.w, self.h) in faces:

                cv2.rectangle(self.img, (self.x, self.y),
                              (self.x+self.w, self.y+self.h), (0, 255, 0), 2)

                ids, confidence = recognizer.predict(
                    gray[self.y:self.y+self.h, self.x:self.x+self.w])

                # Check if confidence is less than 100 ==> "0" is perfect match
                if (confidence < 100):
                    print(ids)
                    self.id = id.index(ids)
                    self.nip  = nips[id.index(ids)]
                    self.name = names[id.index(ids)]
                    self.dept = depts[id.index(ids)]
                    confidence = "  {0}%".format(round(100 - confidence))

                else:
                    self.name = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))

                cv2.putText(self.img, str(self.name), (self.x+5, self.y-5),
                            font, 1, (255, 255, 255), 2)
                cv2.putText(self.img, str(confidence), (self.x+5, self.y+self.h-5),
                            font, 1, (255, 255, 0), 1)
                self.lblnip.setText(self.nip)
                self.lblNama.setText(self.name)
                self.lblDept.setText(self.dept)
            #cv2.imshow('camera', self.img)
            self.displayimage(self.img)
            k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        self.cam.release()

class adminn(QDialog):
    def __init__(self):
        super(adminn, self).__init__()
        loadUi('admin_kar.ui', self)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 100)
        self.btnback.clicked.connect(self.bback)
        self.loaddata()

    def bback(self):
        widget.setCurrentIndex(0)
        widget.setWindowTitle('Absensi')

    def loaddata(self):
        conMan = Connection_manager.connection()
        conMan.cur.execute("Select * from absensi_karyawan")
        data = conMan.cur.fetchall()
        conMan.disconnect()

        self.tableWidget.setRowCount(50)
        tablerow = 0
        for row in data:
            self.tableWidget.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0]))
            )
            self.tableWidget.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1]))
            )
            self.tableWidget.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2]))
            )
            self.tableWidget.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3]))
            )
            self.tableWidget.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4]))
            )
            self.tableWidget.setItem(
                tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5]))
            )
            self.tableWidget.setItem(
                tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6]))
            )
            tablerow += 1



app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
abs = Abs()
reg = Reg()
dta = adminn()
widget.addWidget(abs)
widget.addWidget(reg)
widget.addWidget(dta)
widget.setFixedHeight(420)
widget.setFixedWidth(830)
widget.setWindowTitle('Absensi')
widget.show()

# window = Abs()
# window.setWindowTitle('Absensi')
# window.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
    cv2.destroyAllWindows()
    sys.exit(app.exec_())

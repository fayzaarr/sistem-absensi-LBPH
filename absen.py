# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'absen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 457)
        MainWindow.setStyleSheet("background-color: rgb(20, 114, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imglbl = QtWidgets.QLabel(self.centralwidget)
        self.imglbl.setGeometry(QtCore.QRect(490, 60, 261, 221))
        self.imglbl.setAutoFillBackground(False)
        self.imglbl.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.imglbl.setFrameShape(QtWidgets.QFrame.Panel)
        self.imglbl.setText("")
        self.imglbl.setObjectName("imglbl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 170, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lblnip = QtWidgets.QLabel(self.centralwidget)
        self.lblnip.setGeometry(QtCore.QRect(160, 90, 281, 16))
        self.lblnip.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.lblnip.setText("")
        self.lblnip.setObjectName("lblnip")
        self.lblNama = QtWidgets.QLabel(self.centralwidget)
        self.lblNama.setGeometry(QtCore.QRect(160, 130, 281, 16))
        self.lblNama.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.lblNama.setText("")
        self.lblNama.setObjectName("lblNama")
        self.lblDept = QtWidgets.QLabel(self.centralwidget)
        self.lblDept.setGeometry(QtCore.QRect(160, 170, 281, 16))
        self.lblDept.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.lblDept.setText("")
        self.lblDept.setObjectName("lblDept")
        self.Konfirmasi = QtWidgets.QPushButton(self.centralwidget)
        self.Konfirmasi.setGeometry(QtCore.QRect(250, 230, 75, 23))
        self.Konfirmasi.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.Konfirmasi.setObjectName("Konfirmasi")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(20, 400, 75, 16))
        self.Start.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.Start.setObjectName("Start")
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(130, 400, 75, 16))
        self.Reset.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.Reset.setObjectName("Reset")
        self.data_absensi = QtWidgets.QPushButton(self.centralwidget)
        self.data_absensi.setGeometry(QtCore.QRect(580, 370, 101, 23))
        self.data_absensi.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.data_absensi.setObjectName("data_absensi")
        self.ButtonToRegis = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonToRegis.setGeometry(QtCore.QRect(580, 400, 101, 16))
        self.ButtonToRegis.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.ButtonToRegis.setObjectName("ButtonToRegis")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ABSENSI"))
        self.label_2.setText(_translate("MainWindow", "NIP"))
        self.label_3.setText(_translate("MainWindow", "Nama"))
        self.label_4.setText(_translate("MainWindow", "Departement"))
        self.Konfirmasi.setText(_translate("MainWindow", "Konfirmasi"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.Reset.setText(_translate("MainWindow", "Reset"))
        self.data_absensi.setText(_translate("MainWindow", "Data Absensi"))
        self.ButtonToRegis.setText(_translate("MainWindow", "Halaman Registrasi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

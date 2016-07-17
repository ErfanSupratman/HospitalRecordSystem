# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created: Sat May  7 16:55:18 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PattableQueries import getPatientRecord

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
        
class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.setGeometry(300, 300, 700, 700)
        self.sql_query = QLineEdit()
        self.btn_query = QPushButton("View")
        self.model = QStandardItemModel()
        self.view = QListWidget()


        '''self.label = QtGui.QLabel()
        self.label.setGeometry(QtCore.QRect(20, 90, 111, 21))
        self.label.setText("Reg No:")'''
        self.btn_query.clicked.connect(self.queryProcess)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.sql_query)
        self.verticalLayout.addWidget(self.btn_query)
        self.verticalLayout.addWidget(self.view)
    def queryProcess(self):
        self.model.clear()
        #lists = ['sample','sample','sample','sample','sample','sample','sample','sample','sample','sample','sample','sample','sample','sample','sample','sample','sample','sample','sample','sample',]
        RegistrationNo = str(self.sql_query.text())
        patient = getPatientRecord(RegistrationNo)
        if patient == 0:
            msgData = QMessageBox()
            msgData.setIcon(QMessageBox.Information)
            msgData.setText("This Record has no data!\n please fill out the patient data form.")
            msgData.setWindowTitle("No Patient Data")
            msgData.setStandardButtons(QMessageBox.Ok)
            retval = msgData.exec_()
        #print patient['name']
        #print "Hi"
        #name = "test"
        #write the query here and allow the headernames to be displayed based on result
        #list = writeRawQuery(str(self.sql_query.text()))
        else:
            headerNames=[]
            self.model.setColumnCount(13)
            headerNames.append("Registration No.\t" + patient['regnNo'])
            headerNames.append("Name\t\t" + patient['name'])
            headerNames.append("Address\t\t" + patient['addr'])
            headerNames.append("Age\t\t" + str(patient['age']))
            headerNames.append("DOB\t\t" + str(patient['dob']))
            headerNames.append("Sex\t\t" + patient['sex'])
            headerNames.append("Phone\t\t" + str(patient['phoneNo']))
            headerNames.append("Alias\t\t" + patient['alias'])
            headerNames.append("Occupation\t\t" + patient['occupation'])
            headerNames.append("Con Name\t\t" + patient['conName'])
            headerNames.append("Con Address\t" + patient['conAddr'])
            headerNames.append("Con Phone\t\t" + patient['conPhone'])
            headerNames.append("ID No\t\t" + str(patient['idNos']))
            headerNames.append("nextDateOfVisit\t" + str(patient['nextDateOfVisit']))
            headerNames.append("bloodPressure\t" + str(patient['bloodPressure']))
            headerNames.append("pulseRate\t\t" + str(patient['pulseRate']))
            headerNames.append("bodyTemperature\t" + str(patient['bodyTemperature']))
            headerNames.append("bmi\t\t" + str(patient['bmi']))
            headerNames.append("diagnosis\t\t" + patient['diagnosis'])
            headerNames.append("weight\t\t" + str(patient['weight']))
            #self.model.setHorizontalHeaderLabels(headerNames)
            '''i=0
            for j in range (0,20):
                item = QStandardItem(lists[j])
                self.model.setItem(i, j, item)
            self.view.setModel(self.model)
            self.label = QtGui.QLabel(self)
            self.label.setGeometry(QtCore.QRect(390, 400, 111, 21))
            print "ok"
            self.label.setText("Reg No:")'''
            self.view.addItems(headerNames)

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName(_fromUtf8("MainMenu"))
        MainMenu.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainMenu)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 781, 141))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 110, 271, 281))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("yikg7d5eT.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 490, 131, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 490, 121, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 490, 111, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 490, 111, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 490, 111, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 390, 471, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Roman No9 L"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainMenu)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainMenu.setStatusBar(self.statusbar)
        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(_translate("MainMenu", "Main Menu", None))
        self.label.setText(_translate("MainMenu", "WELCOME TO MANAPPARAI GENERAL HOSPITAL!", None))
        self.pushButton.setText(_translate("MainMenu", "New Patient Record", None))

        self.pushButton_2.setText(_translate("MainMenu", "View Records", None))
        self.pushButton_2.clicked.connect(self.on_pushButton_click)

        self.pushButton_3.setText(_translate("MainMenu", "Insert Query", None))
        self.label_3.setText(_translate("MainMenu", "Saving Lives. Every Day. Every Minute.", None))
        

        self.pushButton_4.setText(_translate("MainMenu", "Patient Data", None))
        self.pushButton_5.setText(_translate("MainMenu", "Patient Test Data", None))
        self.dialogTextBrowser = MyDialog(self)
    
    def on_pushButton_click(self):
        self.dialogTextBrowser.exec_()



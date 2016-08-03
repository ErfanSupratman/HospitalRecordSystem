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
        

class viewPatData(QtGui.QDialog):
    def __init__(self, parent=None):
        super(viewPatData, self).__init__(parent)
        
        self.setWindowTitle("View Records")
        self.setGeometry(300, 300, 700, 700)
        self.label = QtGui.QLabel(self)
        self.label.setText("Enter Reg No:")
        self.sql_query = QLineEdit()
        #self.clearFocus()
        #self.sql_query.setPlaceholderText("Enter Reg No here")
        self.label2 = QtGui.QLabel(self)
        self.label2.setText("Enter Date:")
        self.dateEdit = QtGui.QDateEdit()
        self.btn_query = QPushButton("View")
        self.model = QStandardItemModel()
        self.view = QListWidget()

        self.btn_query.clicked.connect(self.viewData)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.sql_query)
        self.verticalLayout.addWidget(self.label2)
        self.verticalLayout.addWidget(self.dateEdit)
        self.verticalLayout.addWidget(self.btn_query)
        self.verticalLayout.addWidget(self.view)

    def viewData(self):
        RegistrationNo = str(self.sql_query.text())
        print "Working"


class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        self.setWindowTitle("View Records")
        self.setGeometry(300, 300, 700, 700)
        self.label = QtGui.QLabel(self)
               
        self.sql_query = QLineEdit()
        self.btn_query = QPushButton("View")
        self.model = QStandardItemModel()
        self.view = QListWidget()
        self.view.clear()
        self.sql_query.clear()
        print "woew"
        self.btn_query.clicked.connect(self.queryProcess)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.sql_query)
        self.verticalLayout.addWidget(self.btn_query)
        self.verticalLayout.addWidget(self.view)

        msgData = QMessageBox()
        msgData.setIcon(QMessageBox.Information)
        msgData.setText("Open App?")
        msgData.setWindowTitle("Manaparai General Hospital")
        msgData.setStandardButtons(QMessageBox.Ok)
        retval = msgData.exec_()

    def queryProcess(self):

        self.model.clear()
        self.view.clear()
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
            if patient:
                headerNames=[]
                self.model.setColumnCount(13)
                headerNames.append("Registration No.\t" + patient[0].regnNo)
                headerNames.append("Name\t\t" + patient[0].name)
                headerNames.append("Address\t\t" + patient[0].addr)
                headerNames.append("Age\t\t" + str(patient[0].age))
                headerNames.append("DOB\t\t" + str(patient[0].dob))
                headerNames.append("Sex\t\t" + patient[0].sex)
                headerNames.append("Phone\t\t" + str(patient[0].phoneNo))
                headerNames.append("Alias\t\t" + patient[0].alias)
                headerNames.append("Occupation\t\t" + patient[0].occupation)
                headerNames.append("Con Name\t\t" + patient[0].conName)
                headerNames.append("Con Address\t" + patient[0].conAddr)
                headerNames.append("Con Phone\t\t" + patient[0].conPhone)
                headerNames.append("ID No\t\t" + str(patient[0].idNos))
                #headerNames.append("nextDateOfVisit\t" + str(patient['nextDateOfVisit']))
                #headerNames.append("bloodPressure\t" + str(patient['bloodPressure']))
                #headerNames.append("pulseRate\t\t" + str(patient['pulseRate']))
                #headerNames.append("bodyTemperature\t" + str(patient['bodyTemperature']))
                #headerNames.append("bmi\t\t" + str(patient['bmi']))
                #headerNames.append("diagnosis\t\t" + patient['diagnosis'])
                #headerNames.append("weight\t\t" + str(patient['weight']))
                headerNames.append("")
                headerNames.append("")
                headerNames.append("")
                self.details = QtGui.QLabel(self)
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.details.setFont(font)
                self.details.setText("Patient Test Details :")
                headerNames.append('Patient Test Detais')
                headerNames.append("~~~~~~~~~~~~~~~~~~~")
                headerNames.append("")
                for patdet in patient[1]:
                    headerNames.append("")
                    headerNames.append("DATE OF VISIT:\t" + str(patdet.dataOfVisit))
                    headerNames.append("~~~~~~~~~~~~~")
                    testDetails = filter(lambda test: test.testDate == patdet.dataOfVisit,patient[2])
                    for test in testDetails:
                        headerNames.append("Test Name\t" + str(test.testName))
                        headerNames.append("Test Results\t" + str(test.testResult))
                        headerNames.append("")    
                    headerNames.append("nextDateOfVisit\t" + str(patdet.nextDateOfVisit))
                    headerNames.append("Blood Pressure\t" + str(patdet.bloodPressure))
                    headerNames.append("Pulse Rate\t" + str(patdet.pulseRate))
                    headerNames.append("Body Temperature\t" + str(patdet.bodyTemperature))
                    headerNames.append("BMI\t" + str(patdet.bmi))
                    headerNames.append("Diagnosis\t" + str(patdet.diagnosis))
                    headerNames.append("Weight\t" + str(patdet.weight))
                
                    
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

        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(800, 490, 131, 41))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

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
        self.pushButton_6.setText(_translate("MainMenu", "View Patient Test Data", None))
        self.pushButton_6.clicked.connect(self.on_pushButton_6_click)
        self.viewPatDataText = viewPatData(self)
        self.dialogTextBrowser = MyDialog(self)
    
    def on_pushButton_click(self):
        self.dialogTextBrowser.exec_()

    def on_pushButton_6_click(self):
        self.viewPatDataText.exec_()





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
from PattableQueries import getPatientRecords,getAllRecordsByName

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


class viewRecord(QtGui.QDialog):
    def __init__(self, parent=None):
        super(viewRecord, self).__init__(parent)

        self.setWindowTitle("View Records")
        self.setGeometry(300, 300, 700, 700)
        self.label = QtGui.QLabel(self)
        self.radio_name = QtGui.QRadioButton("Name")
        self.radio_regno = QtGui.QRadioButton("Registration No")
        self.radio_date = QtGui.QRadioButton("Date")
        #self.label.setText("Enter Name Or Registration Number:")
               
        self.sql_query = QtGui.QLineEdit()
        self.btn_query = QPushButton("View")
        self.model = QStandardItemModel()
        self.view = QListWidget()
        self.view.clear()
        self.sql_query.clear()
        
        self.leftlist = QListWidget ()
        self.leftlist.insertItem (0, 'Name' )
        self.leftlist.insertItem (1, 'Registration No' )
        self.leftlist.insertItem (2, 'Date' )

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()

        self.changeWidgetName()
        self.changeWidgetRegno()
        self.changeWidgetDate()

        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.stack1)
        self.Stack.addWidget (self.stack2)
        self.Stack.addWidget (self.stack3)
        
        self.btn_query.clicked.connect(self.queryProcess)
        self.leftlist.currentRowChanged.connect(self.display)
        
        #self.horizontalLayout = QtGui.QHBoxLayout()
        #self.horizontalLayout.addWidget(self.radio_name)
        #self.horizontalLayout.addWidget(self.radio_regno)
        #self.horizontalLayout.addWidget(self.radio_date)

        self.grid = QtGui.QGridLayout(self)

        self.hbox = QtGui.QHBoxLayout(self)
        self.hbox.addWidget(self.leftlist)
        self.hbox.addWidget(self.Stack)

        self.grid.addLayout(self.hbox, 0, 0)
        self.grid.addWidget(self.btn_query, 1, 0)
        self.grid.addWidget(self.view, 2, 0)


        msgData = QMessageBox()
        msgData.setIcon(QMessageBox.Information)
        msgData.setText("Open App?")
        msgData.setWindowTitle("Manaparai General Hospital")
        msgData.setStandardButtons(QMessageBox.Ok)
        retval = msgData.exec_()


    def closeEvent(self, event):
        self.view.clear()
        self.sql_query.clear()

    def changeWidgetName(self):
        layout = QFormLayout()
        layout.addRow("Enter Name",QLineEdit())
        self.stack1.setLayout(layout)
    def changeWidgetRegno(self):
        layout = QFormLayout()
        layout.addRow("Enter Reg No",QLineEdit())
        self.stack2.setLayout(layout)
    def changeWidgetDate(self):
        layout = QFormLayout()
        layout.addRow("Enter Start Date",QDateEdit())
        layout.addRow("Enter End Date",QDateEdit())
        self.stack3.setLayout(layout)
    def display(self,i):
        self.Stack.setCurrentIndex(i)
        
    def queryProcess(self):
        print self.leftlist.currentRow()
        self.model.clear()
        self.view.clear()
        RegistrationNo = str(self.sql_query.text())
        patient = getPatientRecords(RegistrationNo)
        if not patient:
            msgData = QMessageBox()
            msgData.setIcon(QMessageBox.Information)
            msgData.setText("This Record has no data!\n please fill out the patient data form.")
            msgData.setWindowTitle("No Patient Data")
            msgData.setStandardButtons(QMessageBox.Ok)
            retval = msgData.exec_()
        else:
            if patient[3] == 0:
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
                headerNames.append("Con Address\t\t" + patient[0].conAddr)
                headerNames.append("Con Phone\t\t" + patient[0].conPhone)
                headerNames.append("ID No\t\t" + str(patient[0].idNos))
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
                
                self.view.addItems(headerNames)
            else:
                headerNames=[]
                self.model.setColumnCount(13)
                headerNames.append('MATCHING RECORDS CONTAINING THE KEYWORD (for name) : '+RegistrationNo)
                headerNames.append("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                headerNames.append("")
                for pat in patient[0]:
                    headerNames.append("Registration No.\t" + pat.regnNo)
                    headerNames.append("Name\t\t" + pat.name)
                    headerNames.append("Address\t\t" + pat.addr)
                    headerNames.append("Age\t\t" + str(pat.age))
                    headerNames.append("DOB\t\t" + str(pat.dob))
                    headerNames.append("Sex\t\t" + pat.sex)
                    headerNames.append("Phone\t\t" + str(pat.phoneNo))
                    headerNames.append("Alias\t\t" + pat.alias)
                    headerNames.append("Occupation\t\t" + pat.occupation)
                    headerNames.append("Con Name\t\t" + pat.conName)
                    headerNames.append("Con Address\t\t" + pat.conAddr)
                    headerNames.append("Con Phone\t\t" + pat.conPhone)
                    headerNames.append("ID No\t\t" + str(pat.idNos))
                    headerNames.append("")
                    headerNames.append("")
                    headerNames.append("")
                self.details = QtGui.QLabel(self)
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
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
        self.dialogTextBrowser = viewRecord(self)
    
    def on_pushButton_click(self):
        self.dialogTextBrowser.exec_()

    def on_pushButton_6_click(self):
        self.viewPatDataText.exec_()





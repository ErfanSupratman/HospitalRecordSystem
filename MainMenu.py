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
from PattableQueries import getPatientRecords,getAllRecordsByName,getAllPatientRecordsByDate


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
        self.sql_query_name = QtGui.QLineEdit()
        layout.addRow("Enter Name",self.sql_query_name)
        self.stack1.setLayout(layout)
    def changeWidgetRegno(self):
        layout = QFormLayout()
        self.sql_query_regno = QtGui.QLineEdit()
        layout.addRow("Enter Reg No",self.sql_query_regno)
        self.stack2.setLayout(layout)
    def changeWidgetDate(self):
        layout = QFormLayout()
        self.sql_query_date1 = QtGui.QDateEdit()
        self.sql_query_date2 = QtGui.QDateEdit()
        layout.addRow("Enter Start Date",self.sql_query_date1)
        layout.addRow("Enter End Date",self.sql_query_date2)
        self.stack3.setLayout(layout)
    def display(self,i):
        self.Stack.setCurrentIndex(i)
        
    def queryProcess(self):
        self.model.clear()
        self.view.clear()
        print self.leftlist.currentRow()
        searchConstraint = self.leftlist.currentRow()
        #remaind the user to select a constraint
        if searchConstraint == -1:
            msgData = QMessageBox()
            msgData.setIcon(QMessageBox.Information)
            msgData.setText("Please select a constraint.")
            msgData.setWindowTitle("No Constraint selected")
            msgData.setStandardButtons(QMessageBox.Ok)
            retval = msgData.exec_()
        elif searchConstraint == 0:
            patientName = self.sql_query_name.text()
            #print patientName
            patients = getAllRecordsByName(patientName)
            #print patients
            if patients != None:  
                for patient in patients:
                    headerNames=[]
                    self.model.setColumnCount(13)
                    headerNames.append("Registration No.\t" + patient.regnNo)
                    headerNames.append("Name\t\t" + patient.name)
                    headerNames.append("Address\t\t" + patient.addr)
                    headerNames.append("Age\t\t" + str(patient.age))
                    headerNames.append("DOB\t\t" + str(patient.dob))
                    headerNames.append("Sex\t\t" + patient.sex)
                    headerNames.append("Phone\t\t" + str(patient.phoneNo))
                    headerNames.append("Alias\t\t" + patient.alias)
                    headerNames.append("Occupation\t\t" + patient.occupation)
                    headerNames.append("Con Name\t\t" + patient.conName)
                    headerNames.append("Con Address\t\t" + patient.conAddr)
                    headerNames.append("Con Phone\t\t" + patient.conPhone)
                    headerNames.append("ID No\t\t" + str(patient.idNos))
                    headerNames.append("")
                    headerNames.append("")
                    headerNames.append("")
                    self.view.addItems(headerNames)
            else:
                msgData = QMessageBox()
                msgData.setIcon(QMessageBox.Information)
                msgData.setText("No records found with the given name!")
                msgData.setWindowTitle("No match")
                msgData.setStandardButtons(QMessageBox.Ok)
                retval = msgData.exec_()
        elif searchConstraint == 1:
            regNo = self.sql_query_regno.text()
            patientDetails,patientData,testData = getPatientRecords(regNo)
            print patientDetails
            print patientData
            if patientDetails != None:
                headerNames=[]
                self.model.setColumnCount(13)
                headerNames.append("Registration No.\t" + patientDetails.regnNo)
                headerNames.append("Name\t\t" + patientDetails.name)
                headerNames.append("Address\t\t" + patientDetails.addr)
                headerNames.append("Age\t\t" + str(patientDetails.age))
                headerNames.append("DOB\t\t" + str(patientDetails.dob))
                headerNames.append("Sex\t\t" + patientDetails.sex)
                headerNames.append("Phone\t\t" + str(patientDetails.phoneNo))
                headerNames.append("Alias\t\t" + patientDetails.alias)
                headerNames.append("Occupation\t\t" + patientDetails.occupation)
                headerNames.append("Con Name\t\t" + patientDetails.conName)
                headerNames.append("Con Address\t\t" + patientDetails.conAddr)
                headerNames.append("Con Phone\t\t" + patientDetails.conPhone)
                headerNames.append("ID No\t\t" + str(patientDetails.idNos))
                headerNames.append("")
                headerNames.append("")
                if patientData != None:
                    for visit in patientData:
                        headerNames.append("Date Of Visit: \t"+str(visit.dataOfVisit))
                        headerNames.append("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        headerNames.append("nextDateOfVisit\t" + str(visit.nextDateOfVisit))
                        headerNames.append("Blood Pressure\t" + str(visit.bloodPressure))
                        headerNames.append("Pulse Rate\t" + str(visit.pulseRate))
                        headerNames.append("Body Temperature\t" + str(visit.bodyTemperature))
                        headerNames.append("BMI\t" + str(visit.bmi))
                        headerNames.append("Diagnosis\t" + str(visit.diagnosis))
                        headerNames.append("Weight\t" + str(visit.weight))
                        headerNames.append("")
                        testDetails = filter(lambda test: test.testDate == visit.dataOfVisit,testData)
                        if len(testDetails):
                            for test in testDetails:
                                headerNames.append("Test Name\t" + str(test.testName))
                                headerNames.append("Test Results\t" + str(test.testResult))
                                headerNames.append("")
                        else:
                                headerNames.append("No Test were taken on "+str(visit.dataOfVisit))
                                headerNames.append("")
                else:
                    headerNames.append("")
                    headerNames.append("No data history available for the given Registration number") 
                headerNames.append("")
                headerNames.append("")
                self.view.addItems(headerNames)
            else:
                msgData = QMessageBox()
                msgData.setIcon(QMessageBox.Information)
                msgData.setText("No matching record with the given Registration No.")
                msgData.setWindowTitle("No match")
                msgData.setStandardButtons(QMessageBox.Ok)
                retval = msgData.exec_()
        else:
            startDate = (self.sql_query_date1.date()).toPyDate()
            endDate = (self.sql_query_date2.date()).toPyDate()
            patients = getAllPatientRecordsByDate(startDate,endDate)
            print patients
            if patients != None:
                for patient in patients:
                    headerNames=[]
                    self.model.setColumnCount(13)
                    headerNames.append("Registration No. : \t" + patient.regnNo.regnNo)
                    headerNames.append("Name : \t\t" + patient.regnNo.name)
                    headerNames.append("Date Of Visit : \t\t" + str(patient.dataOfVisit))
                    headerNames.append("")
                    headerNames.append("")
                    headerNames.append("")
                    self.view.addItems(headerNames)	
            else:
                msgData = QMessageBox()
                msgData.setIcon(QMessageBox.Information)
                msgData.setText("No records with the given Range!")
                msgData.setWindowTitle("No matches")
                msgData.setStandardButtons(QMessageBox.Ok)
                retval = msgData.exec_()
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





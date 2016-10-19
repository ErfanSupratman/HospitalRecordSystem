#!/usr/bin/python
import sys
import time
import datetime
import PatientEntryForm
import PatientDataForm
import PatientTestDataForm
import FormValidator
import MainMenu

from PyQt4 import QtGui,QtCore,QtSql
from PatientEntryForm import Ui_PatientEntryForm
from PatientDataForm import Ui_PatientDataForm
from PatientTestDataForm import Ui_PatientTestDataForm
from MainMenu import Ui_MainMenu
from PattableQueries import insertPatientDetails,insertPatientData,insertTestData,writeRawQuery
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Hospital_Database import PatTable
from peewee import *


#function to increment regno in the PatTable
def regno():
    db = MySQLDatabase('hospitalDB', user='test', password='test', host='localhost')
    db.connect()
    count = PatTable.select().count()
    db.close()
    return count+1;


class Queryer(QWidget):

    #static lists containing column names for patTable and patData
    patTableHeaderNames=["Registration No.", "Name", "Address", "Age", "DOB", "Sex", "Phone",
    "Alias", "Occupation", "Con Name", "Con Address", "Con Phone", "ID No", "Con RTP"]

    patDataHeaderNames=["Registration No.", "Unix time", "Next Visit Date", "Blood Pressure", "Pulse Rate",
    "Body temp.", "BMI", "Diagnosis", "Weight"]

    def __init__(self):
        super(Queryer, self).__init__()
        self.leftlist = QListWidget ()
        self.leftlist.insertItem (1, 'Write Query' )
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.model = QStandardItemModel()
        self.view = QTableView()
        self.label = QtGui.QLabel(self)
        self.label.setText("Enter Your Query:")
        self.sql_query = QLineEdit()
        self.btn_query = QPushButton("Query")
        self.stack2 = QWidget()
        self.stack2UI()
        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.stack2)
                
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)
        
        self.setLayout(hbox)
        #self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 500, 2000,500)
        self.setWindowTitle('Database Query')
        self.show()
      

    def queryProcess(self):
        self.model.clear()
        queryList = []
        queryList = writeRawQuery(str(self.sql_query.text()))

        if queryList:
            self.model.setColumnCount(len(queryList[0]))

            if len(queryList[0]) == len(Queryer.patTableHeaderNames):
                self.model.setHorizontalHeaderLabels(Queryer.patTableHeaderNames)
            elif len(queryList[0]) == len(Queryer.patDataHeaderNames):
                self.model.setHorizontalHeaderLabels(Queryer.patDataHeaderNames)
            
            for d in queryList:
                row=[]
                for name in d:
                    try:
                        item = QStandardItem(str(name))
                        item.setEditable(False)
                        row.append(item)
                    except:
                        continue

                self.model.appendRow(row)

            self.view.setModel(self.model)
        else:
            # Empty result set or invalid query. Case has to be handled
            print "Empty result set or invalid query. Case has to be handled properly"


    def stack2UI(self):
        layout = QVBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.sql_query)
        layout.addWidget(self.btn_query)
        layout.addWidget(self.view)
        self.btn_query.clicked.connect(self.queryProcess)
            
        self.stack2.setLayout(layout)
    
#class for adding newly registering patient     
class Adder(QtGui.QDialog, PatientEntryForm.Ui_PatientEntryForm):
    def __init__(self, parent=None):
        super(Adder, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addRecord)

    def addRecord(self):
        #   m = writeRawQuery('SELECT count(*) from pattable')
        regNumber = regno()
        inputsData = {      
            'Name' : self.plainTextEdit.toPlainText(),
            'RegnNo' : regNumber,
            'Address' : self.plainTextEdit_2.toPlainText(),
            'Age' : self.plainTextEdit_3.toPlainText(),
            'Phone': self.plainTextEdit_4.toPlainText(),
            'Alias' : self.plainTextEdit_5.toPlainText(),
            'Occupation' : self.plainTextEdit_6.toPlainText(),
            'ConName' : self.plainTextEdit_7.toPlainText(),
            'ConAddr' : self.plainTextEdit_8.toPlainText(),
            'ConPhone' : self.plainTextEdit_9.toPlainText(),
            'IDNo' : self.plainTextEdit_10.toPlainText(),
            'ConRelation' : self.plainTextEdit_11.toPlainText(),
            'DOB' : self.dateEdit.date(),
            'SexMale' : self.radio1.isChecked(),
            'SexFemale' : self.radio2.isChecked()
        }

        if inputsData['SexMale'] :
            inputsData['Sex'] = 'M'
        else :
            inputsData['Sex'] = 'F'
        status,message = FormValidator.PatEntryFormValidate(inputsData)
        if status == 1:
            insertPatientDetails(inputsData)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Record has been inserted!\n You Registration number is : "+str(regNumber))
            msg.setWindowTitle("Record Added")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Error! : '+message)
            msg.setWindowTitle("\nRecord Not Added")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
    
#class for adding patient data
class PatientDataAdder(QtGui.QDialog,PatientDataForm.Ui_PatientDataForm):

    def __init__(self, parent=None):
        super(PatientDataAdder, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addData)


    def addData(self):
        inputsData = {      
            'RegNo' : self.plainTextEdit.toPlainText(),
            #'currentUnixTime' is added by default using the datetime object's function 
            'NextDateOfVisit' : self.dateEdit.date(),
            'BloodPressure' : self.plainTextEdit_3.toPlainText(),
            'PulseRate': self.plainTextEdit_4.toPlainText(),
            'BodyTemperature' : self.plainTextEdit_5.toPlainText(),
            'Bmi' : self.plainTextEdit_6.toPlainText(),
            'Diagnosis' : self.plainTextEdit_7.toPlainText(),
            'Weight' : self.plainTextEdit_8.toPlainText()
        }
        status,message = FormValidator.PatDataFormValidate(inputsData)
        if status == 1:
            insertPatientData(inputsData)
            msgData = QMessageBox()
            msgData.setIcon(QMessageBox.Information)
            msgData.setText("Record has been inserted!")
            msgData.setWindowTitle("Record Added")
            msgData.setStandardButtons(QMessageBox.Ok)
            retval = msgData.exec_()    
        else:
            msgData = QMessageBox()
            msgData.setIcon(QMessageBox.Information)
            msgData.setText("Error : "+message)
            msgData.setWindowTitle("\nRecord Not Added")
            msgData.setStandardButtons(QMessageBox.Ok)
            retval = msgData.exec_()                
#class for adding patient result data
class PatientTestDataAdder(QtGui.QDialog,PatientTestDataForm.Ui_PatientTestDataForm):

    def __init__(self, parent=None):
        super(PatientTestDataAdder, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addTestData)


    def addTestData(self):
        inputsData = {      
            'RegNo' : self.plainTextEdit.toPlainText(),
            'TestName' : self.plainTextEdit_2.toPlainText(),
            'TestResult' : self.plainTextEdit_3.toPlainText()
        }
        status,message = FormValidator.PatTestFormValidate(inputsData)
        if status == 1:
            insertTestData(inputsData)
            msgData = QMessageBox()
            msgData.setIcon(QMessageBox.Information)
            msgData.setText("Record has been inserted!")
            msgData.setWindowTitle("Record Added")
            msgData.setStandardButtons(QMessageBox.Ok)
            retval = msgData.exec_()    
        else:
            msgData = QMessageBox()
            msgData.setIcon(QMessageBox.Information)
            msgData.setText("Error : "+message)
            msgData.setWindowTitle("\nRecord Not Added")
            msgData.setStandardButtons(QMessageBox.Ok)
            retval = msgData.exec_()

class HospitalDatabase(QtGui.QMainWindow, MainMenu.Ui_MainMenu):

    def __init__(self, parent=None):
        super(HospitalDatabase, self).__init__(parent)
        #self.Stack = QStackedWidget(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addTheRecord)
        self.getRecord = Adder(self)
        self.pushButton_4.clicked.connect(self.addThePatientData)
        self.getPatientData = PatientDataAdder(self)
        self.pushButton_5.clicked.connect(self.addThePatientTestData)
        self.getPatientTestData = PatientTestDataAdder(self)
        self.pushButton_3.clicked.connect(self.writeQuery)


    @QtCore.pyqtSlot()
    def addTheRecord(self):
        print self.getRecord.exec_()


    @QtCore.pyqtSlot()
    def addThePatientData(self):
        print self.getPatientData.exec_()


    @QtCore.pyqtSlot()
    def addThePatientTestData(self):
        print self.getPatientTestData.exec_()
    

    @QtCore.pyqtSlot()  
    def writeQuery(self):
        #print "Hi"
        self.getQuery = Queryer()
        #print self.getQuery.exec_()


def main():
    app = QtGui.QApplication(sys.argv)
    form = HospitalDatabase()
    form.show()
    app.exec_()
    
    
if __name__ == '__main__':
    main()

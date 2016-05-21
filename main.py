#!/usr/bin/python

from PyQt4 import QtGui,QtCore,QtSql
import sys
import PatientEntryForm
from PatientEntryForm import Ui_PatientEntryForm
import MainMenu
from MainMenu import Ui_MainMenu
from PattableQueries import insertPatient,writeRawQuery
i=0
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Queryer(QWidget):
	def __init__(self):
		super(Queryer, self).__init__()
      		self.leftlist = QListWidget ()
              	self.leftlist.insertItem (1, 'Write Query' )
      
      		self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
      		self.model = QStandardItemModel()
      		self.view = QTableView()
      		
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
   	#try:
   		self.model.clear()
   		list = []
   		list = writeRawQuery(str(self.sql_query.text()))
   		self.model.setColumnCount(13)
   		headerNames=[]
   		headerNames.append("Registration No.")
   		headerNames.append("Name")
   		headerNames.append("Address")
   		headerNames.append("Age")
   		headerNames.append("DOB")
   		headerNames.append("Sex")
   		headerNames.append("Phone")
   		headerNames.append("Alias")
   		#headerNames.append("RegnNo")
   		headerNames.append("Occupation")
   		headerNames.append("Con Name")
   		headerNames.append("Con Address")
   		headerNames.append("Con Phone")
   		headerNames.append("ID No")
   		self.model.setHorizontalHeaderLabels(headerNames)
   		
   		for d in list:
   			row=[]
   			for name in d:
   				try:
   					item = QStandardItem(name)
	   				item.setEditable(False)
	   				row.append(item)
	   			except:
	   				continue
   			
   			self.model.appendRow(row)
		
   		self.view.setModel(self.model)
   		
	   	
    	#except:
    	#	print "Nope. Not Working bruh.."
    		
   
		
	def stack2UI(self):
	      	layout = QVBoxLayout()
      
	      	layout.addWidget(self.sql_query)
	      	layout.addWidget(self.btn_query)
	      	layout.addWidget(self.view)
	      	self.btn_query.clicked.connect(self.queryProcess)
	      	
	      	self.stack2.setLayout(layout)
	
	
class Adder(QtGui.QDialog, PatientEntryForm.Ui_PatientEntryForm):
	def __init__(self, parent=None):
        	super(Adder, self).__init__(parent)
        	self.setupUi(self)
        	self.pushButton.clicked.connect(self.addRecord)

	def addRecord(self):
    		m = writeRawQuery('SELECT count(*) from pattable')
		inputs = { 		
			'Name' : self.plainTextEdit.toPlainText(),
			'RegnNo' : m[0][0]+1,
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
	    		'Sex' : self.Sex.value()
    		}	
    	
	    	insertPatient(inputs['Name'],inputs['Address'],inputs['Age'],inputs['DOB'].day(),inputs['DOB'].month(),inputs['DOB'].year(),inputs['Sex'],
    	inputs['Phone'],inputs['Alias'],inputs['RegnNo'],inputs['Occupation'],inputs['ConName'],inputs['ConAddr'],inputs['ConPhone'],inputs['IDNo'],
    	inputs['ConRelation'])
    	
    		#print "Record Inserted!"
    	
    		msg = QMessageBox()
   		msg.setIcon(QMessageBox.Information)

   		msg.setText("Record has been inserted!")
		msg.setWindowTitle("Record Added")
        	msg.setStandardButtons(QMessageBox.Ok)
   		retval = msg.exec_()
   	
   	
class HospitalDatabase(QtGui.QMainWindow, MainMenu.Ui_MainMenu):
    def __init__(self, parent=None):
        super(HospitalDatabase, self).__init__(parent)
        #self.Stack = QStackedWidget(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addTheRecord)
        self.getRecord = Adder(self)
        
        
        self.pushButton_3.clicked.connect(self.writeQuery)
       
    @QtCore.pyqtSlot()
    def addTheRecord(self):
    	print self.getRecord.exec_()
    
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

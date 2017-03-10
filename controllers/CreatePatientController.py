import peewee
import MySQLdb
from databases.Hospital_Database import PatTable,PatData,TestData
from datetime import date
from views.FormValidator import *

'''
Insert commands for the following tables  - PatTable (patient details)
                                            PatData  (patient data)
'''

#insert the given patient records into the PatTable table
def insertPatientDetails(inputsData):
	insertRecord = PatTable.create(
                name=inputsData['Name'],
                addr=inputsData['Address'],
                age=inputsData['Age'],
                dob=date(inputsData['DOB'].year(),inputsData['DOB'].month(),inputsData['DOB'].day()),
                sex=inputsData['Sex'],
                phoneNo=inputsData['Phone'],
                alias=inputsData['Alias'],
                regnNo=inputsData['RegnNo'],
                occupation=inputsData['Occupation'],
                conName=inputsData['ConName'],
                conAddr=inputsData['ConAddr'],
                conPhone=inputsData['ConPhone'],
                idNos = inputsData['IDNo'],
                conRTP = inputsData['ConRelation']
        )
	print inputsData['ConRelation'],inputsData['IDNo']
	insertRecord.save()

#Insert the given patient data into the PatData table
def insertPatientData(inputsData):
	insertRecord = PatData.create(
                regnNo=inputsData['RegNo'],
                #currentUnixTime=inputsData['currentUnixTime'],
                dataOfVisit=date.today(),
                nextDateOfVisit=date(inputsData['NextDateOfVisit'].year(),inputsData['NextDateOfVisit'].month(),inputsData['NextDateOfVisit'].day()),
                bloodPressure=str(inputsData['BloodPressure']),
                pulseRate=inputsData['PulseRate'],
                bodyTemperature=inputsData['BodyTemperature'],
                bmi=inputsData['Bmi'],
                diagnosis=inputsData['Diagnosis'],
                weight=inputsData['Weight']
        )
	insertRecord.save()

#Insert the given test data into TestData table
def insertTestData(inputsData):
	insertRecord = TestData.create(
                regnNo=inputsData['RegNo'],
                testName=inputsData['TestName'],
                testDate =date.today(),
                testResult=inputsData['TestResult']
        )
	insertRecord.save()

        

#get the required output using raw SQL query
def writeRawQuery(query):
	conn = MySQLdb.connect('localhost', 'test', 'test', 'hospitalDB')
	cursor = conn.cursor()
	try:
		cursor.execute(query)
		data = [row for row in cursor.fetchall()]
		# conn.commit() - Uncomment this if data manipulation through raw SQL is allowed
		conn.close()
		return data
	except:
		conn.close()
		print "Invalid Data"
		return []


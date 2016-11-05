import peewee
import MySQLdb
from Hospital_Database import PatTable,PatData,TestData
from datetime import date
from FormValidator import *

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


#get the patient record by Regno from Pattable & PatData
def getPatientRecords(regnNo):
        patDetails = None
        patData = None
        testData = None
        if PatTable.select().where(PatTable.regnNo == regnNo).exists():
                patDetails = PatTable.get(regnNo = regnNo)
                if PatData.select().where(PatData.regnNo == regnNo).order_by(-PatData.currentUnixTime).exists():
                        patData = PatData.select().where(PatData.regnNo == regnNo).order_by(-PatData.currentUnixTime)
                        if TestData.select().where(TestData.regnNo == regnNo).order_by(-TestData.currentUnixTime).exists():
                                testData = TestData.select().where(TestData.regnNo == regnNo).order_by(-TestData.currentUnixTime)
        return patDetails, patData, testData

#get all the patient records with the same name from PatTable
def getAllRecordsByName(patientName):
        patients = None
        if PatTable.select().where(PatTable.name == patientName).exists():
                patients = PatTable.select().where(PatTable.name == patientName)
        return patients

#get all test records of patient between start date and end date
def getAllPatientRecordsByDate(startDate,endDate):
        patientRecords = None
        if len(PatData.select(PatData.regnNo).where(PatData.dataOfVisit > startDate,PatData.dataOfVisit < endDate)) != 0:
                patientRecords = PatData.select(PatTable.name,PatTable.regnNo,PatData.dataOfVisit).join(PatTable).where(PatData.dataOfVisit > startDate, PatData.dataOfVisit < endDate)
        return patientRecords
        
def getPatientTest(regnNo,dateOfVisit):
	if dateOfVisit != None:
		testDataDetails = TestData.select().where(
                        TestData.regnNo == regnNo,
                        TestData.testDate == dateOfVisit
                )
	else:
		testDataDetails = TestData.select().where(TestData.regnNo == regnNo)
	print testDataDetails[0].testName
	
#get all patients [name,diagnosis] for the given date (query by NextDateOfVisit)
def getPatientsByDate(date = str(date.today())):
        patients = None
        if PatData.select().where(PatData.nextDateOfVisit == date).exists():
                patients = PatData.select(PatTable.regnNo,PatTable.name,PatData.diagnosis).join(PatTable).where(PatData.nextDateOfVisit == date)
        return patients
        
        

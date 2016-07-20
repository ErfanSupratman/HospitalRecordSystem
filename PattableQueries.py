import peewee
import MySQLdb
from Hospital_Database import PatTable,PatData,TestData
from datetime import date
from FormValidator import *

'''
Insert commands for the following tables  - PatTable (patient details)
											PatData  (patient data)
'''

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


def insertPatientData(inputsData):
	insertRecord = PatData.create(
								  regnNo=inputsData['RegNo'],
								  #currentUnixTime=inputsData['currentUnixTime'],
								  nextDateOfVisit=date(inputsData['NextDateOfVisit'].year(),inputsData['NextDateOfVisit'].month(),inputsData['NextDateOfVisit'].day()),
								  bloodPressure=inputsData['BloodPressure'],
								  pulseRate=inputsData['PulseRate'],
								  bodyTemperature=inputsData['BodyTemperature'],
								  bmi=inputsData['Bmi'],
								  diagnosis=inputsData['Diagnosis'],
								  weight=inputsData['Weight']
								 )
	insertRecord.save()


def insertTestData(inputsData):
	insertRecord = TestData.create(
								  regnNo=inputsData['RegNo'],
								  testName=inputsData['TestName'],
								  testDate =date.today(),
								  testResult=inputsData['TestResult']
								 )
	insertRecord.save()

#view
def viewRecordsBetweenDates(sd,sm,sy,ed,em,ey):
	startDate = date(sy,sm,sd)
	endDate = date(ey,em,ed)
	startTime = time.mktime(startDate.timetuple())*1000
	endTime = time.mktime(endDate.timetuple())*1000
	patientRecords = PatTable.select().join(PatData).where(startTime <= PatData.currentUnixTime <= endTime)
	return patientRecords


#query
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

#m = writeRawQuery('SELECT * from pattable')
#for k in m:
#	for j in k:
#		print j	
#		print type(j)

def getPatientRecord(regnNo):
	patTableDetails = PatTable.select().where(PatTable.regnNo == regnNo)
	if patTableDetails.exists():
		patTableDetails = PatTable.get(regnNo = regnNo)
	else:
		return 0;
	patDataDetails = PatData.select().where(PatData.regnNo == regnNo)
	if patDataDetails.exists():
		patDataDetails = PatData.get(regnNo = regnNo)
		patientDetails = {	
						'regnNo' : patTableDetails.regnNo,
						'name' :  patTableDetails.name,
						'addr' : patTableDetails.addr,
						'age' : patTableDetails.age,
						'dob' : patTableDetails.dob,
						'sex' : patTableDetails.sex,
						'phoneNo' : patTableDetails.phoneNo,
						'alias' :patTableDetails.alias,
						'occupation' : patTableDetails.occupation,
						'conName' : patTableDetails.conName,
						'conAddr' : patTableDetails.conAddr,
						'conPhone' : patTableDetails.conPhone,
						'idNos' : patTableDetails.idNos,
						'nextDateOfVisit' : patDataDetails.nextDateOfVisit,
						'bloodPressure' : patDataDetails.bloodPressure,
						'pulseRate' : patDataDetails.pulseRate,
						'bodyTemperature' : patDataDetails.bodyTemperature,
						'bmi' : patDataDetails.bmi,
						'diagnosis' : patDataDetails.diagnosis,
						'weight' : patDataDetails.weight 
						}
		return patientDetails
	else:
		return 0

def getPatientTest(regnNo,dateOfVisit):
	if dateOfVisit != None:
		testDataDetails = TestData.select().where(
												  TestData.regnNo == regnNo,
									   			  TestData.testDate == dateOfVisit
									   			  )
	else:
		testDataDetails = TestData.select().where(TestData.regnNo == regnNo)
	print testDataDetails[0].testName
	
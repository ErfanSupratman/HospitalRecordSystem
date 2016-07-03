import peewee
import sqlite3
from Hospital_Database import PatTable,PatData
from datetime import date


'''
Insert commands for the following tables  - PatTable (patient details)
											PatData  (patient data)
'''

def insertPatientDetails(name,addr,age,D,M,Y,sex,phoneNo,alias,regnNo,occupation,conName,conAddr,conPhone,idNos,conRTP):
	insertRecord = PatTable.create(name=name,addr=addr,age=age,dob=date(Y,M,D),sex=sex,phoneNo=phoneNo,alias=alias,regnNo=regnNo,
	occupation=occupation,conName=conName,conAddr=conAddr,conPhone=conPhone,idNos = idNos,conRTP = conRTP)
	insertRecord.save()

=======
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
								  testResult=inputsData['TestResult']
								 )
	insertRecord.save()
>>>>>>> 04aa370176b5d9400c0545015d40ae09d75a6161
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
	conn = sqlite3.connect('peewee.db')
	cursor = conn.cursor()
	try:
		cursor.execute(query)
		return [row for row in cursor.execute(query)]
	except:
		conn.close()
		print "Invalid Data"
		return "0"

#m = writeRawQuery('SELECT * from pattable')
#for k in m:
#	for j in k:
#		print j	
#		print type(j)

def getPatientRecord(regnNo):
	patTableDetails = PatTable.get(regnNo = regnNo)
	patDataDetails = PatData.get(regnNo = regnNo)
	patientDetails = [	patTableDetails.regnNo,
						patTableDetails.name,
						patTableDetails.addr,
						patTableDetails.age,
						patTableDetails.dob,
						patTableDetails.sex,
						patTableDetails.phoneNo,
						patTableDetails.alias,
						patTableDetails.occupation,
						patTableDetails.conName,
						patTableDetails.conAddr,
						patTableDetails.conPhone,
						patTableDetails.idNos,
						patDataDetails.nextDateOfVisit,
						patDataDetails.pulseRate,
						patDataDetails.bodyTemperature,
						patDataDetails.bmi,
						patDataDetails.diagnosis,
						patDataDetails.weight ]
	return patientDetails




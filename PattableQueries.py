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




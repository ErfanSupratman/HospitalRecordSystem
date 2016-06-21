from peewee import *

#setting DB connection
db = MySQLDatabase('hospitalDB', user='test', password="test", host="localhost")

#base model for meta data of the tables
class BaseModel(Model):
	class Meta:
		database = db

#all tables derive from the BaseModel for the meta data
#patients table
class PatTable(BaseModel):
	name = CharField(max_length=60)
	addr = CharField(max_length=200)
	age = IntegerField(null=True)
	dob = DateField()
	sex = CharField(max_length=1) # Check for only 'M' or 'F' to be done
	phoneNo = CharField(max_length=36)
	alias = CharField(max_length=14)
	regnNo = CharField(max_length=16, primary_key=True)
	occupation = CharField(max_length=20)
	conName = CharField(max_length=30)
	conAddr = CharField(max_length=100)
	conPhone = CharField(max_length=12)
	idNos = CharField(max_length=50)
	ConRTP = CharField(max_length=12,null=True)

#patient data
class PatData(BaseModel):
	class Meta:
		primary_key = CompositeKey('regnNo','currentUnixTime')
	regnNo = ForeignKeyField(PatTable, related_name = 'visits')
	currentUnixTime = BigIntegerField()
	nextDateOfVisit = DateField()
	bloodPressure = CharField(max_length=5)
	pulseRate = CharField(max_length=5)
	bodyTemperature = CharField(max_length=5)
	bmi = CharField(max_length=5)
	diagnosis = CharField(max_length=50)
	weight = CharField(max_length=8)


class TestData(BaseModel):
	class Meta:
		primary_key = CompositeKey('regnNo','currentUnixTime')
	regnNo = ForeignKeyField(PatTable, related_name = 'tests')
	currentUnixTime = BigIntegerField()
	testName = CharField(max_length=50)
	testResult = CharField(max_length=100)
			

if __name__=='__main__':
	db.connect()
	db.create_tables([PatTable, PatData, TestData],safe=True)
	db.close()

import peewee

hospitalDB = peewee.SqliteDatabase('HospitalDatabase.db')

def reset(tableName):
	if tableName.table_exists():
		tableName.drop_table()
		print "Hi"
	tableName.create_table()

class PatTable(peewee.Model):
	class Meta:
		db = hospitalDB
	
	name = peewee.CharField(max_length=60)
	addr = peewee.CharField(max_length=200)
	age = peewee.IntegerField(null=True)
	dob = peewee.DateField()
	sex = peewee.CharField(max_length=1) # Check for only 'M' or 'F' to be done
	phoneNo = peewee.CharField(max_length=36)
	alias = peewee.CharField(max_length=14)
	regnNo = peewee.CharField(max_length=16, primary_key=True)
	occupation = peewee.CharField(max_length=20)
	conName = peewee.CharField(max_length=30)
	conAddr = peewee.CharField(max_length=100)
	conPhone = peewee.CharField(max_length=12)
	idNos = peewee.CharField(max_length=50)
	ConRTP = peewee.CharField(max_length=12,null=True)


class PatData(peewee.Model):
	class Meta:
		db = hospitalDB
		
		primary_key = peewee.CompositeKey('regnNo','currentUnixTime')
	
	
	regnNo = peewee.ForeignKeyField(PatTable, related_name = 'visits')
	currentUnixTime = peewee.BigIntegerField()
	nextDateOfVisit = peewee.DateField()
	bloodPressure = peewee.CharField(max_length=5)
	pulseRate = peewee.CharField(max_length=5)
	bodyTemperature = peewee.CharField(max_length=5)
	bmi = peewee.CharField(max_length=5)
	diagnosis = peewee.CharField(max_length=50)
	weight = peewee.CharField(max_length=8)

class TestData(peewee.Model):
	class Meta:
		db = hospitalDB
		primary_key = peewee.CompositeKey('regnNo','currentUnixTime')
	
	regnNo = peewee.ForeignKeyField(PatTable, related_name = 'tests')
	currentUnixTime = peewee.BigIntegerField()
	testName = peewee.CharField(max_length=50)
	testResult = peewee.CharField(max_length=100)
			

if __name__=='__main__':
	#Script mode - Whe-n you run script, tables are created	
	hospitalDB.connect()
	reset(PatData)
	reset(PatTable)
	reset(TestData)

	#a = TestData.create(regnNo='35',currentUnixTime=12452534,testName='a2c',testResult='sa5')
	#a.save()

	hospitalDB.commit()
	hospitalDB.close()

import re
import datetime

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def validString(name):
	if re.match(r'^\w+$',name) and not re.match(r'\d',name) and len(name):
		return 1
	else:
		return 0

def validPhone(phoneNo):
	if re.match(r'^\w+$',phoneNo) and phoneNo.isdigit() and len(phoneNo) <= 10:
		return 1
	else: 
		return 0

def validAge(age):
	if RepresentsInt(age):
		return 1
	else:
		return 0

def validDate(date):
	if datetime.date(year=2000, month=1,day=1) < date <= datetime.datetime.now():
		return 1
	else:
		return 0

def validInt(number):
	if RepresentsInt(number):
		return 1
	else:
		return 0

def PatEntryFormValidate(inputsData):
	if not validString(inputsData['Name']):
		return '\nInvalid Name\n'
	if not validInt(inputsData['Age']):
		return '\nInvalid Age\n'
	#if not validDate(datetime.date(inputsData['DOB'].year(),inputsData['DOB'].month(),inputsData['DOB'].day())):
	#	return '\nInvalid date\n'
	if not validPhone(inputsData['Phone']):
		return '\nInvalid PhoneNo\n'
	if not validString(inputsData['Alias']):
		return '\nInvalid alias name\n'
	if not validString(inputsData['Occupation']):
		return '\nInvalid entry to occupation\n'
	if not validInt(inputsData['IDNo']):
		return '\nInvalid IDno\n'
	if not validInt(inputsData['RegnNo']):
		return '\nInvalid regNo\n'
	if not validString(inputsData['ConName']):
		return '\nInvalid entry to contact name\n'
	if not validString(inputsData['ConRTP']):
		return '\nInvalid entry to contact relation\n'
	return 1 

def PatDataFormValidate(inputsData):
	if not validInt(inputsData['RegNo']):
		return '\nInvalid regNo\n'
	#if not validDate(datetime.date(inputsData['NextDateOfVisit'].year(),inputsData['NextDateOfVisit'].month(),inputsData['NextDateOfVisit'].day())):
	#	return '\nInvalid date\n'
	if not validInt(inputsData['BloodPressure']):
		return '\nInvalid entry for Blood Pressure\n'
	if not validInt(inputsData['BodyTemperature']):
		return '\nInvalid entry for Body Temperature\n'
	if not validInt(inputsData['Bmi']):
		return '\nInvalid entry for BMI\n'
	if not validInt(inputsData['PulseRate']):
		return '\nInvalid entry for Pulse Rate\n'
	if not validInt(inputsData['Weight']):
		return '\nInvalid entry for Weight\n'
	if not validString(inputsData['Diagnosis']):
		return '\nInvalid Diagnosis\n'
	return 1

def PatTestFormValidate(inputsData):
	if not validInt(inputsData['RegNo']):
		return '\nInvalid regNo\n'
	if not validString(inputsData['TestName']):
		return '\nInvalid Test Name\n'
	if not validString(inputsData['TestResult']):
		return '\nInvalid Test Result\n'
	return 1


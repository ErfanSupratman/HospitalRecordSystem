import re
import datetime
from PyQt4 import QtGui,QtCore,QtSql
from PyQt4.QtGui import *
from PyQt4.QtCore import *
# Validation helpers
# CAUTION : The string input in each helper function is of object type QString, not str

'''
TODO:
-----
1. Modify validString() to accept names with spaces
2. Numbers appear to allowed in names currently. Is this intended? If not, check the regex expressions.
'''

def RepresentsInt(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def validBloodPressure(bp):
	return len(bp)

def validString(name):
	return re.match(r'^[A-Za-z\s]+$',name) and not re.match(r'\d',name) and len(name)

def validPhone(phoneNo):
	return re.match(r'^\w+$',phoneNo) and str(phoneNo).isdigit() and len(phoneNo) <= 10

def validInt(number):
	return RepresentsInt(number)

def validAge(age):
	return validInt(age) and int(age)>=0

def validDate(date):
	return datetime.date(year=2000, month=1,day=1) < date <= datetime.datetime.now()

def validDateOfBirth(date):
    return datetime.date.today() >= date

    
# Validation helpers over

def PatEntryFormValidate(inputsData):
    print inputsData['DOB'].toPyDate()
    if not validString(inputsData['Name']):
        return 0,'\nInvalid Name\n'
    
    if not validAge(inputsData['Age']):
        return 0,'\nInvalid Age\n'

    if not validDateOfBirth(inputsData['DOB'].toPyDate()):
        return 0,'\nInvalid date\n'
    
    if not validPhone(inputsData['Phone']):
        return 0,'\nInvalid PhoneNo\n'
    
    if not validString(inputsData['Alias']):
        return 0,'\nInvalid alias name\n'
    
    if not validString(inputsData['Occupation']):
        return 0,'\nInvalid entry to occupation\n'
    
    if not validInt(inputsData['IDNo']):
        return 0,'\nInvalid IDno\n'
    
    if not validInt(inputsData['RegnNo']):
        return 0,'\nInvalid regNo\n'
    
    if not validString(inputsData['ConName']):
        return 0,'\nInvalid entry to contact name\n'

    if not validString(inputsData['ConRelation']):
        return 0,'\nInvalid entry to contact relation\n'
    
    return 1,''  # No validation error


def PatDataFormValidate(inputsData):
    
    if not validInt(inputsData['RegNo']):
        return 0,'\nInvalid regNo\n'
    
    #if not validDate(datetime.date(inputsData['NextDateOfVisit'].year(),inputsData['NextDateOfVisit'].month(),inputsData['NextDateOfVisit'].day())):
    #	return '\nInvalid date\n'

    if not validBloodPressure(str(inputsData['BloodPressure'])):
        return 0,'\nInvalid entry for Blood Pressure\n'

    if not validInt(inputsData['BodyTemperature']):
        return 0,'\nInvalid entry for Body Temperature\n'
    
    if not validInt(inputsData['Bmi']):
        return 0,'\nInvalid entry for BMI\n'
    
    if not validInt(inputsData['PulseRate']):
        return 0,'\nInvalid entry for Pulse Rate\n'

    if not validInt(inputsData['Weight']):
        return 0,'\nInvalid entry for Weight\n'
    
    if not validString(inputsData['Diagnosis']):
        return 0,'\nInvalid Diagnosis\n'
    
    return 1,''  # No validation error


def PatTestFormValidate(inputsData):

    if not validInt(inputsData['RegNo']):
        return 0,'\nInvalid regNo\n'
    
    if not validString(inputsData['TestName']):
        return 0,'\nInvalid Test Name\n'
    
    if not validString(inputsData['TestResult']):
        return 0,'\nInvalid Test Result\n'
    
    return 1,''  # No validation error


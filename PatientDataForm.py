
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_PatientDataForm(object):
    def setupUi(self,PatientDataForm):
        PatientDataForm.setObjectName(_fromUtf8("PatientDataForm"))        
        PatientDataForm.resize(800, 600)
        self.centralwidget = QtGui.QWidget(PatientDataForm)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(160, 40, 181, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 111, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(160, 100, 181, 31))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(160, 160, 181, 31))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 111, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.plainTextEdit_4 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(160, 230, 181, 31))
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 101, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.plainTextEdit_5 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(160, 290, 181, 31))
        self.plainTextEdit_5.setObjectName(_fromUtf8("plainTextEdit_5"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 300, 121, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.plainTextEdit_6 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(160, 350, 181, 31))
        self.plainTextEdit_6.setObjectName(_fromUtf8("plainTextEdit_6"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 101, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.plainTextEdit_7 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(160, 410, 181, 31))
        self.plainTextEdit_7.setObjectName(_fromUtf8("plainTextEdit_7"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 420, 66, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.plainTextEdit_8 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(160, 470, 181, 31))
        self.plainTextEdit_8.setObjectName(_fromUtf8("plainTextEdit_8"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 480, 111, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 520, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.statusbar = QtGui.QStatusBar(PatientDataForm)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #PatientDataForm.setStatusBar(self.statusbar)

        self.retranslateUi(PatientDataForm)
        QtCore.QMetaObject.connectSlotsByName(PatientDataForm)



    def retranslateUi(self, PatientDataForm):
        PatientDataForm.setWindowTitle(_translate("PatientDataForm", "Patient Data Form", None))
        self.label.setText(_translate("PatientDataForm", "RegNo:", None))
        self.label_2.setText(_translate("PatientDataForm", "Next Date Of Visit:", None))
        self.label_3.setText(_translate("PatientDataForm", "Blood Pressure", None))
        self.label_4.setText(_translate("PatientDataForm", "Pulse Rate", None))
        self.label_5.setText(_translate("PatientDataForm", "Body Temperature", None))
        self.label_6.setText(_translate("PatientDataForm", "Body Mass Index", None))
        self.label_7.setText(_translate("PatientDataForm", "Diagnosis", None))
        self.label_8.setText(_translate("PatientDataForm", "weight", None))
        self.pushButton.setText(_translate("PatientDataForm", "Submit", None))

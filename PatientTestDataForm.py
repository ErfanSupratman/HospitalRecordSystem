
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


class Ui_PatientTestDataForm(object):
    def setupUi(self,PatientTestDataForm):
        PatientTestDataForm.setObjectName(_fromUtf8("PatientTestDataForm"))        
        PatientTestDataForm.resize(800, 600)
        self.centralwidget = QtGui.QWidget(PatientTestDataForm)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(160, 40, 181, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 111, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(160, 100, 181, 31))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(160, 160, 181, 31))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 111, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 300, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.statusbar = QtGui.QStatusBar(PatientTestDataForm)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #PatientTestDataForm.setStatusBar(self.statusbar)

        self.retranslateUi(PatientTestDataForm)
        QtCore.QMetaObject.connectSlotsByName(PatientTestDataForm)



    def retranslateUi(self, PatientTestDataForm):
        PatientTestDataForm.setWindowTitle(_translate("PatientTestDataForm", "Patient Test Data Form", None))
        self.label.setText(_translate("PatientTestDataForm", "RegNo:", None))
        self.label_2.setText(_translate("PatientTestDataForm", "Test Name", None))
        self.label_3.setText(_translate("PatientTestDataForm", "Test Result", None))
        self.pushButton.setText(_translate("PatientTestDataForm", "Submit", None))

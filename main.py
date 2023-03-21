from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from utils.mail_manager import MailManager


class Ui_Form(object):
    def __init__(self,mailData):
        self.data = mailData

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 350)
        
        self.emailText = QtWidgets.QTextEdit(Form)
        self.emailText.setGeometry(QtCore.QRect(200, 70, 341, 41))
        self.emailText.setObjectName("emailText")
        
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(40, 140, 101, 23))
        self.password.setObjectName("password")

        self.passText = QtWidgets.QLineEdit(Form)
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passText.setGeometry(QtCore.QRect(200, 140, 341, 41))
        self.passText.setObjectName("passText")
        
        self.emailAddress = QtWidgets.QLabel(Form)
        self.emailAddress.setGeometry(QtCore.QRect(40, 70, 131, 23))
        self.emailAddress.setObjectName("emailAddress")
        
        self.sendMails = QtWidgets.QPushButton(Form)
        self.sendMails.setGeometry(QtCore.QRect(400, 220, 141, 51))
        self.sendMails.setObjectName("sendMails")
        self.sendMails.clicked.connect(self.sendMailsMethod)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Credentials"))
        self.password.setText(_translate("Form", "Password"))
        self.emailAddress.setText(_translate("Form", "Email address"))
        self.sendMails.setText(_translate("Form", "Send Mails"))

    def sendMailsMethod(self):
        if self.validate() == 1:
            mailManager = MailManager(self.data)
            mailManager.sendMails()
            pop = QtWidgets.QMessageBox()
            pop.setWindowTitle("Progress")
            pop.setText("Successfully Completed!")
            pop.setIcon(QtWidgets.QMessageBox.Information)
            pop.buttonClicked.connect(self.closeProgram)
            x = pop.exec_()
    
    def validate(self):
        if self.emailText.toPlainText().strip()=="" or self.passText.text().strip()=="":
            self.showPopup("Fields must not be empty")
            return 0
        self.data["email"] = self.emailText.toPlainText().strip()
        self.data["pass"] = self.passText.text().strip()
        return 1

    def showPopup(self, message):
        pop = QtWidgets.QMessageBox()
        pop.setWindowTitle("Error")
        pop.setText(message)
        pop.setIcon(QtWidgets.QMessageBox.Warning)
        x = pop.exec_()

    def closeProgram(self):
        sys.exit()
# if __name__ == "__main__":
    
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

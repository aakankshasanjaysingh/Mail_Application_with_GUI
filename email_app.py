from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import os
from credentials import Ui_Form

class Ui_MainWindow(object):
    mailData = {}
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(850, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.subjectText = QtWidgets.QTextEdit(self.centralwidget)
        self.subjectText.setGeometry(QtCore.QRect(260, 40, 491, 41))
        self.subjectText.setObjectName("subjectText")
        self.subject = QtWidgets.QLabel(self.centralwidget)
        self.subject.setGeometry(QtCore.QRect(70, 40, 89, 23))
        self.subject.setObjectName("subject")
        self.body = QtWidgets.QLabel(self.centralwidget)
        self.body.setGeometry(QtCore.QRect(70, 110, 89, 23))
        self.body.setObjectName("body")
        self.bodyText = QtWidgets.QTextEdit(self.centralwidget)
        self.bodyText.setGeometry(QtCore.QRect(260, 110, 491, 181))
        self.bodyText.setObjectName("bodyText")
        
        self.attachment = QtWidgets.QCheckBox(self.centralwidget)
        self.attachment.setGeometry(QtCore.QRect(70, 330, 141, 29))
        self.attachment.setObjectName("attachment")
        self.attachment.clicked.connect(self.isAttachment)

        self.attachmentSelect = QtWidgets.QPushButton(self.centralwidget)
        self.attachmentSelect.setEnabled(True)
        self.attachmentSelect.setGeometry(QtCore.QRect(310, 330, 411, 33))
        self.attachmentSelect.setObjectName("attachmentSelect")
        self.attachmentSelect.setEnabled(False)
        self.attachmentSelect.clicked.connect(self.selectAttachmentFolder)
        
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(320, 570, 191, 41))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.nextWindow)

        self.csvSelect = QtWidgets.QPushButton(self.centralwidget)
        self.csvSelect.setGeometry(QtCore.QRect(310, 440, 411, 33))
        self.csvSelect.setObjectName("csvSelect")
        self.csvSelect.clicked.connect(self.getcsv)

        self.recipientsList = QtWidgets.QLabel(self.centralwidget)
        self.recipientsList.setGeometry(QtCore.QRect(70, 450, 141, 23))
        self.recipientsList.setObjectName("recipientsList")

        self.recipientsList = QtWidgets.QLabel(self.centralwidget)
        self.recipientsList.setGeometry(QtCore.QRect(70, 450, 141, 23))
        self.recipientsList.setObjectName("recipientsList")

        self.attachPathLabel = QtWidgets.QLabel(self.centralwidget)
        self.attachPathLabel.setGeometry(QtCore.QRect(320, 380, 391, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.attachPathLabel.setFont(font)
        self.attachPathLabel.setObjectName("attachPathLabel")

        self.sheetPathLabel = QtWidgets.QLabel(self.centralwidget)
        self.sheetPathLabel.setGeometry(QtCore.QRect(320, 490, 401, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.sheetPathLabel.setFont(font)
        self.sheetPathLabel.setObjectName("sheetPathLabel")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Email Application"))
        self.subject.setText(_translate("MainWindow", "Subject"))
        self.body.setText(_translate("MainWindow", "Body"))
        self.attachment.setText(_translate("MainWindow", " Attachment"))
        self.attachmentSelect.setText(_translate("MainWindow", "Select Folder"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.csvSelect.setText(_translate("MainWindow", "Add File"))
        self.recipientsList.setText(_translate("MainWindow", "Recipients List"))
        self.attachPathLabel.setText(_translate("MainWindow", "- not selected -"))
        self.sheetPathLabel.setText(_translate("MainWindow", "- not added -"))

    def isAttachment(self):
        if(self.attachment.isChecked()==True):
            self.attachmentSelect.setEnabled(True)        
        else:
            self.attachmentSelect.setEnabled(False)
    
    def selectAttachmentFolder(self):
        self.dialog = Main()
        self.folderPath = self.dialog.browseFolder()
        if self.folderPath != "":
            self.attachPathLabel.setText(self.folderPath)
            self.attachPathLabel.adjustSize()

    def getcsv(self):
        self.dialog = Main()
        self.filePath=self.dialog.browseFile()
        if self.filePath != "":
            self.sheetPathLabel.setText(self.filePath)
            self.sheetPathLabel.adjustSize()
       
    def nextWindow(self):
        if self.validateData() ==1:
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form(self.mailData)
            self.ui.setupUi(self.Form)
            self.Form.show()
            
        
    def validateData(self):
        if self.subjectText.toPlainText().strip()=="" or self.bodyText.toPlainText().strip() == "":
            self.showPopup("Fields must not be empty")
            return 0
        if self.sheetPathLabel.text() == "- not added -":
            self.showPopup("Invalid Path")
            return 0
        if self.attachment.isChecked()==True and self.attachPathLabel.text() == "- not selected -": 
            self.showPopup("Invalid Path")
            return 0
        self.mailData = {
                "subject":self.subjectText.toPlainText(),
                "body":self.bodyText.toPlainText(),
                "recipients": self.sheetPathLabel.text()
            }
        if self.attachment.isChecked()==True:
            self.mailData["attachment"] = self.folderPath    
        else:
            self.mailData["attachment"]=""
        #print(mailData)
        return 1

    def getMailData(self):
        return self.mailData

    def showPopup(self, message):
        pop = QtWidgets.QMessageBox()
        pop.setWindowTitle("Error")
        pop.setText(message)
        #pop.setInformativeText(message)
        pop.setIcon(QtWidgets.QMessageBox.Warning)
        x = pop.exec_()


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

    def browseFolder(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setWindowTitle('Open Recipients list file')
        folderPathstr = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        return folderPathstr

    def browseFile(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setWindowTitle('Open Recipients list file')
        dialog.setNameFilter('(*.csv)')
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        filePath = None
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            filePath = dialog.selectedFiles()
        if filePath:
            self.filePathstr = str(filePath[0])
            return self.filePathstr
            

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

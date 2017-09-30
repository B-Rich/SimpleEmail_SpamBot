# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sesb-gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost! (no u)
# Message: Nah, I'm editing it from this file itself.
# Nothing will be lost. Just don't do:
# pyuic5 -x sesb-gui.ui -o sesbgui.py

from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.request import urlopen
import smtplib
import sys
import time
#import threading
#from multiprocessing import Process
#sys.path.append("../")
#from SESB import Engine

__gversion__ = "v0.1b"

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(755, 517)
        MainWindow.setFixedSize(755, 517)
        #self.setWindowIcon(QtGui.QIcon(""))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 410, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(370, 420, 64, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("QLCDNumber {\n"
"    color: rgb(0, 0, 127);\n"
"    background-color: rgb(130, 130, 130);\n"
"}")
        self.lcdNumber.setObjectName("lcdNumber")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(660, 120, 58, 29))
        self.spinBox.setObjectName("spinBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(470, 160, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(470, 200, 251, 191))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 120, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 160, 101, 31))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 260, 301, 181))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setOverwriteMode(True)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 200, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 390, 61, 31))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 50, 301, 151))

        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9.6)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 231, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 51, 31))
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 410, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 410, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 10, 251, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(490, 50, 251, 31))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 10, 71, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 50, 71, 31))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 25))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionCheck_for_Updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionRepo = QtWidgets.QAction(MainWindow)
        self.actionRepo.setObjectName("actionRepo")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionVersion)
        self.menuAbout.addAction(self.actionCheck_for_Updates)
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Shortcuts
        self.pushButton.setShortcut("Ctrl+S")
        self.pushButton_3.setShortcut("Ctrl+D")
        self.pushButton_4.setShortcut("Ctrl+X")
        self.actionQuit.setShortcut("Ctrl+Q")
        #self.actionQuit.

        self.stop = False
        self.normal = None

        self.actionQuit.triggered.connect(self.quit_tab)
        self.actionVersion.triggered.connect(self.version)
        self.actionCheck_for_Updates.triggered.connect(self.check_for_updates)
        self.actionHelp.triggered.connect(self.help)
        self.pushButton.clicked.connect(self.spam_button)
        self.pushButton_3.clicked.connect(self.stop_button)
        self.pushButton_4.clicked.connect(self.send_button)
        #self.pushButton_4.clicked.connect(self.)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SimpleEmail_SpamBot"))
        #MainWindow.setWindowIcon(QtGui.QIcon(""))
        self.pushButton.setText(_translate("MainWindow", "Spam"))
        self.label.setText(_translate("MainWindow", "Delay:"))
        self.label_2.setText(_translate("MainWindow", "Email Subject:"))
        self.label_3.setText(_translate("MainWindow", "Email Message:"))
        self.label_4.setText(_translate("MainWindow", "Counter:"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Targets (one email per space/line):"))
        self.label_6.setText(_translate("MainWindow", "Logs:"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_4.setText(_translate("MainWindow", "Send"))
        self.label_7.setText(_translate("MainWindow", "Full Email:"))
        self.label_8.setText(_translate("MainWindow", "Password:"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
        self.actionCheck_for_Updates.setText(_translate("MainWindow", "Check for Updates"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionRepo.setText(_translate("MainWindow", "Repo"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def quit_tab(self):
        popup = QtWidgets.QMessageBox.question(MainWindow, "Quit SESB",
                                               "Are you sure you want to quit SESB-GUI?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if popup == QtWidgets.QMessageBox.Yes:
            print("\rGoodbye!")
            sys.exit(0)
        else:
            pass

    def version(self):
        msg = """This version of SESB-GUI is: {}""".format(__gversion__)
        popup = QtWidgets.QMessageBox.about(MainWindow, "Version", msg)

    def check_for_updates(self):
        latest_version = urlopen("https://raw.githubusercontent.com/DizAzTor/SimpleEmail_SpamBot/master/gversion.txt").read()
        latest_version = latest_version.rstrip().decode("utf-8", "strict")
        if latest_version != __gversion__:
            msg = "Yes! There is an update available. It's {}".format(latest_version)
        else:
            msg = "Nope, check again later."

        popup = QtWidgets.QMessageBox
        popup.about(MainWindow, "Check for Updates", msg)

    def help(self):
        msg = """\t\t  SESB - GUI
Shortcuts:
Ctrl-Q = quit.
Ctrl-S = spam.
Ctrl-D = stop.
Ctrl-X = send.

About:
SESB-GUI is a graphical user interface (Using PyQt5) version of SESB.
It doesn't have all of the stuff SESB-CLI
has, but I might add them soon! :p

It's pretty straightforward. The "Logs" message box is for you, to
actually know what's going on.

SESB-GUI isn't anything related to SESB-CLI
The spam function is modified for GUI.
I mean, I can make it work from the SESB.py (Engine class).
But right now, I'm just doing it like this.
I'll change a lot of things in SESB later.

Modes:
If you're looking for GUI modes, then, there are none yet.

GitHub repo: https://github.com/DizAzTor/SimpleEmail_SpamBot

"Why is it so slow?!"
1. It's still in alpha.
2. I'm not using threads/multiprocessing. (It's in my TODO list.)

If you are having problems with SESB or
just want to say hi or ask me something,
you can send a message
to my Telegram account. @dizaztor"""
        popup = QtWidgets.QMessageBox.about(MainWindow, "Help", msg)

    def stop_button(self):
        self.stop = True

    def spam_button(self):
        if self.stop is True:
            self.stop = False
        else:
            pass

        account = self.lineEdit_2.text()
        password = self.lineEdit_3.text()

        spam_subject = self.lineEdit.text()
        spam_message = self.textEdit.toPlainText()

        targets = self.plainTextEdit.toPlainText().split()
        spam_delay = self.spinBox.value()

        if "@gmail.com" in account:
            server = smtplib.SMTP("smtp.gmail.com:587")
            yes = True
        elif "@outlook.com" in account:
            server = smtplib.SMTP("smtp-mail.outlook.com:587")
            yes = True
        elif "@icloud.com" in account:
            server = smtplib.SMTP("smtp.mail.me.com:587")
            yes = True
        elif "@yahoo.com" in account:
            server = smtplib.SMTP("smtp.mail.yahoo.com:587")
            yes = True
        elif "@zoho.com" in account:
            server = smtplib.SMTP("smtp.zoho.eu:587")
            yes = True
        elif "@gmx.us" in account:
            server = smtplib.SMTP("smtp.gmx.com:25")
            yes = True
        elif "@fastmail.fm" in account:
            server = smtplib.SMTP("mail.messagingengine.com:587")
            yes = True
        else:
            yes = False
            self.textBrowser.setText(self.textBrowser.toPlainText() + "\rERROR: Unsupported email.")

        if yes is False:
            pass
        else:
            server.ehlo()
            server.starttls()

            try:
                msg = "\r\n".join([
                    "From: %s",
                    "To: %s",
                    "Subject: %s",
                    "",
                    "%s"]) % (account, targets, spam_subject, spam_message)

                server.login(account, password)
                self.textBrowser.setText(self.textBrowser.toPlainText() + "\rSuccessfully logged in.")

                if self.normal == True:
                    server.sendmail(account, targets, msg)
                    self.normal = False
                else:
                    self.textBrowser.setText(self.textBrowser.toPlainText() + "\rStarted spamming...")
                    x = 0
                    #timer = QtCore.QTimer()
                    while (self.stop is False):
                        QtWidgets.QApplication.processEvents()
                        server.sendmail(account, targets, msg)
                        x += 1
                        self.lcdNumber.display(x)
                        self.textBrowser.setText(self.textBrowser.toPlainText() + "\rMail sent.")
                        #timer.start(spam_delay)
                        time.sleep(float(spam_delay))

                        if self.stop is not False:
                            self.textBrowser.setText(self.textBrowser.toPlainText() + "\rStopped.")
                            break

            except smtplib.SMTPAuthenticationError:
                self.textBrowser.setText(self.textBrowser.toPlainText() + "\rERROR: Wrong email or password.")

    def send_button(self):
        self.normal = True
        self.spam_button()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

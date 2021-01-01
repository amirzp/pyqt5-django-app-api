from PyQt5 import (QtWidgets, QtGui)

import login_app
import sys


class MainWindow:
    def __init__(self):
        self.studentWindow = None
        self.loginWindow = None
        self.flag = None
        self.admin_name = None
        self.login()

    def student_log(self):
        flag = self.loginWindow.click_log()
        if flag:
            self.admin_name = self.loginWindow.admin_name
            self.loginWindow.destroy()
            self.loginWindow = None
            self.studentWindow = studentWindow.StudentWindow(self.admin_name)
            self.studentWindow.toolBarLog.clicked.connect(self.login)
            self.studentWindow.toolBarExit.clicked.connect(self.student_exit)
            self.studentWindow.ui()

    def student_exit(self):
        if self.studentWindow:

            if QtWidgets.QMessageBox.information(
                    self.studentWindow,
                    "Warning",
                    "Are you sure want to exit?",
                    QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes
            ) == QtWidgets.QMessageBox.Yes:

                sys.exit(0)

    def login(self):
        if self.studentWindow:

            if QtWidgets.QMessageBox.information(
                    self.studentWindow,
                    "Warning",
                    "Are you sure want to Log out?",
                    QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes
            ) == QtWidgets.QMessageBox.Yes:

                self.studentWindow.destroy()
                self.studentWindow = None

        if not self.studentWindow:
            self.loginWindow = login_app.Dialog()
            self.loginWindow.logButton.clicked.connect(self.login_click)
            self.loginWindow.backButton.clicked.connect(self.register)
            self.flag = self.loginWindow.flag
            self.loginWindow.show()

    def register(self):
        self.loginWindow = login_app.Dialog('reg')
        self.loginWindow.logButton.clicked.connect(self.register_click)
        self.loginWindow.backButton.clicked.connect(self.login)
        self.loginWindow.show()

    def register_click(self):
        pass

    def login_click(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.setStyle('QtCurve')
    app.setFont(QtGui.QFont("Noto Sans", 10))
    # ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    sys.exit(app.exec_())

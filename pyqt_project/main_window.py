from PyQt5 import (QtWidgets, QtGui)

import login_app
import home_app
import sys
import request_api


class MainWindow:
    def __init__(self):
        self.request = request_api.ApiRequest()
        self.homeWindow = None
        self.loginWindow = None
        self.admin_name = None
        self.login()

    def home_app(self):
        # flag = self.loginWindow.click_log()
        # if flag:
        self.loginWindow.destroy()
        self.loginWindow = None
        self.homeWindow = home_app.Window(self.admin_name)
        self.homeWindow.logoutButton.clicked.connect(self.login)
        self.homeWindow.exitButton.clicked.connect(self.home_exit)
        self.homeWindow.ui()

    def home_exit(self):
        if self.homeWindow:

            if QtWidgets.QMessageBox.information(
                    self.homeWindow,
                    "Warning",
                    "Are you sure want to exit?",
                    QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes
            ) == QtWidgets.QMessageBox.Yes:

                sys.exit(0)

    def login(self):
        if self.homeWindow:

            if QtWidgets.QMessageBox.information(
                    self.homeWindow,
                    "Warning",
                    "Are you sure want to Log out?",
                    QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes
            ) == QtWidgets.QMessageBox.Yes:

                self.homeWindow.destroy()
                self.homeWindow = None

        if not self.homeWindow:
            self.loginWindow = login_app.Dialog()
            self.loginWindow.logButton.clicked.connect(self.login_click)
            self.loginWindow.backButton.clicked.connect(self.register)
            self.loginWindow.show()

    def register(self):
        self.loginWindow = login_app.Dialog('reg')
        self.loginWindow.logButton.clicked.connect(self.register_click)
        self.loginWindow.backButton.clicked.connect(self.login)
        self.loginWindow.show()

    def register_click(self):
        pass

    def login_click(self):
        user = self.loginWindow.userLine.text().lower()
        password = self.loginWindow.passLine.text()
        if user and password:
            data = {
                "username": f"{user}",
                "password": f"{password}"
            }
            url = 'http://127.0.0.1:8000/contact/v1/token/'
            request = self.request.login(data=data, url=url)
            if request is True:
                self.admin_name = user
                self.home_app()
                # return True
            else:
                QtWidgets.QMessageBox.information(self.loginWindow, "Warning", request['detail'])
        else:
            QtWidgets.QMessageBox.information(self.loginWindow, "Warning", "Fields can not empty")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.setStyle('QtCurve')
    app.setFont(QtGui.QFont("Noto Sans", 10))
    # ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    sys.exit(app.exec_())

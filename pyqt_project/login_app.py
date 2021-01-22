import sys
import style
from PyQt5 import (QtWidgets, QtGui, QtCore)


class Dialog(QtWidgets.QWidget):

    def __init__(self, win=None):
        super().__init__()

        self.setGeometry(150, 150, 700, 500)
        self.win = win

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.topLayout = QtWidgets.QHBoxLayout()
        self.middleLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout = QtWidgets.QVBoxLayout()
        self.childMiddleLayout = QtWidgets.QFormLayout()
        self.frame = QtWidgets.QFrame()

        self.main_reg = QtWidgets.QVBoxLayout()
        self.frame_reg = QtWidgets.QFrame()

        self.labelLog = QtWidgets.QLabel("LOGIN HERE")
        self.labelLog.setFont(QtGui.QFont("Gabriola", 24))
        self.userLabel = QtWidgets.QLabel("User Name : ")
        self.passLabel = QtWidgets.QLabel("Password : ")
        self.confirmPassLabel = QtWidgets.QLabel("ConfirmPass : ")
        self.userLine = QtWidgets.QLineEdit()
        self.userLine.setPlaceholderText("User Name")
        self.passLine = QtWidgets.QLineEdit()
        self.passLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passLine.setPlaceholderText("Password")
        self.confirmPassLine = QtWidgets.QLineEdit()
        self.confirmPassLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassLine.setPlaceholderText("Confirm Password")
        self.logButton = QtWidgets.QPushButton("Login", self)

        # register & login back >>
        self.backFrame = QtWidgets.QFrame()
        self.backFrame.setStyleSheet(style.login_back_frame())
        self.backButton = QtWidgets.QPushButton()
        self.backButton.setIcon(QtGui.QIcon(QtGui.QPixmap("file/Icon/back.png")))
        self.backButton.setIconSize(QtCore.QSize(40, 40))
        self.backLabel = QtWidgets.QLabel('Register')
        self.backLabel.setFont(QtGui.QFont("Gabriola", 19))

        self._id = None
        self.window = None
        self.admin_name = None

        self.image0 = QtGui.QImage("file/1.jpg")

        self.read_image(self.width(), self.height())
        self.ui_log()

    def ui_log(self):
        # top layout design >>
        self.topLayout.addWidget(self.backButton)
        self.topLayout.addWidget(self.backLabel)
        self.topLayout.addStretch()
        self.backFrame.setLayout(self.topLayout)

        self.bottomLayout.addStretch()
        self.mainLayout.addWidget(self.backFrame, 2)
        self.mainLayout.addStretch(2)
        self.mainLayout.addLayout(self.middleLayout, 4)
        self.mainLayout.addLayout(self.bottomLayout, 4)

        self.middleLayout.addStretch(1)
        self.middleLayout.addWidget(self.frame, 2)
        self.middleLayout.addStretch(1)

        self.labelLog.setAlignment(QtCore.Qt.AlignCenter)
        self.logButton.setStyleSheet(style.log_button())

        self.userLine.setStyleSheet(style.line_edit())
        self.passLine.setStyleSheet(style.line_edit())
        self.frame.setStyleSheet(style.main_frame())
        self.childMiddleLayout.setVerticalSpacing(30)
        self.childMiddleLayout.addRow(self.labelLog)
        self.childMiddleLayout.addRow(self.userLabel, self.userLine)
        self.childMiddleLayout.addRow(self.passLabel, self.passLine)
        if self.win == "reg":
            self.confirmPassLine.setStyleSheet(style.line_edit())
            self.childMiddleLayout.addRow(self.confirmPassLabel, self.confirmPassLine)
            self.labelLog.setText("REGISTER HERE")
            self.backLabel.setText('Login')
            self.logButton.setText("Register")
        self.childMiddleLayout.verticalSpacing()

        self.childMiddleLayout.addRow(self.logButton)
        self.frame.setLayout(self.childMiddleLayout)

    def read_image(self, width=None, height=None):

        if width is not None and height is None:
            image_file = self.image0.scaledToWidth(width, QtCore.Qt.SmoothTransformation)
        elif width is None and height is not None:
            image_file = self.image0.scaledToHeight(height, QtCore.Qt.SmoothTransformation)
        elif width is not None and height is not None:
            image_file = self.image0.scaled(width, height, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        else:
            image_file = self.image0

        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(image_file))

        self.setLayout(self.mainLayout)
        self.setPalette(palette)

    def resizeEvent(self, event=None):
        self.read_image(event.size().width(), event.size().height())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fen = Dialog()
    fen.show()
    sys.exit(app.exec_())

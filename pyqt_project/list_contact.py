from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        # ######## Layouts >>
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.bottomLayout = QtWidgets.QHBoxLayout()
        # ######## widgets >>
        self.tableWidget = QtWidgets.QTableWidget()
        self.editButton = QtWidgets.QPushButton()
        self.editButton.setIcon(QtGui.QIcon(QtGui.QPixmap("file/Icon/edit.svg")))
        self.deleteButton = QtWidgets.QPushButton()
        self.deleteButton.setIcon(QtGui.QIcon(QtGui.QPixmap("file/Icon/delete.svg")))

        self.ui()

    def ui(self):
        self.mainLayout.addWidget(self.tableWidget)

        self.bottomLayout.addStretch()
        self.bottomLayout.addWidget(self.editButton)
        self.bottomLayout.addWidget(self.deleteButton)

        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)

        self.show()

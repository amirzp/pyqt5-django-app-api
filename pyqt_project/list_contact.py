from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        # ######## Layouts >>
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.bottomLayout = QtWidgets.QHBoxLayout()
        # ######## widgets >>
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

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

    def show_item(self, data: dict):
        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)

        self.tableWidget.setRowCount(len(data))
        if not len(data) == 0:
            self.tableWidget.setColumnCount(len(data[0]))
            for i, name in enumerate(data[0].keys()):
                self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(name.capitalize()))

            self.tableWidget.setColumnHidden(0, True)
            self.tableWidget.setColumnHidden(5, True)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

            for i, dict_item in enumerate(data):
                for j, item in enumerate(dict_item.keys()):
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dict_item[item])))

    def get_item(self):
        _id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        name = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        family = self.tableWidget.item(self.tableWidget.currentRow(), 2).text()
        phone = self.tableWidget.item(self.tableWidget.currentRow(), 3).text()
        email = self.tableWidget.item(self.tableWidget.currentRow(), 4).text()
        user = self.tableWidget.item(self.tableWidget.currentRow(), 5).text()
        data = {
            "id": f"{_id}",
            "name": f"{name}",
            "family": f"{family}",
            "phone": f"{phone}",
            "email": f"{email}",
            "user": user
        }
        return data

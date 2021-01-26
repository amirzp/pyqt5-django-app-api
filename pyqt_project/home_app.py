from PyQt5 import QtWidgets, QtGui
import style
import add_contact
import list_contact
import admin_panel


class Window(QtWidgets.QWidget):
    def __init__(self, admin_name: str, api):
        super(Window, self).__init__()
        self.setWindowTitle('Home V1')
        self.setGeometry(150, 150, 700, 500)
        self.userID = None
        self.api = api
        # ########### widgets >>
        self.adminImageLabel = QtWidgets.QLabel()
        image = QtGui.QPixmap('file/Icon/admin.png')
        f = image.scaled(40, 40)
        self.adminImageLabel.setPixmap(f)
        self.adminName = QtWidgets.QLabel(admin_name.capitalize()+'  ')
        self.adminName.setFont(QtGui.QFont("Dyuthi", 13))
        self.logoutButton = QtWidgets.QPushButton()
        self.logoutButton.setIcon(QtGui.QIcon(QtGui.QPixmap("file/Icon/logout.svg")))
        self.exitButton = QtWidgets.QPushButton()
        self.exitButton.setIcon(QtGui.QIcon(QtGui.QPixmap("file/Icon/off.svg")))
        # ########### Layouts >>
        self.mainLayout = QtWidgets.QVBoxLayout()
        # top layout >>
        self.topLayout = QtWidgets.QFrame()
        self.topLayout.setStyleSheet(style.top_layout_home())
        self.topLayoutChild = QtWidgets.QHBoxLayout()
        # bottom layout >>
        self.bottomLayout = QtWidgets.QFrame()

        # ########### Tool Bar >>
        self.toolBar = QtWidgets.QToolBar("ToolBar")

        self.adminPanelAction = QtWidgets.QAction(
            QtGui.QIcon("file/Icon/admin_1.png"),
            "Admin Panel"
        )
        self.listContactAction = QtWidgets.QAction(
            QtGui.QIcon("file/Icon/list.svg"),
            "List Contact"
        )
        self.addContactAction = QtWidgets.QAction(
            QtGui.QIcon("file/Icon/add.svg"),
            "Add Contact"
        )
        # self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # Add Product >>
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.adminPanelAction)
        self.toolBar.addSeparator()
        # Add Member >>
        self.toolBar.addAction(self.listContactAction)
        self.toolBar.addSeparator()
        # Sell Product >>
        self.toolBar.addAction(self.addContactAction)
        # Triggered Action >>
        self.addContactAction.triggered.connect(self.add_contact)
        self.listContactAction.triggered.connect(self.list_contact)
        self.adminPanelAction.triggered.connect(self.admin_panel)

        # first time run is class method self.get_user_id is work.
        self.get_user_id()

    @staticmethod
    def first_layout():
        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        return v_box

    def ui(self):
        # set layouts >>
        self.topLayoutChild.addWidget(self.adminImageLabel)
        self.topLayoutChild.addWidget(self.adminName)
        self.topLayoutChild.addWidget(self.toolBar)
        self.topLayoutChild.addStretch()
        self.topLayoutChild.addWidget(self.logoutButton)
        self.topLayoutChild.addWidget(self.exitButton)
        self.topLayout.setLayout(self.topLayoutChild)

        # چون QFrame قابل Stretch گرفتن نیست یه تابع میسازیم و یک vBox به این ویجت میدهیم
        # تا بتوانیم با استفاده از تابع del_layout این ویجت رو حذف کنیم برای ست کردن فرم های بعدی
        self.bottomLayout.setLayout(self.first_layout())

        self.mainLayout.addWidget(self.topLayout)
        self.mainLayout.addWidget(self.bottomLayout)
        self.setLayout(self.mainLayout)

        self.show()

    def del_layout(self):
        widget = self.mainLayout.takeAt(1).widget()
        if widget is not None:
            widget.deleteLater()
            self.bottomLayout = None

    # ######### add contact page options >>
    def add_contact(self):
        self.del_layout()
        self.bottomLayout = add_contact.Window('add')
        self.bottomLayout.addButton.clicked.connect(self.add_contact_click)
        self.mainLayout.addWidget(self.bottomLayout)

    def add_contact_click(self):
        url = 'http://127.0.0.1:8000/contact/v1/list/'
        name = self.bottomLayout.nameLine.text()
        family = self.bottomLayout.familyLine.text()
        phone = self.bottomLayout.phoneLine.text()
        email = self.bottomLayout.emailLine.text()
        if not (name and family and phone and email) == "":
            data = {
                "name": f"{name}",
                "family": f"{family}",
                "phone": f"{phone}",
                "email": f"{email}",
                "user": self.userID
            }
            request = self.api.post(url=url, data=data)
            if request is True:
                QtWidgets.QMessageBox.information(self.bottomLayout, "Info", 'Contact is added.')
            else:
                QtWidgets.QMessageBox.information(self.bottomLayout, "Warning", request['detail'])
            self.bottomLayout.nameLine.setText("")
            self.bottomLayout.familyLine.setText("")
            self.bottomLayout.phoneLine.setText("")
            self.bottomLayout.emailLine.setText("")
        else:
            QtWidgets.QMessageBox.information(self.bottomLayout, "Warning", "Fields can not empty")
    # ######### end add contact page options <<

    # ######### list contact page options >>
    def list_contact(self):
        self.del_layout()
        self.bottomLayout = list_contact.Window()
        self.bottomLayout.editButton.clicked.connect(self.edit_click)
        self.bottomLayout.deleteButton.clicked.connect(self.delete_click)
        self.mainLayout.addWidget(self.bottomLayout)
        url = 'http://127.0.0.1:8000/contact/v1/list/'
        request = self.api.get(url=url)
        if request[0] is True:
            self.bottomLayout.show_item(request[1])
        else:
            QtWidgets.QMessageBox.information(self.bottomLayout, "Warning", request[1]['detail'])

    def edit_click(self):
        pass

    def delete_click(self):
        if self.bottomLayout.tableWidget.selectionModel().hasSelection():
            m_box = QtWidgets.QMessageBox.information(
                self.bottomLayout,
                "Warning",
                "You sure delete item?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )

            if m_box == QtWidgets.QMessageBox.Yes:
                _id = self.bottomLayout.tableWidget.item(
                    self.bottomLayout.tableWidget.currentRow(),
                    0
                ).text()
                url = f'http://127.0.0.1:8000/contact/v1/list/{_id}/'
                request = self.api.delete(url=url)
                QtWidgets.QMessageBox.information(self.bottomLayout, "Info", request['detail'])
                return self.list_contact()
        else:
            QtWidgets.QMessageBox.information(
                self.bottomLayout,
                "Warning",
                "Select an item first"
            )
    # ######### end list contact page options <<

    def admin_panel(self):
        self.del_layout()
        self.bottomLayout = admin_panel.Window()
        self.mainLayout.addWidget(self.bottomLayout)

    def get_user_id(self):
        url = 'http://127.0.0.1:8000/contact/v1/user/'
        request = self.api.get(url=url)
        if request[0] is True:
            self.userID = int(request[1][0]['id'])
        else:
            QtWidgets.QMessageBox.information(
                self,
                "Warning",
                request[1]['detail']
            )

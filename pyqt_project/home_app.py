from PyQt5 import QtWidgets, QtGui
import sys
import style
import add_contact
import list_contact
import admin_panel


class Window(QtWidgets.QWidget):
    def __init__(self, admin_name: str):
        super(Window, self).__init__()
        self.setWindowTitle('Home V1')
        self.setGeometry(150, 150, 700, 500)
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
        self.addContactAction.triggered.connect(self.add_contact_triggered)
        self.listContactAction.triggered.connect(self.list_contact)
        self.adminPanelAction.triggered.connect(self.admin_panel)

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

    def add_contact_triggered(self):
        self.del_layout()
        self.bottomLayout = add_contact.Window('add')
        self.mainLayout.addWidget(self.bottomLayout)

    def list_contact(self):
        self.del_layout()
        self.bottomLayout = list_contact.Window()
        self.mainLayout.addWidget(self.bottomLayout)

    def admin_panel(self):
        self.del_layout()
        self.bottomLayout = admin_panel.Window()
        self.mainLayout.addWidget(self.bottomLayout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window('aMir')
    window.ui()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets, QtGui
import sys
import style
import add_contact


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
        self.bottomLayout = QtWidgets.QVBoxLayout()

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
        # self.addProduct.triggered.connect(self.add_product)
        # self.sellProduct.triggered.connect(self.add_sell)

    def ui(self):
        # set layouts >>
        self.topLayoutChild.addWidget(self.adminImageLabel)
        self.topLayoutChild.addWidget(self.adminName)
        self.topLayoutChild.addWidget(self.toolBar)
        self.topLayoutChild.addStretch()
        self.topLayoutChild.addWidget(self.logoutButton)
        self.topLayoutChild.addWidget(self.exitButton)
        self.topLayout.setLayout(self.topLayoutChild)

        self.bottomLayout.addStretch()

        self.mainLayout.addWidget(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)

        self.show()

    def del_layout(self):
        layout = self.mainLayout.takeAt(1).layout()
        if layout is not None:
            layout.deleteLater()
            self.bottomLayout = None

    def add_contact_triggered(self):
        self.del_layout()
        self.bottomLayout = add_contact.Window('add')
        self.mainLayout.addWidget(self.bottomLayout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window('aMir')
    window.ui()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets, QtGui
import sys
import style


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
        self.adminName = QtWidgets.QLabel(admin_name.capitalize()+'      ')
        self.loginButton = QtWidgets.QPushButton()
        self.loginButton.setIcon(QtGui.QIcon(QtGui.QPixmap("file/Icon/logout.svg")))
        self.exitButton = QtWidgets.QPushButton()
        self.exitButton.setIcon(QtGui.QIcon(QtGui.QPixmap("file/Icon/off.svg")))
        # ########### Layouts >>
        self.mainLayout = QtWidgets.QVBoxLayout()
        # top layout >>
        self.topLayout = QtWidgets.QFrame()
        self.topLayout.setStyleSheet(style.top_layout_home())
        self.topLayoutChild = QtWidgets.QHBoxLayout()
        # bottom layout >>
        self.bottomLayout = QtWidgets.QHBoxLayout()

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
        self.toolBar.addAction(self.adminPanelAction)
        self.toolBar.addSeparator()
        # Add Member >>
        self.toolBar.addAction(self.listContactAction)
        self.toolBar.addSeparator()
        # Sell Product >>
        self.toolBar.addAction(self.addContactAction)
        # Triggered Action >>
        # self.addMember.triggered.connect(self.add_member)
        # self.addProduct.triggered.connect(self.add_product)
        # self.sellProduct.triggered.connect(self.add_sell)

        self.ui()

    def ui(self):
        # set layouts >>
        self.topLayoutChild.addWidget(self.adminImageLabel)
        self.topLayoutChild.addWidget(self.adminName)
        self.topLayoutChild.addWidget(self.toolBar)
        self.topLayoutChild.addStretch()
        self.topLayoutChild.addWidget(self.loginButton)
        self.topLayoutChild.addWidget(self.exitButton)
        self.topLayout.setLayout(self.topLayoutChild)

        self.mainLayout.addWidget(self.topLayout)
        self.mainLayout.addStretch()
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window('aMir')
    window.show()
    sys.exit(app.exec_())

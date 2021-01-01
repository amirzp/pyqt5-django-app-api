from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Home V1')
        self.setGeometry(150, 150, 700, 500)

        # ########### Tool Bar >>
        self.toolBar = QtWidgets.QToolBar("ToolBar")
        self.addProduct = QtWidgets.QAction(QtGui.QIcon("icon/product.svg"), "Admin Panel")
        self.addMember = QtWidgets.QAction(QtGui.QIcon("icon/followers.svg"), "List Contact")
        self.sellProduct = QtWidgets.QAction(QtGui.QIcon("icon/sell.svg"), "Add Contact")
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # Add Product >>
        self.toolBar.addAction(self.addProduct)
        self.toolBar.addSeparator()
        # Add Member >>
        self.toolBar.addAction(self.addMember)
        self.toolBar.addSeparator()
        # Sell Product >>
        self.toolBar.addAction(self.sellProduct)
        # Triggered Action >>
        self.addMember.triggered.connect(self.add_member)
        self.addProduct.triggered.connect(self.add_product)
        self.sellProduct.triggered.connect(self.add_sell)

        self.main.addWidget(self.toolBar)
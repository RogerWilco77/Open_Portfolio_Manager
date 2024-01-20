from PySide6 import QtGui, QtCore, QtWidgets


class Main_Window(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Open Portfolio Manager")
        self.resize(800, 600)
        self.file_menu = self.menuBar().addMenu("&File")
        self.toolbar = self.addToolBar("Some Toolbar content")
        self.toolbar.addAction('New')
        self.status = self.statusBar()
        self.status.showMessage("Status - Ready")

        self.show()

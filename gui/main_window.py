from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QAction


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
        
        self.open_file_action = QtGui.QAction("&Open", self)
        self.open_file_action.triggered.connect(self.open_file_dialog)
        self.file_menu.addAction(self.open_file_action)
        
        
        self.show()
        
        
    def open_file_dialog(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Wähle Symbolliste", "", "Text Dateien (*.txt)")

        if filename:
            self.load_symbols(filename)
            
    def load_symbols(self, filename):
        with open(filename, "r") as f:
            symbols = f.read().splitlines()
            print(symbols)

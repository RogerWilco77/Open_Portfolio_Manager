import sys
from PySide6.QtCore import (Qt, QAbstractTableModel)
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableView
) 
from PySide6.QtGui import QAction




import yfinance as yf
import pandas as pd
import os


class PandasModel(QAbstractTableModel):
   def __init__(self, data):
      self.df = data
   def rowCount(self, parent=None):
      return self.df.shape[1]

   def data(self, index, role=Qt.ItemDataRole):
      if index.isValid():
         if role == Qt.DisplayRole:
            return str(self.df.iloc[index.row(), index.column()])
         return None
   def headerData(self, col, orientation, role):
      if orientation == Qt.Horizontal and role == Qt.DisplayRole:
         return self.df.columns[col]
      return None

      

class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      
      self.setWindowTitle("Open Portfolio Manager")
      self.resize(1200, 800)
      
      self._create_menu_bar()
      self._create_tool_bar()
      self.Create_status_bar()
      
      # Central eidget and layout
      self.central_widget = QWidget()
      self.setCentralWidget(self.central_widget)
      self.central_layout = QVBoxLayout()
      self.central_widget.setLayout(self.central_layout)
      
      # Placeholder for widgets like list view, table, graph
      self.stock_list_view = QTableView()
      self.central_layout.addWidget(self.stock_list_view)
      
      # Setup signals and slots
      self.import_action.triggered.connect(self.import_symbols)
      
   def _create_menu_bar(self):
      # File menu
      self.file_menu = self.menuBar().addMenu("&File")
      
      self.import_action = QAction("Import Symbols", self)
      self.file_menu.addAction(self.import_action)
      
      self.export_action = QAction("Export Results", self)
      self.file_menu.addAction(self.export_action)
      
   def _create_tool_bar(self):
      self.tool_bar = QToolBar()
      self.addToolBar(self.tool_bar)
      
      # Toolbar buttons go here
      
   def _create_status_bar(self):
      self.status_bar = QStatusBar()
      self.setstatusbar(self.status_bar)
      
      # Progress bar
      self.progress = QProgressBar()
      self.status_bar.addPermanentWidget(self.progress)
      
   def import_symbols(self):
      dirname = os.path.dirname(os.path.realpath(__file__))
      fname = QFileDialog.getOpenFilename(self, 'Import Symbols', dirname)
      symbols = self.load_symbols(fname[0])
       
       
       
       
   def load_symbols(self, fname):
      symbols = []
      with open(fname, "r") as f:
         for line in f:
            symbols.append(line.strip())
            print(line)
      return symbols
   
   if __name__ == 'main':
      app = QApplication(sys.argv)
      window = MainWindow()
      window.show()
      sys.exit(app.exec())
       
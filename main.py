import sys
from gui.main_window import Main_Window
from PySide6 import QtWidgets

def main():
   app = QtWidgets.QApplication(sys.argv)
   main_window = Main_Window()
   main_window.show()

   sys.exit(app.exec())
   app.exec()


if __name__ == '__main__':
   main()
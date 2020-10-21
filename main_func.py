from PyQt5 import QtWidgets
from app_class import App
import sys

def main():
	app = QtWidgets.QApplication(sys.argv)
	window = App()
	window.show()
	
	app.exec_()
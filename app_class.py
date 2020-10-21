import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import design
import os

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		#button clicked
		self.Copy.clicked.connect(self.invisible_fullscreen)
		#press escape to cancel
		self.shortcut_cancel = QtWidgets.QShortcut(QKeySequence('Esc'), self)
		self.shortcut_cancel.activated.connect(self.cancel)

		self.rubberband = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle)
		

	#full screen
	def invisible_fullscreen(self, a):
		super().showFullScreen()
		self.Text.clear()
		self.Text.hide()
		self.Copy.hide()
		super().setWindowOpacity(0)

	def cancel(self):
		super().showNormal()
		self.Text.show()
		self.Copy.show()
		super().setWindowOpacity(1)

	def mousePressEvent(self, event):
		self.origin = event.pos()
		self.startX = event.x()
		self.startY = event.y()
		self.rubberband.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()) )
		self.rubberband.show()
		self.rubberband.setWindowOpacity(0.2)
			
	def mouseMoveEvent(self, event):
		if self.rubberband.isVisible():
			self.rubberband.setGeometry(QtCore.QRect(self.origin, event.pos()).normalized())


	def mouseReleaseEvent(self, event):
		if self.rubberband.isVisible():
			self.rubberband.hide()
			
		self.screenshot(self.rubberband.geometry().x(),self.rubberband.geometry().y(),self.rubberband.geometry().width(),self.rubberband.geometry().height())


		super().showNormal()
		self.Text.show()
		self.Copy.show()
		super().setWindowOpacity(1)
	def screenshot(self, x, y, width, height):
		img = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), x, y, width, height)
		img.save("txt.png")
		text = pytesseract.image_to_string(Image.open('txt.png'), lang='eng+rus')
		self.Text.append(text)
		os.remove('txt.png')
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
#img = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), x, y, width, height)
#self.screenshot(event.x(),event.y(), event.x()+self.startX, event.y()-self.startY)


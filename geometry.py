"""Module to draw building geometry and get wind directions"""

#import libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

#define window class
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        #set title
        self.setWindowTitle("Building Geometry Input")
        #setting window geometry
        self.setGeometry(100, 100, 800, 600)
        #create image object for painter
        self.image = QImage(self.size(), QImage.Format_RGB32)
        #set image color to white
        self.image.fill(Qt.white)

        #default brush size
        self.BRUSH_SIZE = 2
        #brush color
        self.BRUSH_COLOR = Qt.black
        #flag to check if currently drawing
        self.FLAG = False

        #trace the point
        self.last_point = QPoint()

    #check mouse click
    def mousePressEvent(self, event):
        #left mouse button pressed
        if event.button() == Qt.LeftButton:
            self.FLAG = True
            self.lastpoint = event.pos()

    def mouseMoveEvent(self, event):
        
        if (event.buttons() & Qt.LeftButton) & self.FLAG:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.BRUSH_COLOR, self.BRUSH_SIZE, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

#Create PyQt5 app
App = QApplication(sys.argv)

#Create an instance of window class
window = Window()

#Show Window
window.show()

#Start app
sys.exit(App.exec())


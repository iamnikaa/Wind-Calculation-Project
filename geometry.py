# """Module to draw building geometry and get wind directions"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.title = "Wind Geometry Calculation"
        self.top= 150
        self.left= 150
        self.width = 700
        self.height = 500
        
        self.InitWindow()

    def InitWindow(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.win = QWidget(self)
        self.label = QLabel(self.win)
        canvas = QPixmap(self.width - 200, self.height)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        
        self.show()
        
    def paintEvent(self, event):
        
        painter = QPainter(self.label.pixmap())
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.red)
        painter.setBrush(Qt.white)

        painter.drawLine(100, 100, 400, 100)
        painter.drawLine(400, 100, 400, 400)
        painter.drawLine(400, 400, 100, 400)
        painter.drawLine(100, 400, 100, 100)
        
        painter.drawText(250, 420, "4")
        painter.drawText(250, 90, "2")
        painter.drawText(80, 250, "1")
        painter.drawText(410, 250, "3")

        e1 = QLineEdit(self.win)
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        
        e1.move(self.win.mapFromParent(QPoint(250, 250)))
        
        painter.end()
        
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.setWindowTitle(str(e.pos()))

    def textchanged(text):
       print("contents of text box: " + text)
	
    def enterPress():
        print("edited")
    
     
App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
              
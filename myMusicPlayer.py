from PyQt5.QtGui import*
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import*
import sys


class Window(QWidget):
	"""docstring for App"""
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)
		self.left = 400
		self.top = 400
		self.width = 400
		self.height = 250
		#set layout. mainLayout is the overall Layout of the app
		self.mainLayout = QVBoxLayout()
		self.mainLayout.setSpacing(5)
		topLayout = QGridLayout()
		displayLayout = QVBoxLayout()
		sliderArea = QGridLayout()
		controlsArea = QGridLayout()
		controlsArea.setSpacing(0)

		self.topBtn = QPushButton("myPlayer")
		menubutton = QMenu()
		#menubutton.addAction()
		self.topBtn.setMenu(menubutton)
		topLayout.addWidget(self.topBtn, 0,0,1,1)
		songTitleBar = QHBoxLayout()
		manipulateWindow = QHBoxLayout()
		topLayout.addLayout(songTitleBar, 0,1)
		self.songtitle = QLabel("Song title will be here,To be implemented with a status bar")
		songTitleBar.addWidget(self.songtitle) 
		topLayout.addLayout(manipulateWindow, 0,2,1,1)
		self.exit_button = QPushButton("exit")
		manipulateWindow.addWidget(self.exit_button)

		self.playBtn = QPushButton()
		self.playBtn.resize(200,200)
		self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
		self.stopBtn = QPushButton()
		self.stopBtn.resize(100,100)
		self.stopBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
		self.nextBtn = QPushButton()
		self.nextBtn.resize(100,100)
		self.nextBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))
		self.prevBtn = QPushButton()
		self.prevBtn.resize(100,100)
		self.prevBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
		self.openCloseBtn = QPushButton("o/c")
		self.openCloseBtn.resize(100,100)
		controlsArea.addWidget(self.playBtn, 0, 0)
		controlsArea.addWidget(self.stopBtn, 0, 1)
		controlsArea.addWidget(self.nextBtn, 0, 2)
		controlsArea.addWidget(self.prevBtn, 0, 3)
		controlsArea.addWidget(self.openCloseBtn, 0, 4)

		self.durationSlider = QSlider(Qt.Horizontal)
		self.volumeControl = QSlider(Qt.Horizontal)
		self.muteBtn = QPushButton()		#mute button will have a very small icon. Icon will change for mute and unmute
		self.muteBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
		sliderArea.addWidget(self.durationSlider, 0, 0, 1, 1)
		sliderArea.addWidget(self.muteBtn, 0, 1, 1, 1)
		sliderArea.addWidget(self.volumeControl, 0, 2, 1, 2)

		self.display = QLabel("DISPLAY WILL BE HERE")
		self.duration = QLabel("DURATION WILL BE HERE TOO")
		displayLayout.addWidget(self.display)
		displayLayout.addWidget(self.duration)

		self.mainLayout.addLayout(topLayout)
		self.mainLayout.addLayout(displayLayout)	
		self.mainLayout.addLayout(sliderArea)
		self.mainLayout.addLayout(controlsArea)
		self.setLayout(self.mainLayout)

	#def addActions(self):
			#pass	
		
app = QApplication(sys.argv)
app.setStyle("Fusion")
palette = QPalette() # Get a copy of the standard palette.
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)
app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
window = Window()
window.show()
sys.exit(app.exec_())

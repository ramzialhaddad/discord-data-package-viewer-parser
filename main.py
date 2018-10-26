"""
Coded by Ramzi Al Haddad (c) 2002-2018

Will be posting how to video soon on my channel. In the meantime, read below!

To use:
	- Install the modules listed; pyqt5, pandas using pip if you don't know how to install modules, just google.
		it's along the lines of pip install pyqt5 || pip install pandas
	- Place this file in the same directory as README.txt and run!
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import csv
import os
import pandas

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1091, 619)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.listWidget = QtWidgets.QListWidget(self.centralwidget)
		self.listWidget.setGeometry(QtCore.QRect(10, 50, 180, 520))
		self.listWidget.setObjectName("listWidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
		self.label.setObjectName("label")
		self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
		self.listWidget_2.setGeometry(QtCore.QRect(200, 50, 880, 520))
		self.listWidget_2.setObjectName("listWidget_2")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(210, 10, 47, 13))
		self.label_2.setObjectName("label_2")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(420, 10, 75, 23))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.findStuff)#---------------------------------------------------#
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1091, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Channels"))
		self.label_2.setText(_translate("MainWindow", "Chats"))
		self.pushButton.setText(_translate("MainWindow", "Find stuff"))

	def findStuff(self):
		# This obvs opens the file as userFile
		with open('account/user.json') as userFile:
			userFileData = json.load(userFile)
			userID = userFileData['id']
			relationships = userFileData['relationships']
		# This is so that we have a matching index for usernames and the UIDs, since in chats it is only UIDs
		relationshipUsers = []
		relationshipIDs = []

		# Hey the name was from discord not me, don't get mad mate
		for x in relationships:
			relationshipUsers.append(x['user']['username'])
			relationshipIDs.append(x['id'])
			self.listWidget.addItem(x['user']['username'])

		print("Number of users ",self.listWidget.count())

		# This stupid function returns the item that got clicked on :/
		# I do have to change this in order to allow for both the text and name to show
		def relationshipThing(self, value):
			x = self.listWidget.selectedItems()
			for y in x:
				if value == "ID":
					return relationshipIDs[relationshipUsers.index(y.text())]
				elif value == "text":
					return y.text()
#-----------------------------------------------------------------------------------------------------#
		with open('servers/index.json') as serverFile:
			serverFileData = json.load(serverFile)
		
		serverNames = []
		serverIDs = []

		for x in serverFileData:
			serverNames.append(serverFileData[x])
			serverIDs.append(x)

		def parseCSV(self, file_path):
			with open(file_path, "r", encoding="utf8") as f:
				readCSV = csv.reader(f, delimiter=',')
				return list(readCSV)

		def findAllTheChats(self):
			messageChannels = [x[0] for x in os.walk("messages") if not x[0] == "messages"]
			allMessages = []
			for channel in messageChannels:
				allMessages += parseCSV(self, channel + "/messages.csv")

			channelIndex = json.load(open("messages/index.json"))

			for zz in channelIndex:
				if channelIndex[zz] != None:
					if relationshipThing(self, "text") in channelIndex[zz]:
						self.listWidget_2.clear()
						df = pandas.read_csv("messages/"+zz+"/messages.csv")
						chats = df.Contents
						chatList = []
						for chat in chats:
							chatList.append(str(chat))
						chatList = list(reversed(chatList))
						del chat
						for chat in chatList:
							self.listWidget_2.addItem(str(chat))
#-----------------------------------------------------------------------------------------------------#
		self.listWidget.itemClicked.connect(lambda: findAllTheChats(self))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
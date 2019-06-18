"""@package interface
Documentation for this module.
Includes the front-end interface and necessary classes and methods for back-end processes.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib import *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import zlib
import random
import time
import sys
import os

class Ui_Form(object):
    """Documentation for a class.

    Includes necessary methods for user interface.
    """

    def setupUi(self, Form):
        """Documentation for a method.

        Initialize all interface elements and their details.
        """

        Form.setObjectName("Form")
        Form.resize(667, 446)
        Form.setStyleSheet("background-color: #393e46; color: #eeeeee")
        self.Form = Form
        self.graph = [0,0,0,0,0,0,0,0]
        self.my_graph = Graph()
        self.work = False
        self.checked_buttons = ""
        self.file_time = ""
        self.datas1 = []
        self.datas2 = []
        self.datas3 = []
        self.datas4 = []
        self.datas5 = []
        self.datas6 = []
        self.datas7 = []
        self.datas8 = []
        self.times1 = []
        self.times2 = []
        self.times3 = []
        self.times4 = []
        self.times5 = []
        self.times6 = []
        self.times7 = []
        self.times8 = []
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.header = QtWidgets.QLabel(Form)
        self.header.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setStyleSheet("color: #00adb5; font-weight: bold; font-size: 21px")
        self.header.setScaledContents(False)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout_3.addWidget(self.header)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.cb1 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cb1.setFont(font)
        self.cb1.setStyleSheet("color: #eeeeee")
        self.cb1.setObjectName("cb1")
        self.gridLayout.addWidget(self.cb1, 0, 0, 1, 1)
        self.cb5 = QtWidgets.QCheckBox(self.widget)
        self.cb5.setStyleSheet("color: #eeeeee")
        self.cb5.setObjectName("cb5")
        self.gridLayout.addWidget(self.cb5, 0, 1, 1, 1)
        self.cb2 = QtWidgets.QCheckBox(self.widget)
        self.cb2.setStyleSheet("color: #eeeeee")
        self.cb2.setObjectName("cb2")
        self.gridLayout.addWidget(self.cb2, 1, 0, 1, 1)
        self.cb6 = QtWidgets.QCheckBox(self.widget)
        self.cb6.setStyleSheet("color: #eeeeee")
        self.cb6.setObjectName("cb6")
        self.gridLayout.addWidget(self.cb6, 1, 1, 1, 1)
        self.cb3 = QtWidgets.QCheckBox(self.widget)
        self.cb3.setStyleSheet("color: #eeeeee")
        self.cb3.setObjectName("cb3")
        self.gridLayout.addWidget(self.cb3, 2, 0, 1, 1)
        self.cb7 = QtWidgets.QCheckBox(self.widget)
        self.cb7.setStyleSheet("color: #eeeeee")
        self.cb7.setObjectName("cb7")
        self.gridLayout.addWidget(self.cb7, 2, 1, 1, 1)
        self.cb4 = QtWidgets.QCheckBox(self.widget)
        self.cb4.setStyleSheet("color: #eeeeee")
        self.cb4.setObjectName("cb4")
        self.gridLayout.addWidget(self.cb4, 3, 0, 1, 1)
        self.cb8 = QtWidgets.QCheckBox(self.widget)
        self.cb8.setStyleSheet("color: #eeeeee")
        self.cb8.setObjectName("cb8")
        self.gridLayout.addWidget(self.cb8, 3, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_button = QtWidgets.QPushButton(self.widget1)
        self.start_button.setStyleSheet("color: #eeeeee; background-color: #00cc00; font-weight: bold; font-size: 26px; height: 50px; width: 180px")
        self.start_button.setCheckable(True)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(self.widget1)
        self.stop_button.setEnabled(False)
        self.stop_button.setStyleSheet("color: #eeeeee; background-color: #cc0000; font-weight: bold; font-size: 26px; height: 50px; width: 180px")
        self.stop_button.setCheckable(True)
        self.stop_button.toggle()
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout.addWidget(self.stop_button)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("background-color: #eeeeee; color: #393e46;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(7, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.see_button = QtWidgets.QPushButton(Form)
        self.see_button.setStyleSheet("color: #00adb5; background-color: #222831; font-weight: bold; font-size: 20px; height: 50px; width: 180px")
        self.see_button.setCheckable(True)
        self.see_button.setObjectName("see_button")
        self.see_button.setEnabled(False)
        self.verticalLayout.addWidget(self.see_button)
        self.manual_button = QtWidgets.QPushButton(Form)
        self.manual_button.setStyleSheet("color: #00adb5; background-color: #222831; font-weight: bold; font-size: 20px; height: 50px; width: 180px")
        self.manual_button.setCheckable(True)
        self.manual_button.setObjectName("manual_button")
        self.verticalLayout.addWidget(self.manual_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.Form.setWindowIcon(QIcon('esogu.ico'))
        self.start_button.clicked.connect(self.start_clicked)
        self.stop_button.clicked.connect(self.stop_clicked)
        self.see_button.clicked.connect(self.see_clicked)
        self.manual_button.clicked.connect(self.manual_clicked)
        self.cb1.stateChanged.connect(self.channels)
        self.cb2.stateChanged.connect(self.channels)
        self.cb3.stateChanged.connect(self.channels)
        self.cb4.stateChanged.connect(self.channels)
        self.cb5.stateChanged.connect(self.channels)
        self.cb6.stateChanged.connect(self.channels)
        self.cb7.stateChanged.connect(self.channels)
        self.cb8.stateChanged.connect(self.channels)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """Documentation for a method.

        Includes the finishing touches for the user interface.
        """

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dynamic Data Monitoring"))
        self.header.setText(_translate("Form", "VOLTAGE MODULE - DYNAMIC DATA MONITORING APP"))
        self.cb1.setText(_translate("Form", "Channel 1"))
        self.cb5.setText(_translate("Form", "Channel 5"))
        self.cb2.setText(_translate("Form", "Channel 2"))
        self.cb6.setText(_translate("Form", "Channel 6"))
        self.cb3.setText(_translate("Form", "Channel 3"))
        self.cb7.setText(_translate("Form", "Channel 7"))
        self.cb4.setText(_translate("Form", "Channel 4"))
        self.cb8.setText(_translate("Form", "Channel 8"))
        self.start_button.setText(_translate("Form", "START"))
        self.stop_button.setText(_translate("Form", "STOP"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Channel"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Data"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "----- V"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "----- V"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Form", "----- V"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Form", "----- V"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Form", "----- V"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Form", "----- V"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Form", "----- V"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("Form", "----- V"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.see_button.setText(_translate("Form", "OPEN LOG FILE"))
        self.manual_button.setText(_translate("Form", "OPEN USER MANUAL"))
        
    def channels(self, state):
        """Documentation for a method.

        A method for keeping selected channels and their order in memory.
        """
        
        if state == Qt.Checked:
            if self.Form.sender().text()[-1] not in self.checked_buttons:
                self.checked_buttons += self.Form.sender().text()[-1]
        else:
            self.checked_buttons = self.checked_buttons.replace(self.Form.sender().text()[-1],"")


    def see_clicked(self):
        """Documentation for a method.

        A method for opening the log file when OPEN LOG FILE button clicked.
        """

        os.startfile(self.file_time)
        self.see_button.toggle()


    def manual_clicked(self):
        """Documentation for a method.

        A method for opening user manual when OPEN USER MANUAL button clicked.
        """

        os.startfile("User Manual.txt")
        self.manual_button.toggle()
    

    def start_clicked(self):
        """Documentation for a method.

        A method for doing necessary processes after START button clicked.
        1) Take imaginary measurements from measure() method
        2) Save them in a list after CRC32 check.
        3) Take average of 50 measurement sample and show them in table and send to append() method from plotting.
        4) Do this work until STOP button clicked.
        """
        
        
        # Checkboxes, start button, see button are disabled and stop button
        # is toggled for security reasons.
        self.cb1.setEnabled(False)
        self.cb2.setEnabled(False)
        self.cb3.setEnabled(False)
        self.cb4.setEnabled(False)
        self.cb5.setEnabled(False)
        self.cb6.setEnabled(False)
        self.cb7.setEnabled(False)
        self.cb8.setEnabled(False)
        self.start_button.setEnabled(False)
        self.see_button.setEnabled(False)
        self.stop_button.toggle()
        self.work = True
        self.my_graph.start_graph()
        
        nom = 1000 #Table and graph are updating in every 1000 samples.
        count = 0 #Counting 1000 samples.
        avg_measurement = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"] #List for updating table and graph.
        
        while self.work == True:
            
            self.stop_button.setEnabled(True) #Stop button is enabled.
            self.file_time = time.asctime().replace(":", ".") + " Log File.txt" #Log file name is determined with current time.
            decoded_data = self.measure() #Measuring data is coming from self.measure() function.
            
            #Calculating CRC32 for data security.
            measurement_str_for_crc_check = decoded_data.split("c")[0][:-1]
            crc_calculated = str(hex(zlib.crc32(bytes(measurement_str_for_crc_check, encoding="ASCII"))))[2:]
    
            measurement_list = decoded_data.split("#") #Received data is splitted in 9 parts(8 channels and CRC32 value).

            if measurement_list[-1][0] == "c":
                crc_sent = measurement_list[-1][1:]
                
            if crc_calculated == crc_sent: #CRC32 check with received and calculated CRC32 values.
                
                if count == nom: #1000 samples are taken, table and graph will be updated.
                    
                    for i in range(8):
                        avg_measurement[i] = str(format((float(avg_measurement[i]) / nom), ".4f")) #Taking average of 1000 samples.
                        
                    if float(avg_measurement[0]) != False: 
                        self.tableWidget.setItem(0,1, QTableWidgetItem(avg_measurement[0] + " V")) #Table is updated.
                        self.tableWidget.item(0,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        QApplication.processEvents()
                        self.graph[0] = float(avg_measurement[0])
                    else:
                        self.tableWidget.setItem(0,1, QTableWidgetItem(""))
                        self.tableWidget.item(0,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        
                    if float(avg_measurement[1]) != False:
                        self.tableWidget.setItem(1,1, QTableWidgetItem(avg_measurement[1] + " V"))
                        self.tableWidget.item(1,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        QApplication.processEvents()
                        self.graph[1] = float(avg_measurement[1])
                    else:
                        self.tableWidget.setItem(1,1, QTableWidgetItem(""))
                        self.tableWidget.item(1,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    if float(avg_measurement[2]) != False:
                        self.tableWidget.setItem(2,1, QTableWidgetItem(avg_measurement[2] + " V"))
                        self.tableWidget.item(2,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        QApplication.processEvents()
                        self.graph[2] = float(avg_measurement[2])
                    else:
                        self.tableWidget.setItem(2,1, QTableWidgetItem(""))
                        self.tableWidget.item(2,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    if float(avg_measurement[3]) != False:
                        self.tableWidget.setItem(3,1, QTableWidgetItem(avg_measurement[3] + " V"))
                        self.tableWidget.item(3,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        QApplication.processEvents()
                        self.graph[3] = float(avg_measurement[3])
                    else:
                        self.tableWidget.setItem(3,1, QTableWidgetItem(""))
                        self.tableWidget.item(3,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    if float(avg_measurement[4]) != False:
                        self.tableWidget.setItem(4,1, QTableWidgetItem(avg_measurement[4] + " V"))
                        self.tableWidget.item(4,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        QApplication.processEvents()
                        self.graph[4] = float(avg_measurement[4])
                    else:
                        self.tableWidget.setItem(4,1, QTableWidgetItem(""))
                        self.tableWidget.item(4,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    if float(avg_measurement[5]) != False:
                        self.tableWidget.setItem(5,1, QTableWidgetItem(avg_measurement[5] + " V"))
                        self.tableWidget.item(5,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        QApplication.processEvents()
                        self.graph[5] = float(avg_measurement[5])
                    else:
                        self.tableWidget.setItem(5,1, QTableWidgetItem(""))
                        self.tableWidget.item(5,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    if float(avg_measurement[6]) != False:
                        self.tableWidget.setItem(6,1, QTableWidgetItem(avg_measurement[6] + " V"))
                        self.tableWidget.item(6,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        QApplication.processEvents()
                        self.graph[6] = float(avg_measurement[6])
                    else:
                        self.tableWidget.setItem(6,1, QTableWidgetItem(""))
                        self.tableWidget.item(6,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    if float(avg_measurement[7]) != False:
                        self.tableWidget.setItem(7,1, QTableWidgetItem(avg_measurement[7] + " V"))
                        self.tableWidget.item(7,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        QApplication.processEvents()
                        self.graph[7] = float(avg_measurement[7])
                    else:
                        self.tableWidget.setItem(7,1, QTableWidgetItem(""))
                        self.tableWidget.item(7,1).setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                        
                    self.my_graph.append(self.graph) #self.my_graph.append function called for updating graph.
                    self.graph = [0,0,0,0,0,0,0,0]
                    count = 0
                    avg_measurement = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"]
                    
                else:
                    if "1" in self.checked_buttons and measurement_list[0][0] == "1": #Checking if Channel 1 checkbox is checked.
                        data1 = measurement_list[0][1:]
                        avg_measurement[0] = str(float(avg_measurement[0]) + float(measurement_list[0][1:]))
                        time1 = time.asctime()
                        self.datas1.append(data1) #Received Channel 1 data is added to datas1 list.
                        self.times1.append(time1) #Current time for received data from Channel 1 is added to times1 list.
                        QApplication.processEvents()
  
                    if "2" in self.checked_buttons and measurement_list[1][0] == "2":
                        data2 = measurement_list[1][1:]
                        avg_measurement[1] = str(float(avg_measurement[1]) + float(measurement_list[1][1:]))
                        time2 = time.asctime()
                        self.datas2.append(data2)
                        self.times2.append(time2)
                        QApplication.processEvents()
                        

                    if "3" in self.checked_buttons and measurement_list[2][0] == "3":
                        data3 = measurement_list[2][1:]
                        avg_measurement[2] = str(float(avg_measurement[2]) + float(measurement_list[2][1:]))
                        time3 = time.asctime()
                        self.datas3.append(data3)
                        self.times3.append(time3)
                        QApplication.processEvents()
                        

                    if "4" in self.checked_buttons and measurement_list[3][0] == "4":
                        data4 = measurement_list[3][1:]
                        avg_measurement[3] = str(float(avg_measurement[3]) + float(measurement_list[3][1:]))
                        time4 = time.asctime()
                        self.datas4.append(data4)
                        self.times4.append(time4)
                        QApplication.processEvents()
                        

                    if "5" in self.checked_buttons and measurement_list[4][0] == "5":
                        data5 = measurement_list[4][1:]
                        avg_measurement[4] = str(float(avg_measurement[4]) + float(measurement_list[4][1:]))
                        time5 = time.asctime()
                        self.datas5.append(data5)
                        self.times5.append(time5)
                        QApplication.processEvents()
                        

                    if "6" in self.checked_buttons and measurement_list[5][0] == "6":
                        data6 = measurement_list[5][1:]
                        avg_measurement[5] = str(float(avg_measurement[5]) + float(measurement_list[5][1:]))
                        time6 = time.asctime()
                        self.datas6.append(data6)
                        self.times6.append(time6)
                        QApplication.processEvents()
                        

                    if "7" in self.checked_buttons and measurement_list[6][0] == "7":
                        data7 = measurement_list[6][1:]
                        avg_measurement[6] = str(float(avg_measurement[6]) + float(measurement_list[6][1:]))
                        time7 = time.asctime()
                        self.datas7.append(data7)
                        self.times7.append(time7)
                        QApplication.processEvents()
                        

                    if "8" in self.checked_buttons and measurement_list[7][0] == "8":
                        data8 = measurement_list[7][1:]
                        avg_measurement[7] = str(float(avg_measurement[7]) + float(measurement_list[7][1:]))
                        time8 = time.asctime()
                        self.datas8.append(data8)
                        self.times8.append(time8)
                        QApplication.processEvents()
                        
                    count += 1
                    
            else:
                print("wrong data received") #Printing error when received CRC32 value different from calculated CRC32 value.
                QApplication.processEvents()
        

    def measure(self):
        """Documentation for a method.

        A simulation method for returning 8 channel measurements and their CRC32 value when it is called.
        """
        
        # 0-10 V imaginary measurement data created.
        # CRC32 of all frame is calculated.
        # Final data is sending when this function is called.
        
        ch1 = str(format(random.uniform(0.0, 10.0), ".4f"))
        ch2 = str(format(random.uniform(0.0, 10.0), ".4f"))
        ch3 = str(format(random.uniform(0.0, 10.0), ".4f"))
        ch4 = str(format(random.uniform(0.0, 10.0), ".4f"))
        ch5 = str(format(random.uniform(0.0, 10.0), ".4f"))
        ch6 = str(format(random.uniform(0.0, 10.0), ".4f"))
        ch7 = str(format(random.uniform(0.0, 10.0), ".4f"))
        ch8 = str(format(random.uniform(0.0, 10.0), ".4f"))
        
        meas = "1" + ch1 + "#" + "2" + ch2 + "#" + "3" + ch3 + "#" + "4" + ch4 + "#" + "5" + ch5 + "#" + "6" + ch6 + "#" + "7" + ch7 + "#" + "8" + ch8
        
        crc = str(hex(zlib.crc32(bytes(meas, encoding="ASCII"))))[2:]
        
        return meas + "#c" + crc


    def stop_clicked(self):
        """Documentation for a method.

        A method for closing the graph and creating the log file when STOP button clicked.
        """
        
        #Checkboxes, start and see buttons is enabled for next measurement.
        self.my_graph.close_graph()
        self.cb1.setEnabled(True)
        self.cb2.setEnabled(True)
        self.cb3.setEnabled(True)
        self.cb4.setEnabled(True)
        self.cb5.setEnabled(True)
        self.cb6.setEnabled(True)
        self.cb7.setEnabled(True)
        self.cb8.setEnabled(True)
        self.start_button.setEnabled(True)
        self.start_button.toggle()
        self.stop_button.setEnabled(False)
        self.work = False
        
        #Log file is created with datas and times lists.
        f = open(self.file_time, "a")
        f.write("TIME\t\t\t\tCHANNEL 1\tCHANNEL 2\tCHANNEL 3\tCHANNEL 4\tCHANNEL 5\tCHANNEL 6\tCHANNEL 7\tCHANNEL 8\n")
        max_data = max(len(self.datas1), len(self.datas2), len(self.datas3), len(self.datas4), len(self.datas5), len(self.datas6), len(self.datas7), len(self.datas8))
        for i in range(len(self.datas1), max_data):
            self.datas1.append("-----")
        for i in range(len(self.datas2), max_data):
            self.datas2.append("-----")
        for i in range(len(self.datas3), max_data):
            self.datas3.append("-----")
        for i in range(len(self.datas4), max_data):
            self.datas4.append("-----")
        for i in range(len(self.datas5), max_data):
            self.datas5.append("-----")
        for i in range(len(self.datas6), max_data):
            self.datas6.append("-----")
        for i in range(len(self.datas7), max_data):
            self.datas7.append("-----")
        for i in range(len(self.datas8), max_data):
            self.datas8.append("-----")
        times_list = [self.times1, self.times2, self.times3, self.times4, self.times5, self.times6, self.times7, self.times8 ]
        time_data = []
        for t in times_list:
            if len(t) == max_data:
                time_data = t
        for k in range(max_data):
            f.write(time_data[k] + "\t" + self.datas1[k] + "\t\t" +  self.datas2[k] + "\t\t" + self.datas3[k] + "\t\t" + self.datas4[k] + "\t\t" + self.datas5[k] + "\t\t" + self.datas6[k] + "\t\t" + self.datas7[k] + "\t\t" + self.datas8[k] + "\n")
        
        #See button is enabled after log file is created.
        self.see_button.setEnabled(True)
        
        #Datas and times lists are resetted for next meaurement.
        self.datas1 = []
        self.datas2 = []
        self.datas3 = []
        self.datas4 = []
        self.datas5 = []
        self.datas6 = []
        self.datas7 = []
        self.datas8 = []
        self.times1 = []
        self.times2 = []
        self.times3 = []
        self.times4 = []
        self.times5 = []
        self.times6 = []
        self.times7 = []
        self.times8 = []
        


class Graph:
    """Documentation for a class.

    Includes necessary methods for plotting the graph.
    """

    def __init__(self):
        """The constructor for initializing graph refresher."""
        self.graph_refresh_counter = 0
        

    def start_graph(self):
        """Documentation for a method.
        
        A method for open the graph and set details like axis, title, ticks, labels, legend.
        """

        self.xdata = []
        self.y1data = []
        self.y2data = []
        self.y3data = []
        self.y4data = []
        self.y5data = []
        self.y6data = []
        self.y7data = []
        self.y8data = []
        plt.show()
        
        #Ticks, labels, legends and title are determined.
        plt.xticks(np.arange(0, 151, 1), rotation=90)
        plt.yticks(np.arange(0, 10.25, 0.25))
        self.axes = plt.gca()
        self.axes.set_ylabel("Voltage (V)")
        self.axes.set_xlabel("Time (s)")
        self.axes.set_title("Dynamic Data Monitoring with Start Time: " + time.asctime().replace(":", "."))
        self.axes.set_xlim(left = 0)
        self.axes.set_ylim(bottom = 0)
        self.axes.grid(color="#eeeeee")
        self.line1, = self.axes.plot(self.xdata, self.y1data, label="Channel 1")
        self.line2, = self.axes.plot(self.xdata, self.y2data, label="Channel 2")
        self.line3, = self.axes.plot(self.xdata, self.y3data, label="Channel 3")
        self.line4, = self.axes.plot(self.xdata, self.y4data, label="Channel 4")
        self.line5, = self.axes.plot(self.xdata, self.y5data, label="Channel 5")
        self.line6, = self.axes.plot(self.xdata, self.y6data, label="Channel 6")
        self.line7, = self.axes.plot(self.xdata, self.y7data, label="Channel 7")
        self.line8, = self.axes.plot(self.xdata, self.y8data, label="Channel 8")
        self.axes.legend(handles=[self.line1, self.line2, self.line3,self.line4,self.line5,self.line6, self.line7, self.line8])
        self.k = 0
        

    def append(self,i):
        """Documentation for a method.
        
        A method for appending the new data came from start_clicked() function and refresh the plot until 150 data come.
        """

        if self.graph_refresh_counter == 150: #Graph is refreshed when 150 appends are occurred.
            
            #Title is updated with current time.
            self.axes.set_title("Voltage(V) - Time(s) Plot with Start Time: " + time.asctime().replace(":", "."))
            self.k = 0
            self.xdata = []
            self.y1data = []
            self.y2data = []
            self.y3data = []
            self.y4data = []
            self.y5data = []
            self.y6data = []
            self.y7data = []
            self.y8data = []
            self.xdata.append(self.k)
            self.y1data.append(i[0])
            self.y2data.append(i[1])
            self.y3data.append(i[2])
            self.y4data.append(i[3])
            self.y5data.append(i[4])
            self.y6data.append(i[5])
            self.y7data.append(i[6])
            self.y8data.append(i[7])
            self.line1.set_xdata(self.xdata)
            self.line1.set_ydata(self.y1data)
            self.line2.set_xdata(self.xdata)
            self.line2.set_ydata(self.y2data)
            self.line3.set_xdata(self.xdata)
            self.line3.set_ydata(self.y3data)
            self.line4.set_xdata(self.xdata)
            self.line4.set_ydata(self.y4data)
            self.line5.set_xdata(self.xdata)
            self.line5.set_ydata(self.y5data)
            self.line6.set_xdata(self.xdata)
            self.line6.set_ydata(self.y6data)
            self.line7.set_xdata(self.xdata)
            self.line7.set_ydata(self.y7data)
            self.line8.set_xdata(self.xdata)
            self.line8.set_ydata(self.y8data)
            self.k += 1
            self.graph_refresh_counter = 0
            plt.draw()
            plt.pause(1e-170)
        
        else:
            
            #Graph is updated with received append data.
            self.xdata.append(self.k)
            self.y1data.append(i[0])
            self.y2data.append(i[1])
            self.y3data.append(i[2])
            self.y4data.append(i[3])
            self.y5data.append(i[4])
            self.y6data.append(i[5])
            self.y7data.append(i[6])
            self.y8data.append(i[7])
            self.line1.set_xdata(self.xdata)
            self.line1.set_ydata(self.y1data)
            self.line2.set_xdata(self.xdata)
            self.line2.set_ydata(self.y2data)
            self.line3.set_xdata(self.xdata)
            self.line3.set_ydata(self.y3data)
            self.line4.set_xdata(self.xdata)
            self.line4.set_ydata(self.y4data)
            self.line5.set_xdata(self.xdata)
            self.line5.set_ydata(self.y5data)
            self.line6.set_xdata(self.xdata)
            self.line6.set_ydata(self.y6data)
            self.line7.set_xdata(self.xdata)
            self.line7.set_ydata(self.y7data)
            self.line8.set_xdata(self.xdata)
            self.line8.set_ydata(self.y8data)
            self.graph_refresh_counter += 1
            self.k += 1
            plt.draw()
            plt.pause(1e-170)


    def close_graph(self):
        """Documentation for a method.
        
        A method for closing the graph.
        """
        plt.close()
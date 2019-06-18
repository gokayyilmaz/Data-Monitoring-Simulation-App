# -*- coding: utf-8 -*-
"""@package main
Documentation for this module.
Driver program for Dynamic Data Monitoring Simulation
"""

from PyQt5 import QtWidgets
from interface import Ui_Form ###
import sys

class mywindow(QtWidgets.QWidget):
    """Documentation for a class.
    
    Includes necessary method for drive the program.
    """    
    def __init__(self):
        """The constructor for drive the program with calling super and base classes."""
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
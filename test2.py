#!/usr/bin/env python

"""
Interface to get the specific  weight of each of the 5 containers
start_measurment_button starts thread /thread_worker
transfer_data button start query and send data to database
"""

import sys
import sqlite3

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtSql as qsql

from  PyQt5 import sip

class AddWidget(qtw.QWidget):
    '''
    Interface with embedded SQL functions
    '''

    # Attribut Signal

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # your code will go here

        self.mylist = []
        # interface

        # position
        qtRectangle = self.frameGeometry()
        centerPoint = qtw.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        # size
        self.resize(700, 410)
        # frame title
        self.setWindowTitle("add  Widget")
        # heading
        heading_label = qtw.QLabel('add Widget')
        heading_label.setAlignment(qtc.Qt.AlignHCenter | qtc.Qt.AlignTop)

        # add Button
        self.addwidget_button = qtw.QPushButton("add Widget")
        self.getlistof_button = qtw.QPushButton("deleate")

        self.main_layout = qtw.QGridLayout()
        self.main_layout.addWidget(self.getlistof_button,0,0)
        self.main_layout.addWidget(self.addwidget_button, 1, 0)

        self.setLayout(self.main_layout)

        self.show()

        # functionality
        self.addwidget_button.clicked.connect(self.add_widget)
        self.getlistof_button.clicked.connect(self.deleate_widgets_try)


    def add_widget(self):
        self.my_lineedit = qtw.QLineEdit()
        self.mylist.append(self.my_lineedit)
        self.main_layout.addWidget(self.my_lineedit)


    def deleate_widgets(self):
        widgets = (self.main_layout.itemAt(i).widget() for i in range(self.main_layout.count()))
        for widget in widgets:
            if isinstance(widget, qtw.QLineEdit):
                print(widget)
                print("linedit: %s  - %s" %(widget.objectName(), widget.text()))
                widget.deleteLater() # alle objects


    # 
    def deleate_widgets_try(self):
        widgets = (self.main_layout.itemAt(i).widget() for i in range(self.main_layout.count()))
        my_iter = iter(widgets)
    
        if isinstance(my_iter, qtw.QLineEdit):
            next(my_iter.deleteLater()) # alle objects)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = AddWidget()
    sys.exit(app.exec_())
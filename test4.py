import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QMainWindow, QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import os
import sys
import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import numpy as np

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic') 

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.mainGrid = QGridLayout()

        self.mainGrid.addWidget(self.graph(), 0, 0)
        # self.mainGrid.addWidget(self.graph(), 0, 1)

        self.setWindowTitle('BOT-2 Result')
        self.setGeometry(300, 300, 1000, 1000)
        self.setLayout(self.mainGrid)
        self.show()


    def graph(self):
        x = np.arange(5)
        values = [50, 60, 70, 30, 50]
        category = ["", "미세운동 조절", "손 상지 협응", "신체 협응", "근력 및 민첩성", "총점"]

        self.canvas = FigureCanvas(Figure(figsize=(4, 3)))

        self.ax = self.canvas.figure.subplots()
        self.ax.bar(x, values, width=0.5)
        self.ax.set_xticklabels(category)
        self.ax.axis([-1, 5, 20, 80])
        self.ax.grid(True, axis='y')
        self.ax.set_ylabel("30(매우낮음) 40(낮음) 50(평균) 60(높음) 70(매우높음)")


        self.graphGroupBox = QGroupBox("결과지 출력")

        self.graphGrid = QGridLayout()

        self.graphGrid.addWidget(self.canvas, 0, 0)

        self.graphGroupBox.setLayout(self.graphGrid)

        return self.graphGroupBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
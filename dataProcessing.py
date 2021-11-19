import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle('File Open Test')

        self.pushButton = QPushButton('File Open')
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])
        print(fname[0])
        excel = pd.read_excel(fname[0])
        self.excelData = pd.DataFrame.to_numpy(excel)

        # print(self.excelData)

        self.dataProcessing()

    def dataProcessing(self):
        findStartIndex = np.where(self.excelData == "유형")
        startIndex = int(findStartIndex[0])
        endIndex = len(self.excelData)

        # print(startIndex, endIndex)
        
        name = "허태율"
        try:
            if name in self.excelData:
                findRow = np.where(self.excelData == name)
                row = int(findRow[0])
                personData = []
                for i in self.excelData[row]:
                    personData.append(i)
                # print(personData)
                self.requiredData = personData[0:6]
                self.sub1Raw = personData[6:13]
                self.sub2Raw = personData[13:21]
                self.sub3Raw = personData[21:30]
                self.sub4Raw = personData[30:44]
                self.sub5Raw = personData[44:62]
                self.sub6Raw = personData[62:72]
                self.sub7Raw = personData[72:86]
                self.sub8Raw = personData[86:95]

                # print(self.sub1Raw)
                # print(self.sub2Raw)
                # print(self.sub3Raw)
                # print(self.sub4Raw)
                # print(self.sub5Raw)
                # print(self.sub6Raw)
                # print(self.sub7Raw)
                # print(self.sub8Raw)
                print(12)
                self.sub1RawToPoint()
                print(1)
            else:
                pass
        except:
            pass

    def sub1RawToPoint(self):
        self.sub1Point = []
        self.sub1TotalPoint = 0
        # Subtest 1: Find Motor Precision
            # Filing in Shapes
        for i in range(0, 2):
            if self.sub1Raw[i] == 0:
                self.sub1Point.append(0)
            elif self.sub1Raw[i] == 1:
                self.sub1Point.append(1)
            elif self.sub1Raw[i] == 2:
                self.sub1Point.append(2)
            elif self.sub1Raw[i] == 3:
                self.sub1Point.append(3)
            else:
                pass
            self.sub1TotalPoint += self.sub1Point[i]
        
            # Drawing Lines Through Paths
        for i in range(2, 4):
            if self.sub1Raw[i] == 0:
                self.sub1Point.append(7)
            elif self.sub1Raw[i] == 1:
                self.sub1Point.append(6)
            elif self.sub1Raw[i] <= 3:
                self.sub1Point.append(5)
            elif self.sub1Raw[i] <= 5:
                self.sub1Point.append(4)
            elif self.sub1Raw[i] <= 9:
                self.sub1Point.append(3)
            elif self.sub1Raw[i] <= 14:
                self.sub1Point.append(2)
            elif self.sub1Raw[i] <= 20:
                self.sub1Point.append(1)
            else:
                self.sub1Point.append(0)
            
            self.sub1TotalPoint += self.sub1Point[i]

            # Connect Dots, Folding Paper, Cutting Out a Circle
        for i in range(4, 7):
            if  self.sub1Raw[i] == 0:
                self.sub1Point.append(0)
            elif  self.sub1Raw[i] <= 2:
                self.sub1Point.append(1)
            elif  self.sub1Raw[i] <= 4:
                self.sub1Point.append(2)
            elif  self.sub1Raw[i] <= 6:
                self.sub1Point.append(3)
            elif  self.sub1Raw[i] <= 8:
                self.sub1Point.append(4)
            elif  self.sub1Raw[i] <= 10:
                self.sub1Point.append(5)
            elif  self.sub1Raw[i] == 11:
                self.sub1Point.append(6)
            elif  self.sub1Raw[i] == 12:
                self.sub1Point.append(7)

            self.sub1TotalPoint += self.sub1Point[i]
    
        print(self.sub1TotalPoint)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
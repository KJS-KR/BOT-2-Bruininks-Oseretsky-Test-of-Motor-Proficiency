# import pandas as pd

# path = "C:\\Users\\KJS\\Desktop\\CPD\\"
# file_1 = "BOT-2_raw_score.xlsx"
# file_2 = "test_file.xlsx"

# row, column = 5, 0

# data_pd = pd.read_excel(file_1)
# data_np = pd.DataFrame.to_numpy(data_pd)
# print(data_np[row][0], data_np[row][1])

# requiredData = []
# subtest1Data = []
# subtest2Data = []
# subtest3Data = []
# subtest4Data = []
# subtest5Data = []
# subtest6Data = []
# subtest7Data = []
# subtest8Data = []

import sys
import pandas as pd
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("File Open Test")

        self.pushButton = QPushButton("File Open")
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
        excelData = pd.DataFrame.to_numpy(excel)

        print(excelData)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

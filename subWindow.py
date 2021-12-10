import sys
# import PyQt5
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

main_ui = uic.loadUiType('_uiFiles/main.ui')[0]


class OptionWindow(QDialog):
    def __init__(self, parent):  #부모 window 설정
        super(OptionWindow, self).__init__(parent)
        option_ui = '_uiFiles/option.ui'
        uic.loadUi(option_ui, self)
        self.show()


class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_option.clicked.connect(self.clicked_option)

    def clicked_option(self): 	# 버튼 클릭 이벤트
        OptionWindow(self)	#OptionWindows 클래스 self로 부모 윈도우에 대한 정보를 넘겨줌


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainWindow()
    main_dialog.show()
    app.exec_()
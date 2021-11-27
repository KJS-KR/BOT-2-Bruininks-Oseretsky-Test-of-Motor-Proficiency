import os
import sys
import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import numpy as np

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.fname = [""]
        self.check = 0

    def initUI(self):
        self.mainGrid = QGridLayout()

        self.mainGrid.addWidget(self.createExcelDataFields(), 0, 0)
        self.mainGrid.addWidget(self.createRequiredFields(),0, 2)
        self.mainGrid.addWidget(self.createResultFields(), 0, 3)
        self.mainGrid.addWidget(self.createSubTest1Fields(), 1, 0)
        self.mainGrid.addWidget(self.createSubTest2Fields(), 1, 1)
        self.mainGrid.addWidget(self.createSubTest3Fields(), 1, 2)
        self.mainGrid.addWidget(self.createSubTest4Fields(), 1, 3)
        self.mainGrid.addWidget(self.createSubTest5Fields(), 2, 0)
        self.mainGrid.addWidget(self.createSubTest6Fields(), 2, 1)
        self.mainGrid.addWidget(self.createSubTest7Fields(), 2, 2)
        self.mainGrid.addWidget(self.createSubTest8Fields(), 2, 3)
        self.mainGrid.addWidget(self.createFineMaualControlFields(), 3, 0)
        self.mainGrid.addWidget(self.createManualCoordinationFields(), 3, 1)
        self.mainGrid.addWidget(self.createBodyCoordinationFields(), 3, 2)
        self.mainGrid.addWidget(self.createStrengthAndAgilityFields(), 3, 3)

        self.setWindowTitle('My First Application')
        self.setGeometry(300, 300, 1000, 1000)
        self.setLayout(self.mainGrid)
        self.show()

    def createExcelDataFields(self):
        self.excelGroupBox = QGroupBox("파일 선택")

        self.excelGrid = QGridLayout()

        excelButton = QPushButton("파일을 선택해주세요.(필수, 엑셀만)")
        excelButton.clicked.connect(self.FileButtonClicked)
        excelButton.setMaximumWidth(300)
        self.excelGrid.addWidget(excelButton, 0, 0)

        self.excelGroupBox.setLayout(self.excelGrid)

        return self.excelGroupBox

    def FileButtonClicked(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self)
            excel = pd.read_excel(self.fname[0])
            self.excelData = pd.DataFrame.to_numpy(excel)
            self.excelGrid.addWidget(QLabel("파일명 : " + self.fname[0]), 2, 0)

            self.nameList = []
            for i in range(len(self.excelData)-5):
                self.nameList.append(self.excelData[i+5][1])

            excelButton = QPushButton("인원 선택 버튼")
            excelButton.clicked.connect(self.selectUserDialog)
            excelButton.setMaximumWidth(150)

            self.excelGrid.addWidget(excelButton, 3, 0)

            self.excelGroupBox.setLayout(self.excelGrid)

        except:
            QMessageBox.warning(self, "에러", "엑셀 파일이 아니거나, 선택된 파일이 없습니다.")

        return self.excelGroupBox

    def getExcelData(self):
        self.requiredData = self.userData[0:6]
        self.sub1Raw = self.userData[6:13]
        self.sub2Raw = self.userData[13:21]
        self.sub3Raw = self.userData[21:30]
        self.sub4Raw = self.userData[30:44]
        self.sub5Raw = self.userData[44:62]
        self.sub6Raw = self.userData[62:72]
        self.sub7Raw = self.userData[72:86]
        self.sub8Raw = self.userData[86:96]

        self.inputRequiredData()
        self.inputSub1RawPoint()
        self.inputSub2RawPoint()
        self.inputSub3RawPoint()
        self.inputSub4RawPoint()
        self.inputSub5RawPoint()
        self.inputSub6RawPoint()
        self.inputSub7RawPoint()
        self.inputSub8RawPoint()

        self.scaleCombined()

        # self.requiredGroupBox.setLayout(self.requiredGrid)
        # return self.requiredGroupBox

    def selectUserDialog(self):
        nameStr = ', '.join(self.nameList)
        self.inputName, ok = QInputDialog.getText(self, '이름을 입력하시오.', nameStr)
        if self.check > 0: # 위젯 리셋
            self.requiredGrid.itemAt(6).widget().deleteLater()
            self.requiredGrid.itemAt(7).widget().deleteLater()
            self.requiredGrid.itemAt(8).widget().deleteLater()
            self.requiredGrid.itemAt(9).widget().deleteLater()

        for i in range(len(self.nameList)):
            if self.inputName in self.nameList[i]:
                self.name = self.nameList[i]
                for i in range(len(self.excelData)):
                    if self.name in self.excelData[i]:
                        self.userData = self.excelData[i]
                        self.getExcelData()
                        self.check += 1
                        break
            
    def createRequiredFields(self):
        self.nameField, self.ageField, self.maleField, self.femaleField, self.birthDateField, self.testDateField = "", 0, "", "", 0, 0

        self.requiredGroupBox = QGroupBox("필수입력사항")

        self.requiredGrid = QGridLayout()
        gridPart1 = QGroupBox("성별")
        gridPart2 = QGroupBox("유형 선택")

        gridLayout1 = QBoxLayout(QBoxLayout.TopToBottom)
        gridLayout2 = QBoxLayout(QBoxLayout.TopToBottom)

        gridPart1.setLayout(gridLayout1)
        gridPart2.setLayout(gridLayout2)

        self.requiredGrid.addWidget(QLabel("이름 :"), 0, 0)
        # self.nameField = QLineEdit(self)
        # # name.setMaximumWidth(70)
        # self.requiredGrid.addWidget(self.nameField, 0, 1)

        self.requiredGrid.addWidget(QLabel("연령 :"), 1, 0)
        # self.ageField = QLineEdit(self)
        # # age.setMaximumWidth(70)
        # self.requiredGrid.addWidget(self.ageField, 1, 1)

        self.requiredGrid.addWidget(QLabel("생년월일 :"), 2, 0)
        # self.birthDateField = QLineEdit(self)
        # # birthDate.setMaximumWidth(70)
        # self.requiredGrid.addWidget(self.birthDateField, 2, 1)

        self.requiredGrid.addWidget(QLabel("검사일 :"), 3, 0)
        # self.testDateField = QLineEdit(self)
        # # testDate.setMaximumWidth(70)
        # self.requiredGrid.addWidget(self.testDateField, 3, 1)

        self.maleField = QRadioButton("남자")
        self.femaleField = QRadioButton("여자")
        gridLayout1.addWidget(self.maleField)
        gridLayout1.addWidget(self.femaleField)

        self.onlyMaleField = QRadioButton("남자 그룹")
        self.onlyFemaleField = QRadioButton("여자 그룹")
        self.combinedField = QRadioButton("혼성 그룹")
        gridLayout2.addWidget(self.onlyMaleField)
        gridLayout2.addWidget(self.onlyFemaleField)
        gridLayout2.addWidget(self.combinedField)

        # groupBox.setMaximumWidth(300)
        self.requiredGrid.addWidget(gridPart1, 0, 2, 4, 1)
        self.requiredGrid.addWidget(gridPart2, 0, 3, 4, 1)

        self.requiredGroupBox.setLayout(self.requiredGrid)

        return self.requiredGroupBox

    def createSubTest1Fields(self):
        self.sub1GroupBox = QGroupBox("Subtest 1: Fine Moter Precision")
        self.sub1Grid = QGridLayout()

        self.sub1Grid.addWidget(QLabel("항목"), 0, 0, alignment=QtCore.Qt.AlignCenter)
        self.sub1Grid.addWidget(QLabel("Raw Score"), 0, 1, alignment=QtCore.Qt.AlignCenter)
        self.sub1Grid.addWidget(QLabel("Point Score"), 0, 2, alignment=QtCore.Qt.AlignCenter)

        self.sub1Grid.addWidget(QLabel("Filling in Shapes -- Circle : "), 1, 0)
        self.sub1Grid.addWidget(QLabel("Filling in Shapes --Star : "), 2, 0)
        self.sub1Grid.addWidget(QLabel("Drawing Lines Through Paths -- Crooked : "), 3, 0)
        self.sub1Grid.addWidget(QLabel("Drawing Lines Through Paths -- Curved : "), 4, 0)
        self.sub1Grid.addWidget(QLabel("Connecting Dots : "), 5, 0)
        self.sub1Grid.addWidget(QLabel("Folding Paper : "), 6, 0)
        self.sub1Grid.addWidget(QLabel("Cutting Out a Circle : "), 7, 0)
        self.sub1Grid.addWidget(QLabel("Total Point Score Subtest 1 (max=41) : "), 11, 0)

        # subTest1 = []
        # for i in range(7):
        #     subTest1.append(QLineEdit(self))
        #     subTest1[i].setText("")
        #     # subTest1[i].setMaximumWidth(70)
        # for i in range(7):
        #     self.sub1Grid.addWidget(subTest1[i], i + 1, 1)

        # convBtn = QPushButton()
        # convBtn.setText("변환")
        # self.sub1Grid.addWidget(convBtn, 11, 1)

        self.sub1GroupBox.setLayout(self.sub1Grid)

        return self.sub1GroupBox

    def createSubTest2Fields(self):
        self.sub2GroupBox = QGroupBox("Subtest 2: Fine Moter intergration")
        self.sub2Grid = QGridLayout()

        self.sub2Grid.addWidget(QLabel("항목"), 0, 0, alignment=QtCore.Qt.AlignCenter)
        self.sub2Grid.addWidget(QLabel("Raw Score"), 0, 1, alignment=QtCore.Qt.AlignCenter)
        self.sub2Grid.addWidget(QLabel("Point Score"), 0, 2, alignment=QtCore.Qt.AlignCenter)

        self.sub2Grid.addWidget(QLabel("Copying a Circle : "), 1, 0)
        self.sub2Grid.addWidget(QLabel("Copying a Square : "), 2, 0)
        self.sub2Grid.addWidget(QLabel("Copying Overlapping Circles : "), 3, 0)
        self.sub2Grid.addWidget(QLabel("Copying a Wavy Line : "), 4, 0)
        self.sub2Grid.addWidget(QLabel("Copying a Triangle : "), 5, 0)
        self.sub2Grid.addWidget(QLabel("Copying a Diamond : "), 6, 0)
        self.sub2Grid.addWidget(QLabel("Copying a Star : "), 7, 0)
        self.sub2Grid.addWidget(QLabel("Copying Overlapping Pencils : "), 8, 0)
        self.sub2Grid.addWidget(QLabel("Total Point Score Subtest 2 (max=40) : "), 11, 0)

        # subTest2 = []
        # for i in range(8):
        #     subTest2.append(QLineEdit(self))
        #     subTest2[i].setText("")
        # for i in range(8):
        #     grid.addWidget(subTest2[i], i + 1, 1)

        # convBtn = QPushButton()
        # convBtn.setText("변환")
        # self.sub2Grid.addWidget(convBtn, 11, 1)

        self.sub2GroupBox.setLayout(self.sub2Grid)

        return self.sub2GroupBox

    def createSubTest3Fields(self):
        self.sub3GroupBox = QGroupBox("Subtest 3: Manual Dexterity")
        self.sub3Grid = QGridLayout()

        self.sub3Grid.addWidget(QLabel("항목"), 0, 0, alignment=QtCore.Qt.AlignCenter)
        self.sub3Grid.addWidget(QLabel("Raw Score"), 0, 1, alignment=QtCore.Qt.AlignCenter)
        self.sub3Grid.addWidget(QLabel("Point Score"), 0, 2, alignment=QtCore.Qt.AlignCenter)

        self.sub3Grid.addWidget(QLabel("Making Dots in Circles : "), 1, 0)
        self.sub3Grid.addWidget(QLabel("Transferring Pennies : "), 2, 0)
        self.sub3Grid.addWidget(QLabel("Placing Pegs into a Pegboard : "), 3, 0)
        self.sub3Grid.addWidget(QLabel("Sorting Cards : "), 4, 0)
        self.sub3Grid.addWidget(QLabel("Sorting Blocks : "), 5, 0)
        self.sub3Grid.addWidget(QLabel("Total Point Score Subtest 3 (max=45) : "), 11, 0)

        # subTest3 = []
        # for i in range(6):
        #     subTest3.append(QLineEdit(self))
        #     subTest3[i].setText("")
        # for i in range(6):
        #     grid.addWidget(subTest3[i], i + 1, 1)

        # convBtn = QPushButton()
        # convBtn.setText("변환")
        # grid.addWidget(convBtn, 11, 1)

        self.sub3GroupBox.setLayout(self.sub3Grid)

        return self.sub3GroupBox

    def createSubTest4Fields(self):
        self.sub4GroupBox = QGroupBox("Subtest 4: Bilateral Coordination")
        self.sub4Grid = QGridLayout()

        self.sub4Grid.addWidget(QLabel("항목"), 0, 0, alignment=QtCore.Qt.AlignCenter)
        self.sub4Grid.addWidget(QLabel("Raw Score"), 0, 1, alignment=QtCore.Qt.AlignCenter)
        self.sub4Grid.addWidget(QLabel("Point Score"), 0, 2, alignment=QtCore.Qt.AlignCenter)

        self.sub4Grid.addWidget(
            QLabel("Touching Nose with Index Fingers -- Eyes Closed : "), 1, 0
        )
        self.sub4Grid.addWidget(QLabel("Jumping Jacks : "), 2, 0)
        self.sub4Grid.addWidget(QLabel("Jumping in Place -- Same Sides Synchronized : "), 3, 0)
        self.sub4Grid.addWidget(
            QLabel("Jumping in Place -- Opposite Sides Synchronized : "), 4, 0
        )
        self.sub4Grid.addWidget(QLabel("Pivoting Thumbs and Index Fingers : "), 5, 0)
        self.sub4Grid.addWidget(
            QLabel("Tapping Feet and Fingers -- Same Sides Synchronized : "), 6, 0
        )
        self.sub4Grid.addWidget(
            QLabel("Tapping Feet and Fingers -- Opposite Sides Synchronized : "), 7, 0
        )
        self.sub4Grid.addWidget(QLabel("Total Point Score Subtest 4 (max=24) : "), 11, 0)

        # subTest2 = []
        # for i in range(6):
        #     subTest2.append(QLineEdit(self))
        #     subTest2[i].setText("")
        # for i in range(6):
        #     grid.addWidget(subTest2[i], i + 1, 1)

        # convBtn = QPushButton()
        # convBtn.setText("변환")
        # grid.addWidget(convBtn, 11, 1)

        self.sub4GroupBox.setLayout(self.sub4Grid)

        return self.sub4GroupBox

    def createSubTest5Fields(self):
        self.sub5GroupBox = QGroupBox("Subtest 5: Balance")
        self.sub5Grid = QGridLayout()

        self.sub5Grid.addWidget(QLabel("항목"), 0, 0, alignment=QtCore.Qt.AlignCenter)
        self.sub5Grid.addWidget(QLabel("Raw Score"), 0, 1, alignment=QtCore.Qt.AlignCenter)
        self.sub5Grid.addWidget(QLabel("Point Score"), 0, 2, alignment=QtCore.Qt.AlignCenter)

        self.sub5Grid.addWidget(
            QLabel("Standing with Feet Apart on a Line -- Eyes Open: "), 1, 0
        )
        self.sub5Grid.addWidget(QLabel("Walking Forward on a Line : "), 2, 0)
        self.sub5Grid.addWidget(QLabel("Standing on One Leg on a Line -- Eyes Open : "), 3, 0)
        self.sub5Grid.addWidget(QLabel("Standing on One Leg on a Line -- Eyes Closed : "), 4, 0)
        self.sub5Grid.addWidget(QLabel("Walking Forward Heel-to-Toe on a Line : "), 5, 0)
        self.sub5Grid.addWidget(QLabel("Standing on One Leg on a Line -- Eyes Closed : "), 6, 0)
        self.sub5Grid.addWidget(
            QLabel("Standing on One Leg on a Balance Beam -- Eyes Open : "), 7, 0
        )
        self.sub5Grid.addWidget(QLabel("Standing Heel-to-Toe on a Balance Beam : "), 8, 0)
        self.sub5Grid.addWidget(
            QLabel("Starnding on One Leg on a Balance Beam -- Eyes Closed : "), 9, 0
        )
        self.sub5Grid.addWidget(QLabel("Total Point Score Subtest 5 (max=37) : "), 11, 0)

        # subTest5 = []
        # for i in range(9):
        #     subTest5.append(QLineEdit(self))
        #     subTest5[i].setText("")
        # for i in range(9):
        #     grid.addWidget(subTest5[i], i + 1, 1)

        # convBtn = QPushButton()
        # convBtn.setText("변환")
        # grid.addWidget(convBtn, 11, 1)

        self.sub5GroupBox.setLayout(self.sub5Grid)

        return self.sub5GroupBox

    def createSubTest6Fields(self):
        self.sub6GroupBox = QGroupBox("Subtest 6: Running Speed and Agility")
        self.sub6Grid = QGridLayout()

        self.sub6Grid.addWidget(QLabel("항목"), 0, 0, alignment=QtCore.Qt.AlignCenter)
        self.sub6Grid.addWidget(QLabel("Raw Score"), 0, 1, alignment=QtCore.Qt.AlignCenter)
        self.sub6Grid.addWidget(QLabel("Point Score"), 0, 2, alignment=QtCore.Qt.AlignCenter)

        self.sub6Grid.addWidget(QLabel("Shuttle Run : "), 1, 0)
        self.sub6Grid.addWidget(QLabel("Stepping Sideways over a Balance Beam : "), 2, 0)
        self.sub6Grid.addWidget(QLabel("One-Legged Stationary Hop : "), 3, 0)
        self.sub6Grid.addWidget(QLabel("One-Legged Side Hop : "), 4, 0)
        self.sub6Grid.addWidget(QLabel("Two-Legged Side Hop : "), 5, 0)
        self.sub6Grid.addWidget(QLabel("Total Point Score Subtest 6 (max=52) : "), 11, 0)

        # subTest6 = []
        # for i in range(5):
        #     subTest6.append(QLineEdit(self))
        #     subTest6[i].setText("")
        # for i in range(5):
        #     grid.addWidget(subTest6[i], i + 1, 1)

        # convBtn = QPushButton()
        # convBtn.setText("변환")
        # grid.addWidget(convBtn, 11, 1)

        self.sub6GroupBox.setLayout(self.sub6Grid)

        return self.sub6GroupBox

    def createSubTest7Fields(self):
        self.sub7GroupBox = QGroupBox("Subtest 7: Upper-Limb Coordination")
        self.sub7Grid = QGridLayout()

        self.sub7Grid.addWidget(QLabel("항목"), 0, 0, alignment=QtCore.Qt.AlignCenter)
        self.sub7Grid.addWidget(QLabel("Raw Score"), 0, 1, alignment=QtCore.Qt.AlignCenter)
        self.sub7Grid.addWidget(QLabel("Point Score"), 0, 2, alignment=QtCore.Qt.AlignCenter)

        self.sub7Grid.addWidget(QLabel("Dropping and Catching a Ball -- Both Hands : "), 1, 0)
        self.sub7Grid.addWidget(QLabel("Catching a Tossed Ball -- Both Hands : "), 2, 0)
        self.sub7Grid.addWidget(QLabel("Dropping and Catching a Ball --One Hands : "), 3, 0)
        self.sub7Grid.addWidget(QLabel("Catching a Tossed Ball --One Hands : "), 4, 0)
        self.sub7Grid.addWidget(QLabel("Dribbling a Ball -- One Hand : "), 5, 0)
        self.sub7Grid.addWidget(QLabel("Dribbling a Ball -- Alternating Hands : "), 6, 0)
        self.sub7Grid.addWidget(QLabel("Throwing a Ball at a Target : "), 7, 0)
        self.sub7Grid.addWidget(QLabel("Total Point Score Subtest 7 (max=39) : "), 11, 0)

        # subTest7 = []
        # for i in range(7):
        #     subTest7.append(QLineEdit(self))
        #     subTest7[i].setText("")
        # for i in range(7):
        #     grid.addWidget(subTest7[i], i + 1, 1)

        # convBtn = QPushButton()
        # convBtn.setText("변환")
        # grid.addWidget(convBtn, 11, 1)

        self.sub7GroupBox.setLayout(self.sub7Grid)

        return self.sub7GroupBox

    def createSubTest8Fields(self):
        self.sub8GroupBox = QGroupBox("Subtest 8: Strength")
        self.sub8Grid = QGridLayout()

        self.sub8Grid.addWidget(QLabel("항목"), 0, 0, alignment=QtCore.Qt.AlignCenter)
        self.sub8Grid.addWidget(QLabel("Raw Score"), 0, 1, alignment=QtCore.Qt.AlignCenter)
        self.sub8Grid.addWidget(QLabel("Point Score"), 0, 2, alignment=QtCore.Qt.AlignCenter)

        self.sub8Grid.addWidget(QLabel("Standing Long Jump : "), 1, 0)
        self.sub8Grid.addWidget(QLabel("Knee Push-ups : "), 2, 0)
        self.sub8Grid.addWidget(QLabel("Sit-ups : "), 3, 0)
        self.sub8Grid.addWidget(QLabel("Wall Sit : "), 4, 0)
        self.sub8Grid.addWidget(QLabel("V-up : "), 5, 0)
        self.sub8Grid.addWidget(QLabel("Total Point Score Subtest 8 (max=42) : "), 11, 0)

        # subTest8 = []
        # for i in range(5):
        #     subTest8.append(QLineEdit(self))
        #     subTest8[i].setText("")
        # for i in range(5):
        #     grid.addWidget(subTest8[i], i + 1, 1)

        # convBtn = QPushButton()
        # convBtn.setText("변환")
        # grid.addWidget(convBtn, 11, 1)

        self.sub8GroupBox.setLayout(self.sub8Grid)

        return self.sub8GroupBox

    def createFineMaualControlFields(self):
        self.FMCGroupBox = QGroupBox("Find Manual Control")
        self.FMCGrid = QGridLayout()

        self.FMCGrid.addWidget(QLabel("Total Point Score"), 0, 1)
        self.FMCGrid.addWidget(QLabel("Scale Score"), 0, 2)
        self.FMCGrid.addWidget(QLabel("Standard Score"), 0, 3)
        self.FMCGrid.addWidget(QLabel("1. Find Motor Precision"), 1, 0)
        self.FMCGrid.addWidget(QLabel("2. Find Motor Integration"), 2, 0)
        self.FMCGrid.addWidget(
            QLabel("Find Manual Control"), 3, 0, alignment=QtCore.Qt.AlignCenter
        )

        self.FMCGroupBox.setLayout(self.FMCGrid)
        return self.FMCGroupBox

    def createManualCoordinationFields(self):
        self.MCGroupBox = QGroupBox("Manual Coordination")
        self.MCGrid = QGridLayout()

        self.MCGrid.addWidget(QLabel("Total Point Score"), 0, 1)
        self.MCGrid.addWidget(QLabel("Scale Score"), 0, 2)
        self.MCGrid.addWidget(QLabel("Standard Score"), 0, 3)
        self.MCGrid.addWidget(QLabel("3. Manual Dexterity"), 1, 0)
        self.MCGrid.addWidget(QLabel("7. Upper-Limb Coordination"), 2, 0)
        self.MCGrid.addWidget(
            QLabel("Manual Coordination"), 3, 0, alignment=QtCore.Qt.AlignCenter
        )

        self.MCGroupBox.setLayout(self.MCGrid)
        return self.MCGroupBox

    def createBodyCoordinationFields(self):
        self.BCGroupBox = QGroupBox("Body Coordination")
        self.BCGrid = QGridLayout()

        self.BCGrid.addWidget(QLabel("Total Point Score"), 0, 1)
        self.BCGrid.addWidget(QLabel("Scale Score"), 0, 2)
        self.BCGrid.addWidget(QLabel("Standard Score"), 0, 3)
        self.BCGrid.addWidget(QLabel("4. Bilateral Coordination"), 1, 0)
        self.BCGrid.addWidget(QLabel("5. Balance"), 2, 0)
        self.BCGrid.addWidget(
            QLabel("Body Coordination"), 3, 0, alignment=QtCore.Qt.AlignCenter
        )

        self.BCGroupBox.setLayout(self.BCGrid)
        return self.BCGroupBox

    def createStrengthAndAgilityFields(self):
        self.SAGroupBox = QGroupBox("Strength and Agility")
        self.SAGrid = QGridLayout()

        self.SAGrid.addWidget(QLabel("Total Point Score"), 0, 1)
        self.SAGrid.addWidget(QLabel("Scale Score"), 0, 2)
        self.SAGrid.addWidget(QLabel("Standard Score"), 0, 3)
        self.SAGrid.addWidget(QLabel("6. Running Speed and Agility"), 1, 0)
        self.SAGrid.addWidget(QLabel("8. Strength Push-up: Knee Full"), 2, 0)
        self.SAGrid.addWidget(
            QLabel("Strength and Agility"), 3, 0, alignment=QtCore.Qt.AlignCenter
        )

        self.SAGroupBox.setLayout(self.SAGrid)
        return self.SAGroupBox

    def createResultFields(self):
        self.RGroupBox = QGroupBox("Result")
        self.RGrid = QGridLayout()

        self.RGrid.addWidget(QLabel("Total Standard Score"), 0, 0)
        self.RGrid.addWidget(QLabel("Total Motor Composite"), 1, 0)

        self.RGroupBox.setLayout(self.RGrid)
        return self.RGroupBox

    def inputRequiredData(self):
        age = "{:.3f}".format(self.requiredData[5])
        self.requiredGrid.addWidget(QLabel(self.requiredData[1]), 0, 1) # 이름
        self.requiredGrid.addWidget(QLabel(str(age)), 1, 1) # 나이
        self.requiredGrid.addWidget(QLabel(str(self.requiredData[4])[0:10]), 2, 1) # 생년월일
        self.requiredGrid.addWidget(QLabel(str(self.requiredData[3])[0:10]), 3, 1) # 검사일

        if self.requiredData[2] == '남성':
            self.maleField.toggle()
        elif self.requiredData[2] == '여성':
            self.femaleField.toggle()
        else:
            pass

        if self.requiredData[0] == "combined":
            self.combinedField.toggle()
        elif self.requiredData[0] == "male":
            self.onlyMaleField.toggle()
        elif self.requiredData[0] == "female":
            self.onlyFemaleField.toggle()
        else:
            pass

    def inputSub1RawPoint(self):
        self.confSub1Raw = self.sub1Raw

        for i in range(7):
            self.sub1Grid.addWidget(QLabel(str(self.sub1Raw[i])), i+1, 1, alignment=QtCore.Qt.AlignCenter)

        self.sub1TotalPoint = 0
        self.sub1Point = []

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
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                break

            self.sub1TotalPoint += self.sub1Point[i]

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
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                break

            self.sub1TotalPoint += self.sub1Point[i]
        
        for i in range(4, 7):
            if self.sub1Raw[i] == 0:
                self.sub1Point.append(0)
            elif self.sub1Raw[i] <= 2:
                self.sub1Point.append(1)
            elif self.sub1Raw[i] <= 4:
                self.sub1Point.append(2)
            elif self.sub1Raw[i] <= 6:
                self.sub1Point.append(3)
            elif self.sub1Raw[i] <= 8:
                self.sub1Point.append(4)
            elif self.sub1Raw[i] <= 10:
                self.sub1Point.append(5)
            elif self.sub1Raw[i] == 11:
                self.sub1Point.append(6)
            elif self.sub1Raw[i] == 12:
                self.sub1Point.append(7)
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                break

            self.sub1TotalPoint += self.sub1Point[i]

        for i in range(7):
            self.sub1Grid.addWidget(QLabel(str(self.sub1Point[i])), i+1, 2, alignment=QtCore.Qt.AlignCenter)

        self.sub1Grid.addWidget(QLabel(str(self.sub1TotalPoint)), 11, 2, alignment=QtCore.Qt.AlignCenter)

    def inputSub2RawPoint(self):
        self.confSub2Raw = self.sub2Raw
        for i in range(8):
            self.sub2Grid.addWidget(QLabel(str(self.sub2Raw[i])), i+1, 1, alignment=QtCore.Qt.AlignCenter)
            self.sub2Grid.addWidget(QLabel(str(self.sub2Raw[i])), i+1, 2, alignment=QtCore.Qt.AlignCenter)
        
        self.sub2TotalPoint = 0
        for i in range(8):
            self.sub2TotalPoint += self.sub2Raw[i]
        
        self.sub2Grid.addWidget(QLabel(str(self.sub2TotalPoint)), 11, 2, alignment=QtCore.Qt.AlignCenter)
        
    def inputSub3RawPoint(self):
        for i in range(1,5):
            if self.sub3Raw[i] > self.sub3Raw[i+1]:
                self.sub3Raw = np.delete(self.sub3Raw, i+1)
            elif self.sub3Raw[i] < self.sub3Raw[i+1]:
                self.sub3Raw = np.delete(self.sub3Raw, i)
            else:
                self.sub3Raw = np.delete(self.sub3Raw, i)
        
        for i in range(5):
            self.sub3Grid.addWidget(QLabel(str(self.sub3Raw[i])), i+1, 1, alignment=QtCore.Qt.AlignCenter)

        self.sub3TotalPoint = 0
        self.sub3Point = []

        if self.sub3Raw[0] >= 0 and self.sub3Raw[0] <= 4:
            self.sub3Point.append(0)
        elif self.sub3Raw[0] >= 5 and self.sub3Raw[0] <= 10:
            self.sub3Point.append(1)
        elif self.sub3Raw[0] >= 11 and self.sub3Raw[0] <= 15:
            self.sub3Point.append(2)
        elif self.sub3Raw[0] >= 16 and self.sub3Raw[0] <= 20:
            self.sub3Point.append(3)
        elif self.sub3Raw[0] >= 21 and self.sub3Raw[0] <= 25:
            self.sub3Point.append(4)
        elif self.sub3Raw[0] >= 26 and self.sub3Raw[0] <= 30:
            self.sub3Point.append(5)
        elif self.sub3Raw[0] >= 31 and self.sub3Raw[0] <= 35:
            self.sub3Point.append(6)
        elif self.sub3Raw[0] >= 36 and self.sub3Raw[0] <= 40:
            self.sub3Point.append(7)
        elif self.sub3Raw[0] >= 41 and self.sub3Raw[0] <= 50:
            self.sub3Point.append(8)
        elif self.sub3Raw[0] >= 51:
            self.sub3Point.append(9)
        else:
            QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
        
        if self.sub3Raw[1] >= 0 and self.sub3Raw[1] <= 2:
            self.sub3Point.append(0)
        elif self.sub3Raw[1] >= 3 and self.sub3Raw[1] <= 4:
            self.sub3Point.append(1)
        elif self.sub3Raw[1] >= 5 and self.sub3Raw[1] <= 6:
            self.sub3Point.append(2)
        elif self.sub3Raw[1] >= 7 and self.sub3Raw[1] <= 8:
            self.sub3Point.append(3)
        elif self.sub3Raw[1] >= 9 and self.sub3Raw[1] <= 10:
            self.sub3Point.append(4)
        elif self.sub3Raw[1] >= 11 and self.sub3Raw[1] <= 12:
            self.sub3Point.append(5)
        elif self.sub3Raw[1] >= 13 and self.sub3Raw[1] <= 14:
            self.sub3Point.append(6)
        elif self.sub3Raw[1] >= 15 and self.sub3Raw[1] <= 16:
            self.sub3Point.append(7)
        elif self.sub3Raw[1] >= 17 and self.sub3Raw[1] <= 18:
            self.sub3Point.append(8)
        elif self.sub3Raw[1] >= 19 and self.sub3Raw[1] <= 20:
            self.sub3Point.append(9)
        else:
            QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
        
        if self.sub3Raw[2] >= 0 and self.sub3Raw[2] <= 2:
            self.sub3Point.append(0)
        elif self.sub3Raw[2] == 3:
            self.sub3Point.append(1)
        elif self.sub3Raw[2] == 4:
            self.sub3Point.append(2)
        elif self.sub3Raw[2] == 5:
            self.sub3Point.append(3)
        elif self.sub3Raw[2] == 6:
            self.sub3Point.append(4)
        elif self.sub3Raw[2] == 7:
            self.sub3Point.append(5)
        elif self.sub3Raw[2] == 8:
            self.sub3Point.append(6)
        elif self.sub3Raw[2] == 9:
            self.sub3Point.append(7)
        elif self.sub3Raw[2] == 10:
            self.sub3Point.append(8)
        elif self.sub3Raw[2] >= 11:
            self.sub3Point.append(9)
        else:
            QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")

        if self.sub3Raw[3] >= 0 and self.sub3Raw[3] <= 4:
            self.sub3Point.append(0)
        elif self.sub3Raw[3] >= 5 and self.sub3Raw[3] <= 6:
            self.sub3Point.append(1)
        elif self.sub3Raw[3] >= 7 and self.sub3Raw[3] <= 8:
            self.sub3Point.append(2)
        elif self.sub3Raw[3] >= 9 and self.sub3Raw[3] <= 10:
            self.sub3Point.append(3)
        elif self.sub3Raw[3] >= 11 and self.sub3Raw[3] <= 12:
            self.sub3Point.append(4)
        elif self.sub3Raw[3] >= 13 and self.sub3Raw[3] <= 14:
            self.sub3Point.append(5)
        elif self.sub3Raw[3] >= 15 and self.sub3Raw[3] <= 16:
            self.sub3Point.append(6)
        elif self.sub3Raw[3] >= 17 and self.sub3Raw[3] <= 20:
            self.sub3Point.append(7)
        elif self.sub3Raw[3] >= 21 and self.sub3Raw[3] <= 24:
            self.sub3Point.append(8)
        elif self.sub3Raw[3] >= 25:
            self.sub3Point.append(9)
        else:
            QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
        
        if self.sub3Raw[4] >= 0 and self.sub3Raw[4] <= 1:
            self.sub3Point.append(0)
        elif self.sub3Raw[4] == 2:
            self.sub3Point.append(1)
        elif self.sub3Raw[4] == 3:
            self.sub3Point.append(2)
        elif self.sub3Raw[4] == 4:
            self.sub3Point.append(3)
        elif self.sub3Raw[4] == 5:
            self.sub3Point.append(4)
        elif self.sub3Raw[4] == 6:
            self.sub3Point.append(5)
        elif self.sub3Raw[4] == 7:
            self.sub3Point.append(6)
        elif self.sub3Raw[4] == 8:
            self.sub3Point.append(7)
        elif self.sub3Raw[4] == 9:
            self.sub3Point.append(8)
        elif self.sub3Raw[4] >= 10:
            self.sub3Point.append(9)
        else:
            QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
        
        for i in range(5):
            self.sub3Grid.addWidget(QLabel(str(self.sub3Point[i])), i+1, 2, alignment=QtCore.Qt.AlignCenter)
            self.sub3TotalPoint += self.sub3Point[i]

        self.sub3Grid.addWidget(QLabel(str(self.sub3TotalPoint)), 11, 2, alignment=QtCore.Qt.AlignCenter)
        
    def inputSub4RawPoint(self):
        for i in range(7):
            if self.sub4Raw[i] > self.sub4Raw[i+1]:
                self.sub4Raw = np.delete(self.sub4Raw, i+1)
            elif self.sub4Raw[i] < self.sub4Raw[i+1]:
                self.sub4Raw = np.delete(self.sub4Raw, i)
            else:
                self.sub4Raw = np.delete(self.sub4Raw, i+1)

        for i in range(7):
            self.sub4Grid.addWidget(QLabel(str(self.sub4Raw[i])), i+1, 1, alignment=QtCore.Qt.AlignCenter)

        self.sub4TotalPoint = 0
        self.sub4Point = []

        if self.sub4Raw[0] == 0:
            self.sub4Point.append(0)
        elif self.sub4Raw[0] == 1:
            self.sub4Point.append(1)
        elif self.sub4Raw[0] == 2:
            self.sub4Point.append(2)
        elif self.sub4Raw[0] == 3:
            self.sub4Point.append(3)
        elif self.sub4Raw[0] == 4:
            self.sub4Point.append(4)
        else:
            QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
        
        for i in range(1, 5):
            if self.sub4Raw[i] == 0:
                self.sub4Point.append(0)
            elif self.sub4Raw[i] == 1:
                self.sub4Point.append(1)
            elif self.sub4Raw[i] >= 2 and self.sub4Raw[i] <= 4:
                self.sub4Point.append(2)
            elif self.sub4Raw[i] == 5:
                self.sub4Point.append(3)
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                break
        
        for i in range(5, 7):
            if self.sub4Raw[i] == 0:
                self.sub4Point.append(0)
            elif self.sub4Raw[i] == 1:
                self.sub4Point.append(1)
            elif self.sub4Raw[i] >= 2 and self.sub4Raw[i] <= 4:
                self.sub4Point.append(2)
            elif self.sub4Raw[i] >= 5 and self.sub4Raw[i] <= 9:
                self.sub4Point.append(3)
            elif self.sub4Raw[i] == 10:
                self.sub4Point.append(4)
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                break

        for i in range(7):
            self.sub4Grid.addWidget(QLabel(str(self.sub4Point[i])), i+1, 2, alignment=QtCore.Qt.AlignCenter)
            self.sub4TotalPoint += self.sub4Point[i]

        self.sub4Grid.addWidget(QLabel(str(self.sub4TotalPoint)), 11, 2, alignment=QtCore.Qt.AlignCenter)

    def inputSub5RawPoint(self):
        for i in range(9):
            if self.sub5Raw[i] > self.sub5Raw[i+1]:
                self.sub5Raw = np.delete(self.sub5Raw, i+1)
            elif self.sub5Raw[i] < self.sub5Raw[i+1]:
                self.sub5Raw = np.delete(self.sub5Raw, i)
            else:
                self.sub5Raw = np.delete(self.sub5Raw, i+1)

        for i in range(9):
            self.sub5Grid.addWidget(QLabel(str(self.sub5Raw[i])), i+1, 1, alignment=QtCore.Qt.AlignCenter)

        self.sub5TotalPoint = 0
        self.sub5Point = []

        for i in range(9):
            if i == 0 or i == 2 or i == 3 or i == 5 or i == 6 or i == 7:
                if float(self.sub5Raw[i]) >= 0.0 and float(self.sub5Raw[i]) <= 0.9:
                    self.sub5Point.append(0)
                elif float(self.sub5Raw[i]) >= 1.0 and float(self.sub5Raw[i]) <= 2.9:
                    self.sub5Point.append(1)
                elif float(self.sub5Raw[i]) >= 3.0 and float(self.sub5Raw[i]) <= 5.9:
                    self.sub5Point.append(2)
                elif float(self.sub5Raw[i]) >= 6.0 and float(self.sub5Raw[i]) <= 9.9:
                    self.sub5Point.append(3)
                elif float(self.sub5Raw[i]) == 10:
                    self.sub5Point.append(4)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break
            elif i == 1 or i == 4:
                if self.sub5Raw[i] == 0:
                    self.sub5Point.append(0)
                elif self.sub5Raw[i] >= 1 and self.sub5Raw[i] <= 2:
                    self.sub5Point.append(1)
                elif self.sub5Raw[i] >= 3 and self.sub5Raw[i] <= 4:
                    self.sub5Point.append(2)
                elif self.sub5Raw[i] == 5:
                    self.sub5Point.append(3)
                elif self.sub5Raw[i] == 6:
                    self.sub5Point.append(4)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break
            else:
                if float(self.sub5Raw[i]) >= 0.0 and float(self.sub5Raw[i]) <= 0.9:
                    self.sub5Point.append(0)
                elif float(self.sub5Raw[i]) >= 1.0 and float(self.sub5Raw[i]) <= 2.9:
                    self.sub5Point.append(1)
                elif float(self.sub5Raw[i]) >= 3.0 and float(self.sub5Raw[i]) <= 4.9:
                    self.sub5Point.append(2)
                elif float(self.sub5Raw[i]) >= 5.0 and float(self.sub5Raw[i]) <= 7.9:
                    self.sub5Point.append(3)
                elif float(self.sub5Raw[i]) >= 8.0 and float(self.sub5Raw[i]) <= 9.9:
                    self.sub5Point.append(4)
                elif float(self.sub5Raw[i]) == 10:
                    self.sub5Point.append(5)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break
        
        for i in range(9):
            self.sub5Grid.addWidget(QLabel(str(self.sub5Point[i])), i+1, 2, alignment=QtCore.Qt.AlignCenter)
            self.sub5TotalPoint += self.sub5Point[i]

        self.sub5Grid.addWidget(QLabel(str(self.sub5TotalPoint)), 11, 2, alignment=QtCore.Qt.AlignCenter)
        
    def inputSub6RawPoint(self):
        for i in range(5):
            if self.sub6Raw[i] > self.sub6Raw[i+1]:
                self.sub6Raw = np.delete(self.sub6Raw, i+1)
            elif self.sub6Raw[i] < self.sub6Raw[i+1]:
                self.sub6Raw = np.delete(self.sub6Raw, i)
            else:
                self.sub6Raw = np.delete(self.sub6Raw, i+1)

        for i in range(5):
            self.sub6Grid.addWidget(QLabel(str(self.sub6Raw[i])), i+1, 1, alignment=QtCore.Qt.AlignCenter)

        self.sub6TotalPoint = 0
        self.sub6Point = []
        for i in range(5):
            if i == 0:
                if float(self.sub6Raw[i]) >= 16.0:
                    self.sub6Point.append(0)
                elif float(self.sub6Raw[i]) >= 14.0:
                    self.sub6Point.append(1)
                elif float(self.sub6Raw[i]) >= 13.0:
                    self.sub6Point.append(2)
                elif float(self.sub6Raw[i]) >= 12.0:
                    self.sub6Point.append(3)
                elif float(self.sub6Raw[i]) >= 11.0:
                    self.sub6Point.append(4)
                elif float(self.sub6Raw[i]) >= 10.0:
                    self.sub6Point.append(5)
                elif float(self.sub6Raw[i]) >= 9.0:
                    self.sub6Point.append(6)
                elif float(self.sub6Raw[i]) >= 8.0:
                    self.sub6Point.append(7)
                elif float(self.sub6Raw[i]) >= 7.5:
                    self.sub6Point.append(8)
                elif float(self.sub6Raw[i]) >= 7.0:
                    self.sub6Point.append(9)
                elif float(self.sub6Raw[i]) >= 6.5:
                    self.sub6Point.append(10)
                elif float(self.sub6Raw[i]) >= 6.0:
                    self.sub6Point.append(11)
                elif float(self.sub6Raw[i]) <= 5.9:
                    self.sub6Point.append(12)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break 
            elif i == 3:
                if self.sub6Raw[i] == 0:
                    self.sub6Point.append(0)
                elif self.sub6Raw[i] >= 1 and self.sub6Raw[i] <= 2:
                    self.sub6Point.append(1)
                elif self.sub6Raw[i] >= 3 and self.sub6Raw[i] <= 5:
                    self.sub6Point.append(2)
                elif self.sub6Raw[i] >= 6 and self.sub6Raw[i] <= 9:
                    self.sub6Point.append(3)
                elif self.sub6Raw[i] >= 10 and self.sub6Raw[i] <= 14:
                    self.sub6Point.append(4)
                elif self.sub6Raw[i] >= 15 and self.sub6Raw[i] <= 19:
                    self.sub6Point.append(5)
                elif self.sub6Raw[i] >= 20 and self.sub6Raw[i] <= 24:
                    self.sub6Point.append(6)
                elif self.sub6Raw[i] >= 25 and self.sub6Raw[i] <= 29:
                    self.sub6Point.append(7)
                elif self.sub6Raw[i] >= 30 and self.sub6Raw[i] <= 34:
                    self.sub6Point.append(8)
                elif self.sub6Raw[i] >= 35 and self.sub6Raw[i] <= 39:
                    self.sub6Point.append(9)
                elif self.sub6Raw[i] >= 40:
                    self.sub6Point.append(10)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break
            else:
                if self.sub6Raw[i] == 0:
                    self.sub6Point.append(0)
                elif self.sub6Raw[i] >= 1 and self.sub6Raw[i] <= 2:
                    self.sub6Point.append(1)
                elif self.sub6Raw[i] >= 3 and self.sub6Raw[i] <= 5:
                    self.sub6Point.append(2)
                elif self.sub6Raw[i] >= 6 and self.sub6Raw[i] <= 9:
                    self.sub6Point.append(3)
                elif self.sub6Raw[i] >= 10 and self.sub6Raw[i] <= 14:
                    self.sub6Point.append(4)
                elif self.sub6Raw[i] >= 15 and self.sub6Raw[i] <= 19:
                    self.sub6Point.append(5)
                elif self.sub6Raw[i] >= 20 and self.sub6Raw[i] <= 24:
                    self.sub6Point.append(6)
                elif self.sub6Raw[i] >= 25 and self.sub6Raw[i] <= 29:
                    self.sub6Point.append(7)
                elif self.sub6Raw[i] >= 30 and self.sub6Raw[i] <= 39:
                    self.sub6Point.append(8)
                elif self.sub6Raw[i] >= 40 and self.sub6Raw[i] <= 49:
                    self.sub6Point.append(9)
                elif self.sub6Raw[i] >= 50:
                    self.sub6Point.append(10)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break
        for i in range(5):
            self.sub6Grid.addWidget(QLabel(str(self.sub6Point[i])), i+1, 2, alignment=QtCore.Qt.AlignCenter)
            self.sub6TotalPoint += self.sub6Point[i]

        self.sub6Grid.addWidget(QLabel(str(self.sub6TotalPoint)), 11, 2, alignment=QtCore.Qt.AlignCenter)

    def inputSub7RawPoint(self):
        for i in range(7):
            if self.sub7Raw[i] > self.sub7Raw[i+1]:
                self.sub7Raw = np.delete(self.sub7Raw, i+1)
            elif self.sub7Raw[i] < self.sub7Raw[i+1]:
                self.sub7Raw = np.delete(self.sub7Raw, i)
            else:
                self.sub7Raw = np.delete(self.sub7Raw, i+1)

        for i in range(7):
            self.sub7Grid.addWidget(QLabel(str(self.sub7Raw[i])), i+1, 1, alignment=QtCore.Qt.AlignCenter)

        self.sub7TotalPoint = 0
        self.sub7Point = []

        for i in range(7):
            if i == 4 or i == 5:
                if self.sub7Raw[i] == 0:
                    self.sub7Point.append(0)
                elif self.sub7Raw[i] == 1:
                    self.sub7Point.append(1)
                elif self.sub7Raw[i] == 2:
                    self.sub7Point.append(2)
                elif self.sub7Raw[i] == 3:
                    self.sub7Point.append(3)
                elif self.sub7Raw[i] >= 4 and self.sub7Raw[i] <= 5:
                    self.sub7Point.append(4)
                elif self.sub7Raw[i] >= 6 and self.sub7Raw[i] <= 7:
                    self.sub7Point.append(5)
                elif self.sub7Raw[i] >= 8 and self.sub7Raw[i] <= 9:
                    self.sub7Point.append(6)
                elif self.sub7Raw[i] == 10:
                    self.sub7Point.append(7)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break
            else:
                if self.sub7Raw[i] == 0:
                    self.sub7Point.append(0)
                elif self.sub7Raw[i] == 1:
                    self.sub7Point.append(1)
                elif self.sub7Raw[i] == 2:
                    self.sub7Point.append(2)
                elif self.sub7Raw[i] == 3:
                    self.sub7Point.append(3)
                elif self.sub7Raw[i] == 4:
                    self.sub7Point.append(4)
                elif self.sub7Raw[i] == 5:
                    self.sub7Point.append(5)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break

        for i in range(7):
            self.sub7Grid.addWidget(QLabel(str(self.sub7Point[i])), i+1, 2, alignment=QtCore.Qt.AlignCenter)
            self.sub7TotalPoint += self.sub7Point[i]

        self.sub7Grid.addWidget(QLabel(str(self.sub7TotalPoint)), 11, 2, alignment=QtCore.Qt.AlignCenter)

    def inputSub8RawPoint(self):
        for i in range(5):
            if self.sub8Raw[i] > self.sub8Raw[i+1]:
                self.sub8Raw = np.delete(self.sub8Raw, i+1)
            elif self.sub8Raw[i] < self.sub8Raw[i+1]:
                self.sub8Raw = np.delete(self.sub8Raw, i)
            else:
                self.sub8Raw = np.delete(self.sub8Raw, i+1)
            
        # print(self.sub8Raw)

        for i in range(5):
            self.sub8Grid.addWidget(QLabel(str(self.sub8Raw[i])), i+1, 1, alignment=QtCore.Qt.AlignCenter)
        
        self.sub8TotalPoint = 0
        self.sub8Point = []

        for i in range(5):
            if i == 1 or i == 2:
                if self.sub8Raw[i] == 0:
                    self.sub8Point.append(0)
                elif self.sub8Raw[i] >= 1 and self.sub8Raw[i] <= 2:
                    self.sub8Point.append(1)
                elif self.sub8Raw[i] >= 3 and self.sub8Raw[i] <= 5:
                    self.sub8Point.append(2)
                elif self.sub8Raw[i] >= 6 and self.sub8Raw[i] <= 10:
                    self.sub8Point.append(3)
                elif self.sub8Raw[i] >= 11 and self.sub8Raw[i] <= 15:
                    self.sub8Point.append(4)
                elif self.sub8Raw[i] >= 16 and self.sub8Raw[i] <= 20:
                    self.sub8Point.append(5)
                elif self.sub8Raw[i] >= 21 and self.sub8Raw[i] <= 25:
                    self.sub8Point.append(6)
                elif self.sub8Raw[i] >= 26 and self.sub8Raw[i] <= 30:
                    self.sub8Point.append(7)
                elif self.sub8Raw[i] >= 31 and self.sub8Raw[i] <= 35:
                    self.sub8Point.append(8)
                elif self.sub8Raw[i] >= 36:
                    self.sub8Point.append(9)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break
            elif i == 3 or i == 4:
                if float(self.sub8Raw[i]) >= 0.0 and float(self.sub8Raw[i]) <= 0.9:
                    self.sub8Point.append(0)
                elif float(self.sub8Raw[i]) >= 1.0 and float(self.sub8Raw[i]) <= 4.9:
                    self.sub8Point.append(1)
                elif float(self.sub8Raw[i]) >= 5.0 and float(self.sub8Raw[i]) <= 14.9:
                    self.sub8Point.append(2)
                elif float(self.sub8Raw[i]) >= 15.0 and float(self.sub8Raw[i]) <= 24.9:
                    self.sub8Point.append(3)
                elif float(self.sub8Raw[i]) >= 25.0 and float(self.sub8Raw[i]) <= 44.9:
                    self.sub8Point.append(4)
                elif float(self.sub8Raw[i]) >= 45.0 and float(self.sub8Raw[i]) <= 59.9:
                    self.sub8Point.append(5)
                elif float(self.sub8Raw[i]) == 60.0:
                    self.sub8Point.append(6)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break
            else:
                if self.sub8Raw[i] <= 12:
                    self.sub8Point.append(0)
                elif self.sub8Raw[i] >= 13 and self.sub8Raw[i] <= 18:
                    self.sub8Point.append(1)
                elif self.sub8Raw[i] >= 19 and self.sub8Raw[i] <= 24:
                    self.sub8Point.append(2)
                elif self.sub8Raw[i] >= 25 and self.sub8Raw[i] <= 30:
                    self.sub8Point.append(3)
                elif self.sub8Raw[i] >= 31 and self.sub8Raw[i] <= 36:
                    self.sub8Point.append(4)
                elif self.sub8Raw[i] >= 37 and self.sub8Raw[i] <= 42:
                    self.sub8Point.append(5)
                elif self.sub8Raw[i] >= 43 and self.sub8Raw[i] <= 48:
                    self.sub8Point.append(6)
                elif self.sub8Raw[i] >= 49 and self.sub8Raw[i] <= 54:
                    self.sub8Point.append(7)
                elif self.sub8Raw[i] >= 55 and self.sub8Raw[i] <= 60:
                    self.sub8Point.append(8)
                elif self.sub8Raw[i] >= 61 and self.sub8Raw[i] <= 66:
                    self.sub8Point.append(9)
                elif self.sub8Raw[i] >= 67 and self.sub8Raw[i] <= 72:
                    self.sub8Point.append(10)
                elif self.sub8Raw[i] >= 73 and self.sub8Raw[i] <= 84:
                    self.sub8Point.append(11)
                elif self.sub8Raw[i] >= 84:
                    self.sub8Point.append(12)
                else:
                    QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
                    break
        
        for i in range(5):
            self.sub8Grid.addWidget(QLabel(str(self.sub8Point[i])), i+1, 2, alignment=QtCore.Qt.AlignCenter)
            self.sub8TotalPoint += self.sub8Point[i]

        self.sub8Grid.addWidget(QLabel(str(self.sub8TotalPoint)), 11, 2, alignment=QtCore.Qt.AlignCenter)
    
    def scaleCombined(self):
        if self.requiredData[5] >= 10.0 and self.requiredData[5] <= 10.5: 
            if self.sub1TotalPoint >= 0 and self.sub1TotalPoint <= 8:
                self.sub1Scale = 1
            elif self.sub1TotalPoint >= 9 and self.sub1TotalPoint <= 13:
                self.sub1Scale = 2
            elif self.sub1TotalPoint >= 14 and self.sub1TotalPoint <= 17:
                self.sub1Scale = 3 
            elif self.sub1TotalPoint >= 18 and self.sub1TotalPoint <= 21:
                self.sub1Scale = 4
            elif self.sub1TotalPoint >= 22 and self.sub1TotalPoint <= 26:
                self.sub1Scale = 5
            elif self.sub1TotalPoint >= 27 and self.sub1TotalPoint <= 29:
                self.sub1Scale = 6
            elif self.sub1TotalPoint >= 30 and self.sub1TotalPoint <= 31:
                self.sub1Scale = 7
            elif self.sub1TotalPoint == 32:
                self.sub1Scale = 8
            elif self.sub1TotalPoint == 33:
                self.sub1Scale = 9
            elif self.sub1TotalPoint == 34:
                self.sub1Scale = 10
            elif self.sub1TotalPoint == 35:
                self.sub1Scale = 11
            elif self.sub1TotalPoint == 36:
                self.sub1Scale = 12
            elif self.sub1TotalPoint == 37:
                self.sub1Scale = 13
            elif self.sub1TotalPoint == 38:
                self.sub1Scale = 15
            elif self.sub1TotalPoint == 39:
                self.sub1Scale = 17
            elif self.sub1TotalPoint == 40:
                self.sub1Scale = 19
            elif self.sub1TotalPoint == 41:
                self.sub1Scale = 22
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")

            if self.sub2TotalPoint >= 0 and self.sub2TotalPoint <= 5:
                self.sub2Scale = 1
            elif self.sub2TotalPoint >= 6 and self.sub2TotalPoint <= 10:
                self.sub2Scale = 2
            elif self.sub2TotalPoint >= 11 and self.sub2TotalPoint <= 15:
                self.sub2Scale = 3 
            elif self.sub2TotalPoint >= 16 and self.sub2TotalPoint <= 20:
                self.sub2Scale = 4
            elif self.sub2TotalPoint >= 21 and self.sub2TotalPoint <= 24:
                self.sub2Scale = 5
            elif self.sub2TotalPoint >= 25 and self.sub2TotalPoint <= 27:
                self.sub2Scale = 6
            elif self.sub2TotalPoint >= 28 and self.sub2TotalPoint <= 30:
                self.sub2Scale = 7
            elif self.sub2TotalPoint == 31:
                self.sub2Scale = 8
            elif self.sub2TotalPoint == 33:
                self.sub2Scale = 10
            elif self.sub2TotalPoint == 34:
                self.sub2Scale = 11
            elif self.sub2TotalPoint == 35:
                self.sub2Scale = 12
            elif self.sub2TotalPoint == 36:
                self.sub2Scale = 13
            elif self.sub2TotalPoint == 37:
                self.sub2Scale = 14
            elif self.sub2TotalPoint == 38:
                self.sub2Scale = 15
            elif self.sub2TotalPoint == 39:
                self.sub2Scale = 18
            elif self.sub2TotalPoint == 40:
                self.sub2Scale = 22
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")

            if self.sub3TotalPoint >= 0 and self.sub3TotalPoint <= 5:
                self.sub3Scale = 1
            elif self.sub3TotalPoint >= 6 and self.sub3TotalPoint <= 9:
                self.sub3Scale = 2
            elif self.sub3TotalPoint >= 10 and self.sub3TotalPoint <= 12:
                self.sub3Scale = 3 
            elif self.sub3TotalPoint >= 13 and self.sub3TotalPoint <= 15:
                self.sub3Scale = 4
            elif self.sub3TotalPoint >= 16 and self.sub3TotalPoint <= 18:
                self.sub3Scale = 5
            elif self.sub3TotalPoint >= 19 and self.sub3TotalPoint <= 21:
                self.sub3Scale = 6
            elif self.sub3TotalPoint == 22:
                self.sub3Scale = 7
            elif self.sub3TotalPoint >= 23 and self.sub3TotalPoint <= 24:
                self.sub3Scale = 8
            elif self.sub3TotalPoint == 25:
                self.sub3Scale = 9
            elif self.sub3TotalPoint == 26:
                self.sub3Scale = 10
            elif self.sub3TotalPoint == 27:
                self.sub3Scale = 11
            elif self.sub3TotalPoint == 28:
                self.sub3Scale = 12
            elif self.sub3TotalPoint == 29:
                self.sub3Scale = 13
            elif self.sub3TotalPoint == 30:
                self.sub3Scale = 15
            elif self.sub3TotalPoint == 31:
                self.sub3Scale = 16
            elif self.sub3TotalPoint == 32:
                self.sub3Scale = 17
            elif self.sub3TotalPoint == 33:
                self.sub3Scale = 18
            elif self.sub3TotalPoint == 34:
                self.sub3Scale = 20
            elif self.sub3TotalPoint == 35:
                self.sub3Scale = 21
            elif self.sub3TotalPoint == 36:
                self.sub3Scale = 23
            elif self.sub3TotalPoint == 37:
                self.sub3Scale = 24
            elif self.sub3TotalPoint == 38:
                self.sub3Scale = 25
            elif self.sub3TotalPoint == 39:
                self.sub3Scale = 26
            elif self.sub3TotalPoint == 40:
                self.sub3Scale = 27
            elif self.sub3TotalPoint >= 41 and self.sub3TotalPoint <= 42:
                self.sub3Scale = 28
            elif self.sub3TotalPoint == 43:
                self.sub3Scale = 29
            elif self.sub3TotalPoint == 44:
                self.sub3Scale = 30
            elif self.sub3TotalPoint == 45:
                self.sub3Scale = 31
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
            
            if self.sub4TotalPoint >= 0 and self.sub4TotalPoint <= 2:
                self.sub4Scale = 1
            elif self.sub4TotalPoint == 3:
                self.sub4Scale = 2
            elif self.sub4TotalPoint >= 4 and self.sub4TotalPoint <= 5:
                self.sub4Scale = 3 
            elif self.sub4TotalPoint >= 6 and self.sub4TotalPoint <= 8:
                self.sub4Scale = 4
            elif self.sub4TotalPoint >= 9 and self.sub4TotalPoint <= 11:
                self.sub4Scale = 5
            elif self.sub4TotalPoint >= 12 and self.sub4TotalPoint <= 14:
                self.sub4Scale = 6
            elif self.sub4TotalPoint >= 15 and self.sub4TotalPoint <= 17:
                self.sub4Scale = 7
            elif self.sub4TotalPoint == 18:
                self.sub4Scale = 8
            elif self.sub4TotalPoint == 19:
                self.sub4Scale = 9
            elif self.sub4TotalPoint == 20:
                self.sub4Scale = 10
            elif self.sub4TotalPoint == 21:
                self.sub4Scale = 11
            elif self.sub4TotalPoint == 22:
                self.sub4Scale = 13
            elif self.sub4TotalPoint == 23:
                self.sub4Scale = 16
            elif self.sub4TotalPoint == 24:
                self.sub4Scale = 20
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
            
            if self.sub5TotalPoint >= 0 and self.sub5TotalPoint <= 7:
                self.sub5Scale = 1
            elif self.sub5TotalPoint >= 8 and self.sub5TotalPoint <= 11:
                self.sub5Scale = 2
            elif self.sub5TotalPoint >= 12 and self.sub5TotalPoint <= 16:
                self.sub5Scale = 3 
            elif self.sub5TotalPoint >= 17 and self.sub5TotalPoint <= 20:
                self.sub5Scale = 4
            elif self.sub5TotalPoint >= 21 and self.sub5TotalPoint <= 23:
                self.sub5Scale = 5
            elif self.sub5TotalPoint >= 24 and self.sub5TotalPoint <= 26:
                self.sub5Scale = 6
            elif self.sub5TotalPoint >= 27 and self.sub5TotalPoint <= 28:
                self.sub5Scale = 7
            elif self.sub5TotalPoint == 29:
                self.sub5Scale = 8
            elif self.sub5TotalPoint == 30:
                self.sub5Scale = 9
            elif self.sub5TotalPoint == 31:
                self.sub5Scale = 10
            elif self.sub5TotalPoint == 32:
                self.sub5Scale = 12
            elif self.sub5TotalPoint == 33:
                self.sub5Scale = 14
            elif self.sub5TotalPoint == 34:
                self.sub5Scale = 16
            elif self.sub5TotalPoint == 35:
                self.sub5Scale = 18
            elif self.sub5TotalPoint == 36:
                self.sub5Scale = 20
            elif self.sub5TotalPoint == 37:
                self.sub5Scale = 23
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
            
            if self.sub6TotalPoint >= 0 and self.sub6TotalPoint <= 4:
                self.sub6Scale = 1
            elif self.sub6TotalPoint >= 5 and self.sub6TotalPoint <= 7:
                self.sub6Scale = 2
            elif self.sub6TotalPoint >= 8 and self.sub6TotalPoint <= 11:
                self.sub6Scale = 3 
            elif self.sub6TotalPoint >= 12 and self.sub6TotalPoint <= 15:
                self.sub6Scale = 4
            elif self.sub6TotalPoint >= 16 and self.sub6TotalPoint <= 18:
                self.sub6Scale = 5
            elif self.sub6TotalPoint >= 19 and self.sub6TotalPoint <= 21:
                self.sub6Scale = 6
            elif self.sub6TotalPoint >= 22 and self.sub6TotalPoint <= 24:
                self.sub6Scale = 7
            elif self.sub6TotalPoint == 25:
                self.sub6Scale = 8
            elif self.sub6TotalPoint == 26:
                self.sub6Scale = 9
            elif self.sub6TotalPoint >= 27 and self.sub6TotalPoint <= 28:
                self.sub6Scale = 10
            elif self.sub6TotalPoint >= 29 and self.sub6TotalPoint <= 30:
                self.sub6Scale = 11
            elif self.sub6TotalPoint == 31:
                self.sub6Scale = 12
            elif self.sub6TotalPoint >= 32 and self.sub6TotalPoint <= 33:
                self.sub6Scale = 13
            elif self.sub6TotalPoint == 34:
                self.sub6Scale = 14
            elif self.sub6TotalPoint == 35:
                self.sub6Scale = 15
            elif self.sub6TotalPoint == 36:
                self.sub6Scale = 16
            elif self.sub6TotalPoint == 37:
                self.sub6Scale = 17
            elif self.sub6TotalPoint == 38:
                self.sub6Scale = 18
            elif self.sub6TotalPoint == 39:
                self.sub6Scale = 19
            elif self.sub6TotalPoint == 40:
                self.sub6Scale = 20
            elif self.sub6TotalPoint >= 41 and self.sub6TotalPoint <= 42:
                self.sub6Scale = 21
            elif self.sub6TotalPoint == 43:
                self.sub6Scale = 22
            elif self.sub6TotalPoint == 44:
                self.sub6Scale = 23
            elif self.sub6TotalPoint >= 45 and self.sub6TotalPoint <= 46:
                self.sub6Scale = 24
            elif self.sub6TotalPoint == 47:
                self.sub6Scale = 26
            elif self.sub6TotalPoint == 48:
                self.sub6Scale = 27
            elif self.sub6TotalPoint == 49:
                self.sub6Scale = 28
            elif self.sub6TotalPoint == 50:
                self.sub6Scale = 29
            elif self.sub6TotalPoint == 51:
                self.sub6Scale = 30
            elif self.sub6TotalPoint == 52:
                self.sub6Scale = 32

            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")

            if self.sub7TotalPoint >= 0 and self.sub7TotalPoint <= 4:
                self.sub7Scale = 1
            elif self.sub7TotalPoint >= 5 and self.sub7TotalPoint <= 9:
                self.sub7Scale = 2
            elif self.sub7TotalPoint >= 10 and self.sub7TotalPoint <= 12:
                self.sub7Scale = 3 
            elif self.sub7TotalPoint >= 13 and self.sub7TotalPoint <= 16:
                self.sub7Scale = 4
            elif self.sub7TotalPoint >= 17 and self.sub7TotalPoint <= 20:
                self.sub7Scale = 5
            elif self.sub7TotalPoint >= 21 and self.sub7TotalPoint <= 24:
                self.sub7Scale = 6
            elif self.sub7TotalPoint >= 25 and self.sub7TotalPoint <= 27:
                self.sub7Scale = 7
            elif self.sub7TotalPoint == 28:
                self.sub7Scale = 8
            elif self.sub7TotalPoint == 29:
                self.sub7Scale = 9
            elif self.sub7TotalPoint >= 30 and self.sub7TotalPoint <= 31:
                self.sub7Scale = 10
            elif self.sub7TotalPoint == 32:
                self.sub7Scale = 11
            elif self.sub7TotalPoint == 33:
                self.sub7Scale = 12
            elif self.sub7TotalPoint == 34:
                self.sub7Scale = 13
            elif self.sub7TotalPoint == 35:
                self.sub7Scale = 14
            elif self.sub7TotalPoint == 36:
                self.sub7Scale = 15
            elif self.sub7TotalPoint == 37:
                self.sub7Scale = 17
            elif self.sub7TotalPoint == 38:
                self.sub7Scale = 20
            elif self.sub7TotalPoint == 39:
                self.sub7Scale = 23
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
            
            if self.sub8TotalPoint >= 0 and self.sub8TotalPoint <= 1:
                self.sub8Scale = 1
            elif self.sub8TotalPoint >= 2 and self.sub8TotalPoint <= 3:
                self.sub8Scale = 2
            elif self.sub8TotalPoint >= 4 and self.sub8TotalPoint <= 6:
                self.sub8Scale = 3 
            elif self.sub8TotalPoint >= 7 and self.sub8TotalPoint <= 8:
                self.sub8Scale = 4
            elif self.sub8TotalPoint >= 9 and self.sub8TotalPoint <= 10:
                self.sub8Scale = 5
            elif self.sub8TotalPoint >= 11 and self.sub8TotalPoint <= 13:
                self.sub8Scale = 6
            elif self.sub8TotalPoint >= 14 and self.sub8TotalPoint <= 15:
                self.sub8Scale = 7
            elif self.sub8TotalPoint == 16:
                self.sub8Scale = 8
            elif self.sub8TotalPoint == 17:
                self.sub8Scale = 9
            elif self.sub8TotalPoint == 18:
                self.sub8Scale = 10
            elif self.sub8TotalPoint >= 19 and self.sub8TotalPoint <= 20:
                self.sub8Scale = 11
            elif self.sub8TotalPoint >= 21 and self.sub8TotalPoint <= 22:
                self.sub8Scale = 12
            elif self.sub8TotalPoint == 23:
                self.sub8Scale = 13
            elif self.sub8TotalPoint == 24:
                self.sub8Scale = 14
            elif self.sub8TotalPoint >= 25 and self.sub8TotalPoint <= 26:
                self.sub8Scale = 15
            elif self.sub8TotalPoint == 27:
                self.sub8Scale = 16
            elif self.sub8TotalPoint == 28:
                self.sub8Scale = 17
            elif self.sub8TotalPoint == 29:
                self.sub8Scale = 18
            elif self.sub8TotalPoint == 30:
                self.sub8Scale = 19
            elif self.sub8TotalPoint == 31:
                self.sub8Scale = 20
            elif self.sub8TotalPoint == 32:
                self.sub8Scale = 21
            elif self.sub8TotalPoint == 33:
                self.sub8Scale = 22
            elif self.sub8TotalPoint >= 34 and self.sub8TotalPoint <= 35:
                self.sub8Scale = 23
            elif self.sub8TotalPoint == 36:
                self.sub8Scale = 24
            elif self.sub8TotalPoint >= 37 and self.sub8TotalPoint <= 38:
                self.sub8Scale = 26
            elif self.sub8TotalPoint == 39:
                self.sub8Scale = 28
            elif self.sub8TotalPoint == 40:
                self.sub8Scale = 29
            elif self.sub8TotalPoint == 41:
                self.sub8Scale = 30
            elif self.sub8TotalPoint == 42:
                self.sub8Scale = 32

        elif self.requiredData[5] >= 10.6 and self.requiredData[5] <= 10.11:
            if self.sub1TotalPoint >= 0 and self.sub1TotalPoint <= 8:
                self.sub1Scale = 1
            elif self.sub1TotalPoint >= 9 and self.sub1TotalPoint <= 13:
                self.sub1Scale = 2
            elif self.sub1TotalPoint >= 14 and self.sub1TotalPoint <= 17:
                self.sub1Scale = 3 
            elif self.sub1TotalPoint >= 18 and self.sub1TotalPoint <= 21:
                self.sub1Scale = 4
            elif self.sub1TotalPoint >= 22 and self.sub1TotalPoint <= 26:
                self.sub1Scale = 5
            elif self.sub1TotalPoint >= 27 and self.sub1TotalPoint <= 30:
                self.sub1Scale = 6
            elif self.sub1TotalPoint == 31:
                self.sub1Scale = 7
            elif self.sub1TotalPoint == 32:
                self.sub1Scale = 8
            elif self.sub1TotalPoint == 33:
                self.sub1Scale = 9
            elif self.sub1TotalPoint == 34:
                self.sub1Scale = 10
            elif self.sub1TotalPoint >= 35 and self.sub1TotalPoint <= 36:
                self.sub1Scale = 11
            elif self.sub1TotalPoint == 37:
                self.sub1Scale = 12
            elif self.sub1TotalPoint == 38:
                self.sub1Scale = 14
            elif self.sub1TotalPoint == 39:
                self.sub1Scale = 16
            elif self.sub1TotalPoint == 40:
                self.sub1Scale = 19
            elif self.sub1TotalPoint == 41:
                self.sub1Scale = 22
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")

            if self.sub2TotalPoint >= 0 and self.sub2TotalPoint <= 5:
                self.sub2Scale = 1
            elif self.sub2TotalPoint >= 6 and self.sub2TotalPoint <= 10:
                self.sub2Scale = 2
            elif self.sub2TotalPoint >= 11 and self.sub2TotalPoint <= 15:
                self.sub2Scale = 3 
            elif self.sub2TotalPoint >= 16 and self.sub2TotalPoint <= 20:
                self.sub2Scale = 4
            elif self.sub2TotalPoint >= 21 and self.sub2TotalPoint <= 24:
                self.sub2Scale = 5
            elif self.sub2TotalPoint >= 25 and self.sub2TotalPoint <= 27:
                self.sub2Scale = 6
            elif self.sub2TotalPoint >= 28 and self.sub2TotalPoint <= 30:
                self.sub2Scale = 7
            elif self.sub2TotalPoint == 31:
                self.sub2Scale = 8
            elif self.sub2TotalPoint >= 32 and self.sub2TotalPoint <= 33:
                self.sub2Scale = 9
            elif self.sub2TotalPoint == 34:
                self.sub2Scale = 10
            elif self.sub2TotalPoint == 35:
                self.sub2Scale = 11
            elif self.sub2TotalPoint == 36:
                self.sub2Scale = 12
            elif self.sub2TotalPoint == 37:
                self.sub2Scale = 13
            elif self.sub2TotalPoint == 38:
                self.sub2Scale = 15
            elif self.sub2TotalPoint == 39:
                self.sub2Scale = 18
            elif self.sub2TotalPoint == 40:
                self.sub2Scale = 22
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")

            if self.sub3TotalPoint >= 0 and self.sub3TotalPoint <= 5:
                self.sub3Scale = 1
            elif self.sub3TotalPoint >= 6 and self.sub3TotalPoint <= 9:
                self.sub3Scale = 2
            elif self.sub3TotalPoint >= 10 and self.sub3TotalPoint <= 12:
                self.sub3Scale = 3 
            elif self.sub3TotalPoint >= 13 and self.sub3TotalPoint <= 15:
                self.sub3Scale = 4
            elif self.sub3TotalPoint >= 16 and self.sub3TotalPoint <= 18:
                self.sub3Scale = 5
            elif self.sub3TotalPoint >= 19 and self.sub3TotalPoint <= 21:
                self.sub3Scale = 6
            elif self.sub3TotalPoint >= 22 and self.sub3TotalPoint <= 23:
                self.sub3Scale = 7
            elif self.sub3TotalPoint == 24:
                self.sub3Scale = 8
            elif self.sub3TotalPoint == 25:
                self.sub3Scale = 9
            elif self.sub3TotalPoint == 26:
                self.sub3Scale = 10
            elif self.sub3TotalPoint == 27:
                self.sub3Scale = 11
            elif self.sub3TotalPoint == 28:
                self.sub3Scale = 12
            elif self.sub3TotalPoint == 29:
                self.sub3Scale = 13
            elif self.sub3TotalPoint == 30:
                self.sub3Scale = 14
            elif self.sub3TotalPoint == 31:
                self.sub3Scale = 15
            elif self.sub3TotalPoint == 32:
                self.sub3Scale = 16
            elif self.sub3TotalPoint == 33:
                self.sub3Scale = 17
            elif self.sub3TotalPoint == 34:
                self.sub3Scale = 19
            elif self.sub3TotalPoint == 35:
                self.sub3Scale = 20
            elif self.sub3TotalPoint == 36:
                self.sub3Scale = 22
            elif self.sub3TotalPoint == 37:
                self.sub3Scale = 23
            elif self.sub3TotalPoint == 38:
                self.sub3Scale = 25
            elif self.sub3TotalPoint >= 39 and self.sub3TotalPoint <= 40:
                self.sub3Scale = 26
            elif self.sub3TotalPoint >= 41 and self.sub3TotalPoint <= 42:
                self.sub3Scale = 27
            elif self.sub3TotalPoint == 43:
                self.sub3Scale = 28
            elif self.sub3TotalPoint == 44:
                self.sub3Scale = 30
            elif self.sub3TotalPoint == 45:
                self.sub3Scale = 31
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
            
            if self.sub4TotalPoint >= 0 and self.sub4TotalPoint <= 2:
                self.sub4Scale = 1
            elif self.sub4TotalPoint == 3:
                self.sub4Scale = 2
            elif self.sub4TotalPoint >= 4 and self.sub4TotalPoint <= 5:
                self.sub4Scale = 3 
            elif self.sub4TotalPoint >= 6 and self.sub4TotalPoint <= 8:
                self.sub4Scale = 4
            elif self.sub4TotalPoint >= 9 and self.sub4TotalPoint <= 11:
                self.sub4Scale = 5
            elif self.sub4TotalPoint >= 12 and self.sub4TotalPoint <= 14:
                self.sub4Scale = 6
            elif self.sub4TotalPoint >= 15 and self.sub4TotalPoint <= 17:
                self.sub4Scale = 7
            elif self.sub4TotalPoint >= 18 and self.sub4TotalPoint <= 19:
                self.sub4Scale = 8
            elif self.sub4TotalPoint == 20:
                self.sub4Scale = 9
            elif self.sub4TotalPoint == 21:
                self.sub4Scale = 10
            elif self.sub4TotalPoint == 22:
                self.sub4Scale = 13
            elif self.sub4TotalPoint == 23:
                self.sub4Scale = 16
            elif self.sub4TotalPoint == 24:
                self.sub4Scale = 20
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
            
            if self.sub5TotalPoint >= 0 and self.sub5TotalPoint <= 7:
                self.sub5Scale = 1
            elif self.sub5TotalPoint >= 8 and self.sub5TotalPoint <= 11:
                self.sub5Scale = 2
            elif self.sub5TotalPoint >= 12 and self.sub5TotalPoint <= 16:
                self.sub5Scale = 3 
            elif self.sub5TotalPoint >= 17 and self.sub5TotalPoint <= 20:
                self.sub5Scale = 4
            elif self.sub5TotalPoint >= 21 and self.sub5TotalPoint <= 23:
                self.sub5Scale = 5
            elif self.sub5TotalPoint >= 24 and self.sub5TotalPoint <= 26:
                self.sub5Scale = 6
            elif self.sub5TotalPoint >= 27 and self.sub5TotalPoint <= 28:
                self.sub5Scale = 7
            elif self.sub5TotalPoint == 29:
                self.sub5Scale = 8
            elif self.sub5TotalPoint == 30:
                self.sub5Scale = 9
            elif self.sub5TotalPoint == 31:
                self.sub5Scale = 10
            elif self.sub5TotalPoint == 32:
                self.sub5Scale = 12
            elif self.sub5TotalPoint == 33:
                self.sub5Scale = 14
            elif self.sub5TotalPoint == 34:
                self.sub5Scale = 16
            elif self.sub5TotalPoint == 35:
                self.sub5Scale = 18
            elif self.sub5TotalPoint == 36:
                self.sub5Scale = 20
            elif self.sub5TotalPoint == 37:
                self.sub5Scale = 23
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
            
            if self.sub6TotalPoint >= 0 and self.sub6TotalPoint <= 4:
                self.sub6Scale = 1
            elif self.sub6TotalPoint >= 5 and self.sub6TotalPoint <= 7:
                self.sub6Scale = 2
            elif self.sub6TotalPoint >= 8 and self.sub6TotalPoint <= 11:
                self.sub6Scale = 3 
            elif self.sub6TotalPoint >= 12 and self.sub6TotalPoint <= 15:
                self.sub6Scale = 4
            elif self.sub6TotalPoint >= 16 and self.sub6TotalPoint <= 18:
                self.sub6Scale = 5
            elif self.sub6TotalPoint >= 19 and self.sub6TotalPoint <= 21:
                self.sub6Scale = 6
            elif self.sub6TotalPoint >= 22 and self.sub6TotalPoint <= 24:
                self.sub6Scale = 7
            elif self.sub6TotalPoint == 25:
                self.sub6Scale = 8
            elif self.sub6TotalPoint == 26:
                self.sub6Scale = 9
            elif self.sub6TotalPoint >= 27 and self.sub6TotalPoint <= 28:
                self.sub6Scale = 10
            elif self.sub6TotalPoint >= 29 and self.sub6TotalPoint <= 30:
                self.sub6Scale = 11
            elif self.sub6TotalPoint >= 31 and self.sub6TotalPoint <= 32:
                self.sub6Scale = 12
            elif self.sub6TotalPoint == 33:
                self.sub6Scale = 13
            elif self.sub6TotalPoint == 34:
                self.sub6Scale = 14
            elif self.sub6TotalPoint == 35:
                self.sub6Scale = 15
            elif self.sub6TotalPoint >= 36 and self.sub6TotalPoint <= 37:
                self.sub6Scale = 16
            elif self.sub6TotalPoint == 38:
                self.sub6Scale = 17
            elif self.sub6TotalPoint == 39:
                self.sub6Scale = 18
            elif self.sub6TotalPoint == 40:
                self.sub6Scale = 19
            elif self.sub6TotalPoint >= 41 and self.sub6TotalPoint <= 42:
                self.sub6Scale = 20
            elif self.sub6TotalPoint == 43:
                self.sub6Scale = 21
            elif self.sub6TotalPoint == 44:
                self.sub6Scale = 23
            elif self.sub6TotalPoint >= 45 and self.sub6TotalPoint <= 46:
                self.sub6Scale = 24
            elif self.sub6TotalPoint == 47:
                self.sub6Scale = 25
            elif self.sub6TotalPoint == 48:
                self.sub6Scale = 26
            elif self.sub6TotalPoint == 49:
                self.sub6Scale = 27
            elif self.sub6TotalPoint == 50:
                self.sub6Scale = 29
            elif self.sub6TotalPoint == 51:
                self.sub6Scale = 30
            elif self.sub6TotalPoint == 52:
                self.sub6Scale = 32
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")

            if self.sub7TotalPoint >= 0 and self.sub7TotalPoint <= 4:
                self.sub7Scale = 1
            elif self.sub7TotalPoint >= 5 and self.sub7TotalPoint <= 9:
                self.sub7Scale = 2
            elif self.sub7TotalPoint >= 10 and self.sub7TotalPoint <= 12:
                self.sub7Scale = 3 
            elif self.sub7TotalPoint >= 13 and self.sub7TotalPoint <= 16:
                self.sub7Scale = 4
            elif self.sub7TotalPoint >= 17 and self.sub7TotalPoint <= 20:
                self.sub7Scale = 5
            elif self.sub7TotalPoint >= 21 and self.sub7TotalPoint <= 24:
                self.sub7Scale = 6
            elif self.sub7TotalPoint >= 25 and self.sub7TotalPoint <= 27:
                self.sub7Scale = 7
            elif self.sub7TotalPoint >= 28 and self.sub7TotalPoint <= 29:
                self.sub7Scale = 8
            elif self.sub7TotalPoint >= 30 and self.sub7TotalPoint <= 31:
                self.sub7Scale = 9
            elif self.sub7TotalPoint >= 32 and self.sub7TotalPoint <= 33:
                self.sub7Scale = 10
            elif self.sub7TotalPoint == 34:
                self.sub7Scale = 11
            elif self.sub7TotalPoint == 35:
                self.sub7Scale = 13
            elif self.sub7TotalPoint == 36:
                self.sub7Scale = 15
            elif self.sub7TotalPoint == 37:
                self.sub7Scale = 17
            elif self.sub7TotalPoint == 38:
                self.sub7Scale = 20
            elif self.sub7TotalPoint == 39:
                self.sub7Scale = 23
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
            
            if self.sub8TotalPoint >= 0 and self.sub8TotalPoint <= 1:
                self.sub8Scale = 1
            elif self.sub8TotalPoint >= 2 and self.sub8TotalPoint <= 3:
                self.sub8Scale = 2
            elif self.sub8TotalPoint >= 4 and self.sub8TotalPoint <= 6:
                self.sub8Scale = 3 
            elif self.sub8TotalPoint >= 7 and self.sub8TotalPoint <= 8:
                self.sub8Scale = 4
            elif self.sub8TotalPoint >= 9 and self.sub8TotalPoint <= 10:
                self.sub8Scale = 5
            elif self.sub8TotalPoint >= 11 and self.sub8TotalPoint <= 13:
                self.sub8Scale = 6
            elif self.sub8TotalPoint >= 14 and self.sub8TotalPoint <= 15:
                self.sub8Scale = 7
            elif self.sub8TotalPoint == 16:
                self.sub8Scale = 8
            elif self.sub8TotalPoint == 17:
                self.sub8Scale = 9
            elif self.sub8TotalPoint == 18:
                self.sub8Scale = 10
            elif self.sub8TotalPoint >= 19 and self.sub8TotalPoint <= 20:
                self.sub8Scale = 11
            elif self.sub8TotalPoint >= 21 and self.sub8TotalPoint <= 22:
                self.sub8Scale = 12
            elif self.sub8TotalPoint == 23:
                self.sub8Scale = 13
            elif self.sub8TotalPoint >= 24 and self.sub8TotalPoint <= 25:
                self.sub8Scale = 14
            elif self.sub8TotalPoint == 26:
                self.sub8Scale = 15
            elif self.sub8TotalPoint == 27:
                self.sub8Scale = 16
            elif self.sub8TotalPoint == 28:
                self.sub8Scale = 17
            elif self.sub8TotalPoint == 29:
                self.sub8Scale = 18
            elif self.sub8TotalPoint == 30:
                self.sub8Scale = 19
            elif self.sub8TotalPoint == 31:
                self.sub8Scale = 20
            elif self.sub8TotalPoint >= 32 and self.sub8TotalPoint <= 33:
                self.sub8Scale = 21
            elif self.sub8TotalPoint == 34:
                self.sub8Scale = 22
            elif self.sub8TotalPoint == 35:
                self.sub8Scale = 23
            elif self.sub8TotalPoint == 36:
                self.sub8Scale = 24
            elif self.sub8TotalPoint >= 37 and self.sub8TotalPoint <= 38:
                self.sub8Scale = 26
            elif self.sub8TotalPoint == 39:
                self.sub8Scale = 28
            elif self.sub8TotalPoint == 40:
                self.sub8Scale = 29
            elif self.sub8TotalPoint == 41:
                self.sub8Scale = 30
            elif self.sub8TotalPoint == 42:
                self.sub8Scale = 32
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")

        self.FMC = self.sub1Scale + self.sub2Scale
        self.MC = self.sub3Scale + self.sub7Scale
        self.BC = self.sub4Scale + self.sub5Scale
        self.SA = self.sub6Scale + self.sub8Scale

        self.FMCGrid.addWidget(QLabel(str(self.sub1TotalPoint)), 1, 1, alignment=QtCore.Qt.AlignCenter)
        self.FMCGrid.addWidget(QLabel(str(self.sub1Scale)), 1, 2, alignment=QtCore.Qt.AlignCenter)
        self.FMCGrid.addWidget(QLabel(str(self.sub2TotalPoint)), 2, 1, alignment=QtCore.Qt.AlignCenter)
        self.FMCGrid.addWidget(QLabel(str(self.sub2Scale)), 2, 2, alignment=QtCore.Qt.AlignCenter)
        self.FMCGrid.addWidget(QLabel("sum"), 3, 1, alignment=QtCore.Qt.AlignCenter)
        self.FMCGrid.addWidget(QLabel(str(self.FMC)), 3, 2, alignment=QtCore.Qt.AlignCenter)
        
        self.MCGrid.addWidget(QLabel(str(self.sub3TotalPoint)), 1, 1, alignment=QtCore.Qt.AlignCenter)
        self.MCGrid.addWidget(QLabel(str(self.sub3Scale)), 1, 2, alignment=QtCore.Qt.AlignCenter)
        self.MCGrid.addWidget(QLabel(str(self.sub7TotalPoint)), 2, 1, alignment=QtCore.Qt.AlignCenter)
        self.MCGrid.addWidget(QLabel(str(self.sub7Scale)), 2, 2, alignment=QtCore.Qt.AlignCenter)
        self.MCGrid.addWidget(QLabel("sum"), 3, 1, alignment=QtCore.Qt.AlignCenter)
        self.MCGrid.addWidget(QLabel(str(self.MC)), 3, 2, alignment=QtCore.Qt.AlignCenter)
        
        self.BCGrid.addWidget(QLabel(str(self.sub4TotalPoint)), 1, 1, alignment=QtCore.Qt.AlignCenter)
        self.BCGrid.addWidget(QLabel(str(self.sub4Scale)), 1, 2, alignment=QtCore.Qt.AlignCenter)
        self.BCGrid.addWidget(QLabel(str(self.sub5TotalPoint)), 2, 1, alignment=QtCore.Qt.AlignCenter)
        self.BCGrid.addWidget(QLabel(str(self.sub5Scale)), 2, 2, alignment=QtCore.Qt.AlignCenter)
        self.BCGrid.addWidget(QLabel("sum"), 3, 1, alignment=QtCore.Qt.AlignCenter)
        self.BCGrid.addWidget(QLabel(str(self.BC)), 3, 2, alignment=QtCore.Qt.AlignCenter) 

        self.SAGrid.addWidget(QLabel(str(self.sub6TotalPoint)), 1, 1, alignment=QtCore.Qt.AlignCenter)
        self.SAGrid.addWidget(QLabel(str(self.sub6Scale)), 1, 2, alignment=QtCore.Qt.AlignCenter)
        self.SAGrid.addWidget(QLabel(str(self.sub8TotalPoint)), 2, 1, alignment=QtCore.Qt.AlignCenter)
        self.SAGrid.addWidget(QLabel(str(self.sub8Scale)), 2, 2, alignment=QtCore.Qt.AlignCenter)
        self.SAGrid.addWidget(QLabel("sum"), 3, 1, alignment=QtCore.Qt.AlignCenter)
        self.SAGrid.addWidget(QLabel(str(self.SA)), 3, 2, alignment=QtCore.Qt.AlignCenter)

        self.standardCombined()

    def standardCombined(self):
        if self.FMC >= 44:
            self.FMCstandard = 72
        elif self.FMC >= 43:
            self.FMCstandard = 69
        elif self.FMC >= 42:
            self.FMCstandard = 67
        elif self.FMC >= 41:
            self.FMCstandard = 65
        elif self.FMC >= 40:
            self.FMCstandard = 63
        elif self.FMC >= 39:
            self.FMCstandard = 61
        elif self.FMC >= 38:
            self.FMCstandard = 60
        elif self.FMC >= 37:
            self.FMCstandard = 58
        elif self.FMC >= 36:
            self.FMCstandard = 57
        elif self.FMC >= 35:
            self.FMCstandard = 55
        elif self.FMC >= 34:
            self.FMCstandard = 54
        elif self.FMC >= 33:
            self.FMCstandard = 53
        elif self.FMC >= 32:
            self.FMCstandard = 51
        elif self.FMC >= 31:
            self.FMCstandard = 50
        elif self.FMC >= 30:
            self.FMCstandard = 49
        elif self.FMC >= 29:
            self.FMCstandard = 48
        elif self.FMC >= 28:
            self.FMCstandard = 47
        elif self.FMC >= 27:
            self.FMCstandard = 46
        elif self.FMC >= 26:
            self.FMCstandard = 45
        elif self.FMC >= 25:
            self.FMCstandard = 44
        elif self.FMC >= 24:
            self.FMCstandard = 43
        elif self.FMC >= 23:
            self.FMCstandard = 42
        elif self.FMC >= 22:
            self.FMCstandard = 40
        elif self.FMC >= 21:
            self.FMCstandard = 39
        elif self.FMC >= 20:
            self.FMCstandard = 38
        elif self.FMC >= 19:
            self.FMCstandard = 37
        elif self.FMC >= 18:
            self.FMCstandard = 36
        elif self.FMC >= 17:
            self.FMCstandard = 35
        elif self.FMC >= 16:
            self.FMCstandard = 34
        elif self.FMC >= 15:
            self.FMCstandard = 33
        elif self.FMC >= 14:
            self.FMCstandard = 32
        elif self.FMC >= 13:
            self.FMCstandard = 31
        elif self.FMC >= 12:
            self.FMCstandard = 30
        elif self.FMC >= 11:
            self.FMCstandard = 29
        elif self.FMC >= 10:
            self.FMCstandard = 28
        elif self.FMC >= 9:
            self.FMCstandard = 27
        elif self.FMC >= 8:
            self.FMCstandard = 26
        elif self.FMC >= 7:
            self.FMCstandard = 25
        elif self.FMC >= 6:
            self.FMCstandard = 24
        elif self.FMC >= 5:
            self.FMCstandard = 23
        elif self.FMC >= 4:
            self.FMCstandard = 21
        elif self.FMC >= 3 and self.FMC <= 2:
            self.FMCstandard = 20
        else:
            QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
        
        if self.MC >= 54:
            self.MCstandard = 79
        elif self.MC >= 53:
            self.MCstandard = 78
        elif self.MC >= 52:
            self.MCstandard = 76
        elif self.MC >= 51:
            self.MCstandard = 75
        elif self.MC >= 50:
            self.MCstandard = 74
        elif self.MC >= 49:
            self.MCstandard = 72
        elif self.MC >= 48:
            self.MCstandard = 71
        elif self.MC >= 47:
            self.MCstandard = 70
        elif self.MC >= 46:
            self.MCstandard = 69
        elif self.MC >= 45:
            self.MCstandard = 68
        elif self.MC >= 44:
            self.MCstandard = 67
        elif self.MC >= 42 and self.MC <= 43:
            self.MCstandard = 66
        elif self.MC >= 41:
            self.MCstandard = 64
        elif self.MC >= 40:
            self.MCstandard = 62
        elif self.MC >= 39:
            self.MCstandard = 60
        elif self.MC >= 38:
            self.MCstandard = 59
        elif self.MC >= 37:
            self.MCstandard = 58
        elif self.MC >= 36:
            self.MCstandard = 57
        elif self.MC >= 35:
            self.MCstandard = 56
        elif self.MC >= 34:
            self.MCstandard = 55
        elif self.MC >= 33:
            self.MCstandard = 54
        elif self.MC >= 32:
            self.MCstandard = 52
        elif self.MC >= 31:
            self.MCstandard = 51
        elif self.MC >= 30:
            self.MCstandard = 50
        elif self.MC >= 29:
            self.MCstandard = 48
        elif self.MC >= 28:
            self.MCstandard = 47
        elif self.MC >= 27:
            self.MCstandard = 46
        elif self.MC >= 26:
            self.MCstandard = 44
        elif self.MC >= 25:
            self.MCstandard = 43
        elif self.MC >= 24:
            self.MCstandard = 41
        elif self.MC >= 23:
            self.MCstandard = 40
        elif self.MC >= 22:
            self.MCstandard = 39
        elif self.MC >= 21:
            self.MCstandard = 38
        elif self.MC >= 20:
            self.MCstandard = 37
        elif self.MC >= 19:
            self.MCstandard = 36
        elif self.MC >= 18:
            self.MCstandard = 34
        elif self.MC >= 17:
            self.MCstandard = 33
        elif self.MC >= 15 and self.MC <= 16:
            self.MCstandard = 32
        elif self.MC >= 14:
            self.MCstandard = 31
        elif self.MC >= 12 and self.MC <= 13:
            self.MCstandard = 30
        elif self.MC >= 11:
            self.MCstandard = 29
        elif self.MC >= 9 and self.MC <= 10:
            self.MCstandard = 28
        elif self.MC >= 8:
            self.MCstandard = 27
        elif self.MC >= 7:
            self.MCstandard = 26
        elif self.MC >= 6:
            self.MCstandard = 25
        elif self.MC >= 4 and self.MC <= 5:
            self.MCstandard = 24
        elif self.MC >= 3:
            self.MCstandard = 22
        elif self.MC >= 2:
            self.MCstandard = 21
        else:
            QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")

        if self.BC >= 43:
            self.BCstandard = 67
        elif self.BC >= 42:
            self.BCstandard = 65
        elif self.BC >= 41:
            self.BCstandard = 64
        elif self.BC >= 40:
            self.BCstandard = 63
        elif self.BC >= 39:
            self.BCstandard = 62
        elif self.BC >= 38:
            self.BCstandard = 61
        elif self.BC >= 37:
            self.BCstandard = 59
        elif self.BC >= 36:
            self.BCstandard = 57
        elif self.BC >= 35:
            self.BCstandard = 55
        elif self.BC >= 34:
            self.BCstandard = 54
        elif self.BC >= 33:
            self.BCstandard = 52
        elif self.BC >= 32:
            self.BCstandard = 51
        elif self.BC >= 30 and self.BC <= 31:
            self.BCstandard = 50
        elif self.BC >= 29:
            self.BCstandard = 48
        elif self.BC >= 28:
            self.BCstandard = 46
        elif self.BC >= 27:
            self.BCstandard = 45
        elif self.BC >= 26:
            self.BCstandard = 44
        elif self.BC >= 25:
            self.BCstandard = 43
        elif self.BC >= 24:
            self.BCstandard = 41
        elif self.BC >= 23:
            self.BCstandard = 40
        elif self.BC >= 22:
            self.BCstandard = 39
        elif self.BC >= 21:
            self.BCstandard = 38
        elif self.BC >= 20:
            self.BCstandard = 37
        elif self.BC >= 19:
            self.BCstandard = 36
        elif self.BC >= 18:
            self.BCstandard = 35
        elif self.BC >= 17:
            self.BCstandard = 34
        elif self.BC >= 16:
            self.BCstandard = 33
        elif self.BC >= 15:
            self.BCstandard = 32
        elif self.BC >= 14:
            self.BCstandard = 31
        elif self.BC >= 13:
            self.BCstandard = 30
        elif self.BC >= 11 and self.BC <= 12:
            self.BCstandard = 29
        elif self.BC >= 10:
            self.BCstandard = 28
        elif self.BC >= 8 and self.BC <= 9:
            self.BCstandard = 27
        elif self.BC >= 7:
            self.BCstandard = 26
        elif self.BC >= 5 and self.BC <= 6:
            self.BCstandard = 25
        elif self.BC >= 4:
            self.BCstandard = 24
        elif self.BC >= 3:
            self.BCstandard = 22
        elif self.BC >= 2:
            self.BCstandard = 20
        else:
            QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
        
        if self.SA >= 54:
            self.SAstandard = 80
        elif self.SA >= 53:
            self.SAstandard = 79
        elif self.SA >= 52:
            self.SAstandard = 78
        elif self.SA >= 51:
            self.SAstandard = 77
        elif self.SA >= 50:
            self.SAstandard = 75
        elif self.SA >= 49:
            self.SAstandard = 73
        elif self.SA >= 48:
            self.SAstandard = 71
        elif self.SA >= 47:
            self.SAstandard = 69
        elif self.SA >= 46:
            self.SAstandard = 68
        elif self.SA >= 45:
            self.SAstandard = 67
        elif self.SA >= 44:
            self.SAstandard = 66
        elif self.SA >= 43:
            self.SAstandard = 64
        elif self.SA >= 42:
            self.SAstandard = 63
        elif self.SA >= 41:
            self.SAstandard = 62
        elif self.SA >= 40:
            self.SAstandard = 61
        elif self.SA >= 39:
            self.SAstandard = 60
        elif self.SA >= 38:
            self.SAstandard = 59
        elif self.SA >= 37:
            self.SAstandard = 58
        elif self.SA >= 36:
            self.SAstandard = 57
        elif self.SA >= 35:
            self.SAstandard = 56
        elif self.SA >= 34:
            self.SAstandard = 54
        elif self.SA >= 33:
            self.SAstandard = 53
        elif self.SA >= 32:
            self.SAstandard = 52
        elif self.SA >= 31:
            self.SAstandard = 51
        elif self.SA >= 30:
            self.SAstandard = 50
        elif self.SA >= 29:
            self.SAstandard = 49
        elif self.SA >= 28:
            self.SAstandard = 47
        elif self.SA >= 27:
            self.SAstandard = 46
        elif self.SA >= 26:
            self.SAstandard = 45
        elif self.SA >= 25:
            self.SAstandard = 44
        elif self.SA >= 24:
            self.SAstandard = 43
        elif self.SA >= 23:
            self.SAstandard = 42
        elif self.SA >= 22:
            self.SAstandard = 41
        elif self.SA >= 21:
            self.SAstandard = 40
        elif self.SA >= 20:
            self.SAstandard = 39
        elif self.SA >= 19:
            self.SAstandard = 38
        elif self.SA >= 18:
            self.SAstandard = 37
        elif self.SA >= 17:
            self.SAstandard = 36
        elif self.SA >= 16:
            self.SAstandard = 35
        elif self.SA >= 15:
            self.SAstandard = 33
        elif self.SA >= 14:
            self.SAstandard = 32
        elif self.SA >= 13:
            self.SAstandard = 30
        elif self.SA >= 11 and self.SA <= 12:
            self.SAstandard = 29
        elif self.SA >= 9 and self.SA <= 10:
            self.SAstandard = 28
        elif self.SA >= 7 and self.SA <= 8:
            self.SAstandard = 27
        elif self.SA >= 6:
            self.SAstandard = 26
        elif self.SA >= 5:
            self.SAstandard = 24
        elif self.SA >= 4:
            self.SAstandard = 23
        elif self.SA >= 3:
            self.SAstandard = 22
        elif self.SA >= 2:
            self.SAstandard = 20
        else:
            QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")

        self.totalStandard = self.FMCstandard + self.MCstandard + self.BCstandard + self.SAstandard

        self.FMCGrid.addWidget(QLabel(str(self.FMCstandard)), 3, 3, alignment=QtCore.Qt.AlignCenter)
        self.MCGrid.addWidget(QLabel(str(self.MCstandard)), 3, 3, alignment=QtCore.Qt.AlignCenter)
        self.BCGrid.addWidget(QLabel(str(self.BCstandard)), 3, 3, alignment=QtCore.Qt.AlignCenter)
        self.SAGrid.addWidget(QLabel(str(self.SAstandard)), 3, 3, alignment=QtCore.Qt.AlignCenter) 

        self.total()

    def total(self):
        self.RGrid.addWidget(QLabel(str(self.totalStandard)), 0, 1) 

        if self.requiredData[5] >= 10.0 and self.requiredData[5] <= 21.0:
            if self.totalStandard >= 272:
                self.TMC = 80
            elif self.totalStandard >= 269:
                self.TMC = 79
            elif self.totalStandard >= 266:
                self.TMC = 78
            elif self.totalStandard >= 262:
                self.TMC = 77
            elif self.totalStandard >= 259:
                self.TMC = 76
            elif self.totalStandard >= 257:
                self.TMC = 75
            elif self.totalStandard >= 255:
                self.TMC = 74
            elif self.totalStandard >= 254:
                self.TMC = 73
            elif self.totalStandard >= 252:
                self.TMC = 72
            elif self.totalStandard >= 251:
                self.TMC = 71
            elif self.totalStandard >= 250:
                self.TMC = 70
            elif self.totalStandard >= 249:
                self.TMC = 69
            elif self.totalStandard >= 246:
                self.TMC = 68
            elif self.totalStandard >= 244:
                self.TMC = 67
            elif self.totalStandard >= 243:
                self.TMC = 66
            elif self.totalStandard >= 240:
                self.TMC = 65
            elif self.totalStandard >= 237:
                self.TMC = 64
            elif self.totalStandard >= 235:
                self.TMC = 63
            elif self.totalStandard >= 233:
                self.TMC = 62
            elif self.totalStandard >= 230:
                self.TMC = 61
            elif self.totalStandard >= 227:
                self.TMC = 60
            elif self.totalStandard >= 224:
                self.TMC = 59
            elif self.totalStandard >= 221:
                self.TMC = 58
            elif self.totalStandard >= 219:
                self.TMC = 57
            elif self.totalStandard >= 216:
                self.TMC = 56
            elif self.totalStandard >= 214:
                self.TMC = 55
            elif self.totalStandard >= 212:
                self.TMC = 54
            elif self.totalStandard >= 210:
                self.TMC = 53
            elif self.totalStandard >= 207:
                self.TMC = 52
            elif self.totalStandard >= 204:
                self.TMC = 51
            elif self.totalStandard >= 201:
                self.TMC = 50
            elif self.totalStandard >= 199:
                self.TMC = 49
            elif self.totalStandard >= 196:
                self.TMC = 48
            elif self.totalStandard >= 192:
                self.TMC = 47
            elif self.totalStandard >= 190:
                self.TMC = 46
            elif self.totalStandard >= 188:
                self.TMC = 45
            elif self.totalStandard >= 185:
                self.TMC = 44
            elif self.totalStandard >= 183:
                self.TMC = 43
            elif self.totalStandard >= 179:
                self.TMC = 42
            elif self.totalStandard >= 176:
                self.TMC = 41
            elif self.totalStandard >= 173:
                self.TMC = 40
            elif self.totalStandard >= 169:
                self.TMC = 39
            elif self.totalStandard >= 165:
                self.TMC = 38
            elif self.totalStandard >= 162:
                self.TMC = 37
            elif self.totalStandard >= 158:
                self.TMC = 36
            elif self.totalStandard >= 152:
                self.TMC = 35
            elif self.totalStandard >= 145:
                self.TMC = 34
            elif self.totalStandard >= 141:
                self.TMC = 33
            elif self.totalStandard >= 136:
                self.TMC = 32
            elif self.totalStandard >= 129:
                self.TMC = 31
            elif self.totalStandard >= 122:
                self.TMC = 30
            elif self.totalStandard >= 118:
                self.TMC = 29
            elif self.totalStandard >= 114:
                self.TMC = 28
            elif self.totalStandard >= 110:
                self.TMC = 27
            elif self.totalStandard >= 106:
                self.TMC = 26
            elif self.totalStandard >= 104:
                self.TMC = 25
            elif self.totalStandard >= 101:
                self.TMC = 24
            elif self.totalStandard >= 99:
                self.TMC = 23
            elif self.totalStandard >= 96:
                self.TMC = 22
            elif self.totalStandard >= 94:
                self.TMC = 21
            elif self.totalStandard >= 80:
                self.TMC = 20
            else:
                QMessageBox.warning(self, "에러", "데이터를 확인해주세요.")
        else:
            pass

        self.RGrid.addWidget(QLabel(str(self.TMC)), 1, 1) 

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
import sys
import re
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QGroupBox, QHBoxLayout, QRadioButton, QWidget, QLineEdit, QLabel, QGridLayout, QMessageBox, QPushButton, QCheckBox, QBoxLayout

class Conversion(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()

        grid.addWidget(self.createRequiredFields(), 0, 0, 1, 1)
        grid.addWidget(self.createResultFields(), 0, 3)
        grid.addWidget(self.createSubTest1Fields(), 1, 0)
        grid.addWidget(self.createSubTest2Fields(), 1, 1)
        grid.addWidget(self.createSubTest3Fields(), 1, 2)
        grid.addWidget(self.createSubTest4Fields(), 1, 3)
        grid.addWidget(self.createSubTest5Fields(), 2, 0)
        grid.addWidget(self.createSubTest6Fields(), 2, 1)
        grid.addWidget(self.createSubTest7Fields(), 2, 2)
        grid.addWidget(self.createSubTest8Fields(), 2, 3)
        grid.addWidget(self.createFineMaualControlFields(), 3, 0)
        grid.addWidget(self.createManualCoordinationFields(), 3, 1)
        grid.addWidget(self.createBodyCoordinationFields(), 3, 2)
        grid.addWidget(self.createStrengthAndAgilityFields(), 3, 3)

        self.setWindowTitle('Score Conversion Program')
        self.setGeometry(300, 300, 1000, 1000)
        self.setLayout(grid)
        self.show()

    def createRequiredFields(self):
        name , age, male, female, birthDate, testDate = "", 0, "", "", 0, 0

        groupBox = QGroupBox('필수입력사항')

        grid = QGridLayout()
        gridPart1 = QGroupBox("성별")
        gridPart2 = QGroupBox("유형 선택")

        gridLayout1 = QBoxLayout(QBoxLayout.TopToBottom)
        gridLayout2 = QBoxLayout(QBoxLayout.TopToBottom)

        gridPart1.setLayout(gridLayout1)
        gridPart2.setLayout(gridLayout2)

        grid.addWidget(QLabel('이름 :'), 0, 0)
        name = QLineEdit(self)
        grid.addWidget(name, 0, 1)

        grid.addWidget(QLabel('나이 :'), 1, 0)
        age = QLineEdit(self)
        grid.addWidget(age, 1, 1)

        grid.addWidget(QLabel('생년월일 :'), 2, 0)
        birthDate = QLineEdit(self)
        grid.addWidget(birthDate, 2, 1)

        grid.addWidget(QLabel('검사일 :'), 3, 0)
        testDate = QLineEdit(self)
        grid.addWidget(testDate, 3, 1)

        male = QRadioButton("남자")
        female = QRadioButton("여자")
        gridLayout1.addWidget(male)
        gridLayout1.addWidget(female)

        onlyMale = QRadioButton("남자 그룹")
        onlyFemale = QRadioButton("여자 그룹")
        Combined = QRadioButton("혼성 그룹")
        gridLayout2.addWidget(onlyMale)
        gridLayout2.addWidget(onlyFemale)
        gridLayout2.addWidget(Combined)

        # groupBox.setMaximumWidth(300)
        grid.addWidget(gridPart1, 0, 2, 4, 1)
        grid.addWidget(gridPart2, 0, 3, 4, 1)

        groupBox.setLayout(grid)
        
        return groupBox

    def createSubTest1Fields(self):
        groupBox = QGroupBox('Subtest 1: Fine Moter Precision')
        grid = QGridLayout()

        grid.addWidget(QLabel('항목'), 0, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Raw Score'), 0, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Point Score'), 0, 2, alignment=QtCore.Qt.AlignCenter)

        grid.addWidget(QLabel('Filling in Shapes -- Circle : '), 1, 0)
        grid.addWidget(QLabel('Filling in Shapes --Star : '), 2, 0)
        grid.addWidget(QLabel('Drawing Lines Through Paths -- Crooked : '), 3, 0)
        grid.addWidget(QLabel('Drawing Lines Through Paths -- Curved : '), 4, 0)
        grid.addWidget(QLabel('Connecting Dots : '), 5, 0)
        grid.addWidget(QLabel('Folding Paper : '), 6, 0)
        grid.addWidget(QLabel('Cutting Out a Circle : '), 7, 0)
        grid.addWidget(QLabel('Total Point Score Subtest 1 (max=41) : '), 11, 0)

        subTest1 = []
        for i in range(7):
            subTest1.append(QLineEdit(self))
            subTest1[i].setText("")
        for i in range(7):
            grid.addWidget(subTest1[i], i+1, 1)

        convBtn = QPushButton()
        convBtn.setText("변환")
        grid.addWidget(convBtn, 11, 1)       

        groupBox.setLayout(grid)

        return groupBox
    
    def createSubTest2Fields(self):
        groupBox = QGroupBox('Subtest 2: Fine Moter intergration')
        grid = QGridLayout()

        grid.addWidget(QLabel('항목'), 0, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Raw Score'), 0, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Point Score'), 0, 2, alignment=QtCore.Qt.AlignCenter)

        grid.addWidget(QLabel('Copying a Circle : '), 1, 0)
        grid.addWidget(QLabel('Copying a Square : '), 2, 0)
        grid.addWidget(QLabel('Copying Overlapping Circles : '), 3, 0)
        grid.addWidget(QLabel('Copying a Wavy Line : '), 4, 0)
        grid.addWidget(QLabel('Copying a Triangle : '), 5, 0)
        grid.addWidget(QLabel('Copying a Diamond : '), 6, 0)
        grid.addWidget(QLabel('Copying a Star : '), 7, 0)
        grid.addWidget(QLabel('Copying Overlapping Pencils : '), 8, 0)
        grid.addWidget(QLabel('Total Point Score Subtest 2 (max=40) : '), 11, 0)

        subTest2 = []
        for i in range(8):
            subTest2.append(QLineEdit(self))
            subTest2[i].setText("")
        for i in range(8):
            grid.addWidget(subTest2[i], i+1, 1)

        convBtn = QPushButton()
        convBtn.setText("변환")
        grid.addWidget(convBtn, 11, 1)       

        groupBox.setLayout(grid)

        return groupBox

    def createSubTest3Fields(self):
        groupBox = QGroupBox('Subtest 3: Manual Dexterity')
        grid = QGridLayout()

        grid.addWidget(QLabel('항목'), 0, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Raw Score'), 0, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Point Score'), 0, 2, alignment=QtCore.Qt.AlignCenter)

        grid.addWidget(QLabel('Making Dots in Circles : '), 1, 0)
        grid.addWidget(QLabel('Transferring Pennies : '), 2, 0)
        grid.addWidget(QLabel('Placing Pegs into a Pegboard : '), 3, 0)
        grid.addWidget(QLabel('Sorting Cards : '), 4, 0)
        grid.addWidget(QLabel('Sorting Blocks : '), 5, 0)
        grid.addWidget(QLabel('Total Point Score Subtest 3 (max=45) : '), 11, 0)

        subTest3 = []
        for i in range(6):
            subTest3.append(QLineEdit(self))
            subTest3[i].setText("")
        for i in range(6):
            grid.addWidget(subTest3[i], i+1, 1)

        convBtn = QPushButton()
        convBtn.setText("변환")
        grid.addWidget(convBtn, 11, 1)       

        groupBox.setLayout(grid)

        return groupBox

    def createSubTest4Fields(self):
        groupBox = QGroupBox('Subtest 4: Bilateral Coordination')
        grid = QGridLayout()

        grid.addWidget(QLabel('항목'), 0, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Raw Score'), 0, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Point Score'), 0, 2, alignment=QtCore.Qt.AlignCenter)

        grid.addWidget(QLabel('Touching Nose with Index Fingers -- Eyes Closed : '), 1, 0)
        grid.addWidget(QLabel('Jumping Jacks : '), 2, 0)
        grid.addWidget(QLabel('Jumping in Place -- Same Sides Synchronized : '), 3, 0)
        grid.addWidget(QLabel('Jumping in Place -- Opposite Sides Synchronized : '), 4, 0)
        grid.addWidget(QLabel('Pivoting Thumbs and Index Fingers : '), 5, 0)
        grid.addWidget(QLabel('Tapping Feet and Fingers -- Same Sides Synchronized : '), 6, 0)
        grid.addWidget(QLabel('Total Point Score Subtest 4 (max=24) : '), 11, 0)

        subTest2 = []
        for i in range(6):
            subTest2.append(QLineEdit(self))
            subTest2[i].setText("")
        for i in range(6):
            grid.addWidget(subTest2[i], i+1, 1)

        convBtn = QPushButton()
        convBtn.setText("변환")
        grid.addWidget(convBtn, 11, 1)       

        groupBox.setLayout(grid)

        return groupBox

    def createSubTest5Fields(self):
        groupBox = QGroupBox('Subtest 5: Balance')
        grid = QGridLayout()

        grid.addWidget(QLabel('항목'), 0, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Raw Score'), 0, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Point Score'), 0, 2, alignment=QtCore.Qt.AlignCenter)

        grid.addWidget(QLabel('Standing with Feet Apart on a Line -- Eyes Open: '), 1, 0)
        grid.addWidget(QLabel('Walking Forward on a Line : '), 2, 0)
        grid.addWidget(QLabel('Standing on One Leg on a Line -- Eyes Open : '), 3, 0)
        grid.addWidget(QLabel('Standing on One Leg on a Line -- Eyes Closed : '), 4, 0)
        grid.addWidget(QLabel('Walking Forward Heel-to-Toe on a Line : '), 5, 0)
        grid.addWidget(QLabel('Standing on One Leg on a Line -- Eyes Closed : '), 6, 0)
        grid.addWidget(QLabel('Standing on One Leg on a Balance Beam -- Eyes Open : '), 7, 0)
        grid.addWidget(QLabel('Standing Heel-to-Toe on a Balance Beam : '), 8, 0)
        grid.addWidget(QLabel('Starnding on One Leg on a Balance Beam -- Eyes Closed : '), 9, 0)
        grid.addWidget(QLabel('Total Point Score Subtest 5 (max=37) : '), 11, 0)

        subTest5 = []
        for i in range(9):
            subTest5.append(QLineEdit(self))
            subTest5[i].setText("")
        for i in range(9):
            grid.addWidget(subTest5[i], i+1, 1)

        convBtn = QPushButton()
        convBtn.setText("변환")
        grid.addWidget(convBtn, 11, 1)       

        groupBox.setLayout(grid)

        return groupBox

    def createSubTest6Fields(self):
        groupBox = QGroupBox('Subtest 6: Running Speed and Agility')
        grid = QGridLayout()

        grid.addWidget(QLabel('항목'), 0, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Raw Score'), 0, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Point Score'), 0, 2, alignment=QtCore.Qt.AlignCenter)

        grid.addWidget(QLabel('Shuttle Run : '), 1, 0)
        grid.addWidget(QLabel('Stepping Sideways over a Balance Beam : '), 2, 0)
        grid.addWidget(QLabel('One-Legged Stationary Hop : '), 3, 0)
        grid.addWidget(QLabel('One-Legged Side Hop : '), 4, 0)
        grid.addWidget(QLabel('Two-Legged Side Hop : '), 5, 0)
        grid.addWidget(QLabel('Total Point Score Subtest 6 (max=52) : '), 11, 0)

        subTest6 = []
        for i in range(5):
            subTest6.append(QLineEdit(self))
            subTest6[i].setText("")
        for i in range(5):
            grid.addWidget(subTest6[i], i+1, 1)

        convBtn = QPushButton()
        convBtn.setText("변환")
        grid.addWidget(convBtn, 11, 1)       

        groupBox.setLayout(grid)

        return groupBox

    def createSubTest7Fields(self):
        groupBox = QGroupBox('Subtest 7: Upper-Limb Coordination')
        grid = QGridLayout()

        grid.addWidget(QLabel('항목'), 0, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Raw Score'), 0, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Point Score'), 0, 2, alignment=QtCore.Qt.AlignCenter)

        grid.addWidget(QLabel('Dropping and Catching a Ball -- Both Hands : '), 1, 0)
        grid.addWidget(QLabel('Catching a Tossed Ball -- Both Hands : '), 2, 0)
        grid.addWidget(QLabel('Dropping and Catching a Ball --One Hands : '), 3, 0)
        grid.addWidget(QLabel('Catching a Tossed Ball --One Hands : '), 4, 0)
        grid.addWidget(QLabel('Dribbling a Ball -- One Hand : '), 5, 0)
        grid.addWidget(QLabel('Dribbling a Ball -- Alternating Hands : '), 6, 0)
        grid.addWidget(QLabel('Throwing a Ball at a Target : '), 7, 0)
        grid.addWidget(QLabel('Total Point Score Subtest 7 (max=39) : '), 11, 0)

        subTest7 = []
        for i in range(7):
            subTest7.append(QLineEdit(self))
            subTest7[i].setText("")
        for i in range(7):
            grid.addWidget(subTest7[i], i+1, 1)

        convBtn = QPushButton()
        convBtn.setText("변환")
        grid.addWidget(convBtn, 11, 1)       

        groupBox.setLayout(grid)

        return groupBox

    def createSubTest8Fields(self):
        groupBox = QGroupBox('Subtest 8: Strength')
        grid = QGridLayout()

        grid.addWidget(QLabel('항목'), 0, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Raw Score'), 0, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('Point Score'), 0, 2, alignment=QtCore.Qt.AlignCenter)

        grid.addWidget(QLabel('Standing Long Jump : '), 1, 0)
        grid.addWidget(QLabel('Knee Push-ups : '), 2, 0)
        grid.addWidget(QLabel('Sit-ups : '), 3, 0)
        grid.addWidget(QLabel('Wall Sit : '), 4, 0)
        grid.addWidget(QLabel('V-up : '), 5, 0)
        grid.addWidget(QLabel('Total Point Score Subtest 8 (max=42) : '), 11, 0)

        subTest8 = []
        for i in range(5):
            subTest8.append(QLineEdit(self))
            subTest8[i].setText("")
        for i in range(5):
            grid.addWidget(subTest8[i], i+1, 1)

        convBtn = QPushButton()
        convBtn.setText("변환")
        grid.addWidget(convBtn, 11, 1)       

        groupBox.setLayout(grid)

        return groupBox

    def createFineMaualControlFields(self):
        groupBox = QGroupBox('Find Manual Control')
        grid = QGridLayout()

        grid.addWidget(QLabel('Total Point Score'), 0, 1)
        grid.addWidget(QLabel('Scale Score'), 0, 2)
        grid.addWidget(QLabel('Standard Score'), 0, 3)
        grid.addWidget(QLabel('1. Find Motor Precision'), 1, 0)
        grid.addWidget(QLabel('2. Find Motor Integration'), 2, 0)
        grid.addWidget(QLabel('Find Manual Control'), 3, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('5'), 1, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('6'), 1, 2, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('7'), 2, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('8'), 2, 2, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('sum : 10'), 3, 2)
        grid.addWidget(QLabel('11'), 3, 3, alignment=QtCore.Qt.AlignCenter)

        groupBox.setLayout(grid)
        return groupBox

    def createManualCoordinationFields(self):
        groupBox = QGroupBox('Manual Coordination')
        grid = QGridLayout()

        grid.addWidget(QLabel('Total Point Score'), 0, 1)
        grid.addWidget(QLabel('Scale Score'), 0, 2)
        grid.addWidget(QLabel('Standard Score'), 0, 3)
        grid.addWidget(QLabel('3. Manual Dexterity'), 1, 0)
        grid.addWidget(QLabel('7. Upper-Limb Coordination'), 2, 0)
        grid.addWidget(QLabel('Manual Coordination'), 3, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('5'), 1, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('6'), 1, 2, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('7'), 2, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('8'), 2, 2, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('sum : 10'), 3, 2)
        grid.addWidget(QLabel('11'), 3, 3, alignment=QtCore.Qt.AlignCenter)

        groupBox.setLayout(grid)
        return groupBox

    def createBodyCoordinationFields(self):
        groupBox = QGroupBox('Body Coordination')
        grid = QGridLayout()

        grid.addWidget(QLabel('Total Point Score'), 0, 1)
        grid.addWidget(QLabel('Scale Score'), 0, 2)
        grid.addWidget(QLabel('Standard Score'), 0, 3)
        grid.addWidget(QLabel('4. Bilateral Coordination'), 1, 0)
        grid.addWidget(QLabel('5. Balance'), 2, 0)
        grid.addWidget(QLabel('Body Coordination'), 3, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('5'), 1, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('6'), 1, 2, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('7'), 2, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('8'), 2, 2, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('sum : 10'), 3, 2)
        grid.addWidget(QLabel('11'), 3, 3, alignment=QtCore.Qt.AlignCenter)

        groupBox.setLayout(grid)
        return groupBox

    def createStrengthAndAgilityFields(self):
        groupBox = QGroupBox('Strength and Agility')
        grid = QGridLayout()

        grid.addWidget(QLabel('Total Point Score'), 0, 1)
        grid.addWidget(QLabel('Scale Score'), 0, 2)
        grid.addWidget(QLabel('Standard Score'), 0, 3)
        grid.addWidget(QLabel('6. Running Speed and Agility'), 1, 0)
        grid.addWidget(QLabel('8. Strength Push-up: Knee Full'), 2, 0)
        grid.addWidget(QLabel('Strength and Agility'), 3, 0, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('5'), 1, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('6'), 1, 2, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('7'), 2, 1, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('8'), 2, 2, alignment=QtCore.Qt.AlignCenter)
        grid.addWidget(QLabel('sum : 10'), 3, 2)
        grid.addWidget(QLabel('11'), 3, 3, alignment=QtCore.Qt.AlignCenter)

        groupBox.setLayout(grid)
        return groupBox

    def createResultFields(self):
        groupBox = QGroupBox('Result')
        grid = QGridLayout()

        grid.addWidget(QLabel('Total Motor Composite'), 0, 0)
        grid.addWidget(QLabel('111'), 0, 1)

        groupBox.setLayout(grid)
        return groupBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Conversion()
    sys.exit(app.exec_())
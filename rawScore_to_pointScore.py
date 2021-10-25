import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QMessageBox, QPushButton

class Conversion(QWidget):

    def __init__(self):
        super().__init__()
        self.setting()
        self.initUI()

    def setting(self):
        self.raw_arr_1 = []
        self.raw_arr_2 = []
        self.raw_arr_3 = []
        self.raw_arr_4 = []
        self.raw_arr_5 = []
        self.raw_arr_6 = []
        self.raw_arr_7 = []
        self.raw_arr_8 = []

        self.point_arr_1 = []
        self.point_arr_2 = []
        self.point_arr_3 = []
        self.point_arr_4 = []
        self.point_arr_5 = []
        self.point_arr_6 = []
        self.point_arr_7 = []
        self.point_arr_8 = []


        for i in range(7):
            self.raw_arr_1.append(QLineEdit(self))
            self.raw_arr_1[i].setText("")
        for i in range(8):
            self.raw_arr_2.append(QLineEdit(self))
            self.raw_arr_2[i].setText("")
        for i in range(5):
            self.raw_arr_3.append(QLineEdit(self))
            self.raw_arr_3[i].setText("")
        for i in range(7):
            self.raw_arr_4.append(QLineEdit(self))
            self.raw_arr_4[i].setText("")
        for i in range(9):
            self.raw_arr_5.append(QLineEdit(self))
            self.raw_arr_5[i].setText("")
        for i in range(5):
            self.raw_arr_6.append(QLineEdit(self))
            self.raw_arr_6[i].setText("")
        for i in range(7):
            self.raw_arr_7.append(QLineEdit(self))
            self.raw_arr_7[i].setText("")
        for i in range(5):
            self.raw_arr_8.append(QLineEdit(self))
            self.raw_arr_8[i].setText("")
            
        self.raw_conv_btn_arr = []

        for i in range(8):
            self.raw_conv_btn_arr.append(QPushButton())
            self.raw_conv_btn_arr[i].setText("Conversion")
            self.raw_conv_btn_arr[i].clicked.connect(self.validation)

    def initUI(self):

        self.grid = QGridLayout()
        # Subtest 1: Fine Moter Precision layout
        self.grid.addWidget(QLabel('Subtest 1: Fine Moter Precision'), 0, 0)
        self.grid.addWidget(QLabel('Filling in Shapes -- Circle : '), 1, 0)
        self.grid.addWidget(QLabel('Filling in Shapes --Star : '), 2, 0)
        self.grid.addWidget(QLabel('Drawing Lines Through Paths -- Crooked : '), 3, 0)
        self.grid.addWidget(QLabel('Drawing Lines Through Paths -- Curved : '), 4, 0)
        self.grid.addWidget(QLabel('Connecting Dots : '), 5, 0)
        self.grid.addWidget(QLabel('Folding Paper : '), 6, 0)
        self.grid.addWidget(QLabel('Cutting Out a Circle : '), 7, 0)
        self.grid.addWidget(QLabel('Total Point Score Subtest 1 (max=41) : '), 11, 0)

        self.grid.addWidget(QLabel('Raw Score'), 0, 1)

        self.grid.addWidget(QLabel('Point Score'), 0, 2)

        # Subtest 1 Raw Score form layout
        for i in range(7):
            self.grid.addWidget(self.raw_arr_1[i], i+1, 1)

         # Subtest 2: Fine Moter intergration layout
        self.grid.addWidget(QLabel('Subtest 2: Fine Moter intergration'), 0, 3)
        self.grid.addWidget(QLabel('Copying a Circle : '), 1, 3)
        self.grid.addWidget(QLabel('Copying a Square : '), 2, 3)
        self.grid.addWidget(QLabel('Copying Overlapping Circles : '), 3, 3)
        self.grid.addWidget(QLabel('Copying a Wavy Line : '), 4, 3)
        self.grid.addWidget(QLabel('Copying a Triangle : '), 5, 3)
        self.grid.addWidget(QLabel('Copying a Diamond : '), 6, 3)
        self.grid.addWidget(QLabel('Copying a Star : '), 7, 3)
        self.grid.addWidget(QLabel('Copying Overlapping Pencils : '), 8, 3)
        self.grid.addWidget(QLabel('Total Point Score Subtest 2 (max=40) : '), 11, 3)

        self.grid.addWidget(QLabel('Raw Score'), 0, 4)

        self.grid.addWidget(QLabel('Point Score'), 0, 5)

        # Subtest 2 Raw Score form layout
        for i in range(8):
            self.grid.addWidget(self.raw_arr_2[i], i+1, 4)

        # Subtest 3: Manual Dexterity layout
        self.grid.addWidget(QLabel('Subtest 3: Manual Dexterity'), 0, 6)
        self.grid.addWidget(QLabel('Making Dots in Circles : '), 1, 6)
        self.grid.addWidget(QLabel('Transferring Pennies : '), 2, 6)
        self.grid.addWidget(QLabel('Placing Pegs into a Pegboard : '), 3, 6)
        self.grid.addWidget(QLabel('Sorting Cards : '), 4, 6)
        self.grid.addWidget(QLabel('Sorting Blocks : '), 5, 6)
        self.grid.addWidget(QLabel('Total Point Score Subtest 3 (max=45) : '), 11, 6)

        self.grid.addWidget(QLabel('Raw Score'), 0, 7)

        self.grid.addWidget(QLabel('Point Score'), 0, 8)

        # Subtest 3 Raw Score form layout
        for i in range(5):
            self.grid.addWidget(self.raw_arr_3[i], i+1, 7)

        # Subtest 4: Bilateral Coordination layout
        self.grid.addWidget(QLabel('Subtest 4: Bilateral Coordination'), 0, 9)
        self.grid.addWidget(QLabel('Touching Nose with Index Fingers -- Eyes Closed : '), 1, 9)
        self.grid.addWidget(QLabel('Jumping Jacks : '), 2, 9)
        self.grid.addWidget(QLabel('Jumping in Place -- Same Sides Synchronized : '), 3, 9)
        self.grid.addWidget(QLabel('Jumping in Place -- Opposite Sides Synchronized : '), 4, 9)
        self.grid.addWidget(QLabel('Pivoting Thumbs and Index Fingers : '), 5, 9)
        self.grid.addWidget(QLabel('Tapping Feet and Fingers -- Same Sides Synchronized : '), 6, 9)
        self.grid.addWidget(QLabel(' '), 10, 9)
        self.grid.addWidget(QLabel('Total Point Score Subtest 4 (max=24) : '), 11, 9)

        self.grid.addWidget(QLabel('Raw Score'), 0, 10)

        self.grid.addWidget(QLabel('Point Score'), 0, 11)

        for i in range(7):
            self.grid.addWidget(self.raw_arr_4[i], i+1, 10)

        self.grid.addWidget(QLabel('----------------------'), 12, 0)

        # Subtest 5: Balance layout
        self.grid.addWidget(QLabel('Subtest 5: Balance'), 13, 0)
        self.grid.addWidget(QLabel('Standing with Feet Apart on a Line -- Eyes Open: '), 14, 0)
        self.grid.addWidget(QLabel('Walking Forward on a Line : '), 15, 0)
        self.grid.addWidget(QLabel('Standing on One Leg on a Line -- Eyes Open : '), 16, 0)
        self.grid.addWidget(QLabel('Standing on One Leg on a Line -- Eyes Closed : '), 17, 0)
        self.grid.addWidget(QLabel('Walking Forward Heel-to-Toe on a Line : '), 18, 0)
        self.grid.addWidget(QLabel('Standing on One Leg on a Line -- Eyes Closed : '), 19, 0)
        self.grid.addWidget(QLabel('Standing on One Leg on a Balance Beam -- Eyes Open : '), 20, 0)
        self.grid.addWidget(QLabel('Standing Heel-to-Toe on a Balance Beam : '), 21, 0)
        self.grid.addWidget(QLabel('Starnding on One Leg on a Balance Beam -- Eyes Closed : '), 22, 0)
        self.grid.addWidget(QLabel('Total Point Score Subtest 5 (max=37) : '), 23, 0)

        self.grid.addWidget(QLabel('Raw Score'), 13, 1)

        self.grid.addWidget(QLabel('Point Score'), 13, 2)

        for i in range(9):
            self.grid.addWidget(self.raw_arr_5[i], i+14, 1)

        # Subtest 6: Running Speed and Agility layout
        self.grid.addWidget(QLabel('Subtest 6: Running Speed and Agility'), 13, 3)
        self.grid.addWidget(QLabel('Shuttle Run : '), 14, 3)
        self.grid.addWidget(QLabel('Stepping Sideways over a Balance Beam : '), 15, 3)
        self.grid.addWidget(QLabel('One-Legged Stationary Hop : '), 16, 3)
        self.grid.addWidget(QLabel('One-Legged Side Hop : '), 17, 3)
        self.grid.addWidget(QLabel('Two-Legged Side Hop : '), 18, 3)
        self.grid.addWidget(QLabel('Total Point Score Subtest 6 (max=52) : '), 23, 3)

        self.grid.addWidget(QLabel('Raw Score'), 13, 4)

        self.grid.addWidget(QLabel('Point Score'), 13, 5)

        for i in range(5):
            self.grid.addWidget(self.raw_arr_6[i], i+14, 4)

        # Subtest 7: Upper-Limb Coordination layout
        self.grid.addWidget(QLabel('Subtest 7: Upper-Limb Coordination'), 13, 6)
        self.grid.addWidget(QLabel('Dropping and Catching a Ball -- Both Hands : '), 14, 6)
        self.grid.addWidget(QLabel('Catching a Tossed Ball -- Both Hands : '), 15, 6)
        self.grid.addWidget(QLabel('Dropping and Catching a Ball --One Hands : '), 16, 6)
        self.grid.addWidget(QLabel('Catching a Tossed Ball --One Hands : '), 17, 6)
        self.grid.addWidget(QLabel('Dribbling a Ball -- One Hand : '), 18, 6)
        self.grid.addWidget(QLabel('Dribbling a Ball -- Alternating Hands : '), 19, 6)
        self.grid.addWidget(QLabel('Throwing a Ball at a Target : '), 20, 6)
        self.grid.addWidget(QLabel('Total Point Score Subtest 7 (max=39) : '), 23, 6)

        self.grid.addWidget(QLabel('Raw Score'), 13, 7)

        self.grid.addWidget(QLabel('Point Score'), 13, 8)

        for i in range(7):
            self.grid.addWidget(self.raw_arr_7[i], i+14, 7)

        # Subtest 8: Strength layout
        self.grid.addWidget(QLabel('Subtest 8: Strength'), 13, 9)
        self.grid.addWidget(QLabel('Standing Long Jump : '), 14, 9)
        self.grid.addWidget(QLabel('(a)Knee Push-ups OR (b)Full Push-ups : '), 15, 9)
        self.grid.addWidget(QLabel('Sit-ups : '), 16, 9)
        self.grid.addWidget(QLabel('Wall Sit : '), 17, 9)
        self.grid.addWidget(QLabel('V-up : '), 18, 9)
        self.grid.addWidget(QLabel('Total Point Score Subtest 8 (max=42) : '), 23, 9)

        self.grid.addWidget(QLabel('Raw Score'), 13, 10)

        self.grid.addWidget(QLabel('Point Score'), 13, 11)

        for i in range(5):
            self.grid.addWidget(self.raw_arr_8[i], i+14, 10)

        for i in range(8):
            if i < 4:
                self.grid.addWidget(self.raw_conv_btn_arr[i], 11, 1+i*3)
            else:
                self.grid.addWidget(self.raw_conv_btn_arr[i], 23, 1+(i-4)*3)

        self.setWindowTitle('Score Conversion Program')
        self.setGeometry(300, 300, 300, 200)
        self.setLayout(self.grid)
        self.show()

    def make_grid(self):
        for i in range(8):
            self.grid.addWidget(QLabel(str(self.point_arr_1[i])), i+1, 2)
        

    def validation(self):
        special_char = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '<', '.', '>', '/', '?', '[', ']', '{', '}', '-']
        err = False
        for i in range(7):
            if self.raw_arr_1[i].text() == "" or re.findall('[a-zA-Zㄱ-힣]', self.raw_arr_1[i].text()) or any(c in special_char for c in self.raw_arr_1[i].text()):
                print(self.raw_arr_1[0].text())
                err = True
                break

        if err == True:
            QMessageBox.warning(self, "Error", "Please check it out again.")
        else:
            self.change_point_score()

    def change_point_score(self):
        self.point_arr_1 = []
        total_point_score = 0

        # Subtest 1: Find Motor Precision
            # Filing in Shapes
        for i in range(0, 2):
            if int(self.raw_arr_1[i].text()) == 0:
                self.point_arr_1.append(0)
            elif int(self.raw_arr_1[i].text()) == 1:
                self.point_arr_1.append(1)
            elif int(self.raw_arr_1[i].text()) == 2:
                self.point_arr_1.append(2)
            elif int(self.raw_arr_1[i].text()) == 3:
                self.point_arr_1.append(3)
            else:
                QMessageBox.warning(self, "Error", "Please check it out again.")
            total_point_score += self.point_arr_1[i]

            # Drawing Lines Through Paths
        for i in range(2, 4):
            if int(self.raw_arr_1[i].text()) == 0:
                self.point_arr_1.append(7)
            elif int(self.raw_arr_1[i].text()) == 1:
                self.point_arr_1.append(6)
            elif int(self.raw_arr_1[i].text()) <= 3:
                self.point_arr_1.append(5)
            elif int(self.raw_arr_1[i].text()) <= 5:
                self.point_arr_1.append(4)
            elif int(self.raw_arr_1[i].text()) <= 9:
                self.point_arr_1.append(3)
            elif int(self.raw_arr_1[i].text()) <= 14:
                self.point_arr_1.append(2)
            elif int(self.raw_arr_1[i].text()) <= 20:
                self.point_arr_1.append(1)
            else:
                self.point_arr_1.append(0)
            
            total_point_score += self.point_arr_1[i]

            # Connect Dots, Folding Paper, Cutting Out a Circle
        for i in range(4, 7):
            if int(self.raw_arr_1[i].text()) == 0:
                self.point_arr_1.append(0)
            elif int(self.raw_arr_1[i].text()) <= 2:
                self.point_arr_1.append(1)
            elif int(self.raw_arr_1[i].text()) <= 4:
                self.point_arr_1.append(2)
            elif int(self.raw_arr_1[i].text()) <= 6:
                self.point_arr_1.append(3)
            elif int(self.raw_arr_1[i].text()) <= 8:
                self.point_arr_1.append(4)
            elif int(self.raw_arr_1[i].text()) <= 10:
                self.point_arr_1.append(5)
            elif int(self.raw_arr_1[i].text()) == 11:
                self.point_arr_1.append(6)
            elif int(self.raw_arr_1[i].text()) == 12:
                self.point_arr_1.append(7)
            # 12보다 높은 값을 받을 경우????

            total_point_score += self.point_arr_1[i]
        
        self.point_arr_1.append(total_point_score)

        print(self.point_arr_1, total_point_score)

        self.make_grid()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Conversion()
    sys.exit(app.exec_())


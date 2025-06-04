import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QGraphicsEffect, \
    QGraphicsColorizeEffect
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Calculator")
        self.setGeometry(205, 150, 370, 350)
        self.UiComponents()
        self.show()

    # Here is the implementation of the GUI components function
    # That is used fo creating label elements ant styling them

    def UiComponents(self):
        self.label = QLabel(self)

        self.label.setGeometry(10, 5, 350, 70) # set geometry of the label
        self.label.setWordWrap(True)

        self.label.setStyleSheet("QLabel {border: 50px solidBlack;"
                                 "background: white; color: green}")

        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 14))

        # Creation of all numeric push buttons form 0 to 9 and set their shape and size

        # creating button 1
        push01 = QPushButton("1", self)
        # set geometry for button 1
        push01.setGeometry(10, 150, 80, 40)

        # in the same way we create the rest of number buttons
        push02 = QPushButton("2", self)
        push02.setGeometry(100, 150, 80, 40)

        push03 = QPushButton("3", self)
        push03.setGeometry(190, 150, 80, 40)

        push04 = QPushButton("4", self)
        push04.setGeometry(10, 200, 80, 40)

        push05 = QPushButton("5", self)
        push05.setGeometry(100, 200, 80, 40)

        push06 = QPushButton("6", self)
        push06.setGeometry(190, 200, 80, 40)

        push07 = QPushButton("7", self)
        push07.setGeometry(10, 250, 80, 40)

        push08 = QPushButton("8", self)
        push08.setGeometry(100, 250, 80, 40)

        push09 = QPushButton("9", self)
        push09.setGeometry(190, 250, 80, 40)

        push00 = QPushButton("0", self)
        push00.setGeometry(10, 300, 80, 40)

        push_equalsTo = QPushButton("=", self)
        push_equalsTo.setGeometry(190, 300, 80, 40)
        clr_effect = QGraphicsColorizeEffect()
        clr_effect.setColor(Qt.blue)
        push_equalsTo.setGraphicsEffect(clr_effect)

        push_addition = QPushButton("+", self)
        push_addition.setGeometry(280, 300, 80, 40)

        push_subtract = QPushButton("-", self)
        push_subtract.setGeometry(280, 250, 80, 40)

        push_multiply = QPushButton("*", self)
        push_multiply.setGeometry(280, 200, 80, 40)

        push_division = QPushButton("/", self)
        push_division.setGeometry(280, 150, 80, 40)

        push_point = QPushButton(".", self)
        push_point.setGeometry(100, 300, 80, 40)

        push_clr = QPushButton("Clr", self)
        push_clr.setGeometry(10, 100, 200, 40)

        push_del = QPushButton("Del", self)
        push_del.setGeometry(215, 100, 145, 40)

        # Adding respecting actions for all created buttons

        push_subtract.clicked.connect(self.action_subtract)
        push_addition.clicked.connect(self.action_addition)
        push_multiply.clicked.connect(self.action_multiply)
        push_division.clicked.connect(self.action_division)
        push_equalsTo.clicked.connect(self.action_equalsTo)
        push_point.clicked.connect(self.action_point)
        push_clr.clicked.connect(self.action_clr)
        push_del.clicked.connect(self.action_del)
        push00.clicked.connect(self.action00)
        push01.clicked.connect(self.action01)
        push02.clicked.connect(self.action02)
        push03.clicked.connect(self.action03)
        push04.clicked.connect(self.action04)
        push05.clicked.connect(self.action05)
        push06.clicked.connect(self.action06)
        push07.clicked.connect(self.action07)
        push08.clicked.connect(self.action08)
        push09.clicked.connect(self.action09)

    def action_equalsTo(self):
        equation = self.label.text()

        try:
            # evaluating the solution
            sol = eval(equation)
            self.label.setText(str(sol))

        except:
            self.label.setText("Wrong input")

    def action_addition(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_subtract(self):
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_multiply(self):
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_division(self):
        text = self.label.text()
        self.label.setText(text + " / ")

    def action00(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def action01(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def action02(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def action03(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def action04(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def action05(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def action06(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def action07(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def action08(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def action09(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def action_point(self):
        text = self.label.text()
        self.label.setText(text + ".")

    def action_clr(self):
        self.label.setText("")

    def action_del(self):
        text = self.label.text()
        self.label.setText(text[:-1])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
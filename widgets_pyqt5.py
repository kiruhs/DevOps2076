from PyQt5.QtWidgets import * # QCheckBox
from PyQt5.QtGui import QPalette, QFont
from PyQt5.QtCore import Qt
import sys


# app = QApplication([])
# app.setStyle('Fusion') # Fusion Windows Macintosh
# palette = QPalette()
# palette.setColor(QPalette.Button, Qt.yellow)
# palette.setColor(QPalette.ButtonText, Qt.red)
# palette.setColor(QPalette.Text, Qt.green)
# app.setPalette(palette)
# app.setStyleSheet("QLabel {margin: auto; color: green; border: 3px}")
# # app.setStyleSheet("QPushButton {border: 8px;}" )
# window = QWidget()
# window.setWindowTitle("First app")
# window.resize(250, 150)
# window.move(600, 300)
# layout = QVBoxLayout()
# # label = QLabel("Hello World!")
# # label.show()
# button_top = QPushButton('Top')
# button_top.setToolTip("This will call to message box")
# layout.addWidget(button_top)
# button_bottom = QPushButton('Bottom')
# button_bottom.setToolTip("This will quit the application")
# layout.addWidget(QLabel('Hello world'))
# layout.addWidget(button_bottom)
# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText("The button clicked")
#     alert.exec_()
#
# button_top.clicked.connect(on_button_clicked)
# button_bottom.clicked.connect(sys.exit)
# window.setLayout(layout)
# window.show()
# app.exec_()

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Message box")
#
#         self.show()
#
#     def closeEvent(self, event):
#         reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
#                                      QMessageBox.Yes | QMessageBox.No)
#
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
#
# app = QApplication(sys.argv)
# exmp = Example()
# sys.exit(app.exec_())


# class Checkbox(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         cb = QCheckBox("&Show title", self)
#         cb.setShortcut("Alt+S")
#         cb.move(20,20)
#         cb.toggle()
#         cb.stateChanged.connect(self.changeTitle)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('QCheckBox')
#         self.show()
#
#     def changeTitle(self, state):
#         if state == Qt.Checked:
#             self.setWindowTitle('QCheckBox')
#         else:
#             self.setWindowTitle('')
#
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     check = Checkbox()
#     sys.exit(app.exec_())


class Slider(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        # self.label.setPixmap() - add icon
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300,300, 280,170)
        self.setWindowTitle('Slider')
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setText("Muted")
        elif value > 0 and value < 30:
            self.label.setText("Minimal")
        elif value > 30 and value < 80:
            self.label.setText("Average")
        else:
            self.label.setText("Maximal")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sl = Slider()
    sys.exit(app.exec_())
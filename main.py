from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QPushButton
import sys


class Kvadrat_tenglama(QWidget):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        self.setWindowTitle("KVADRAT TENGLAMA FINDER")
        self.resize(617, 607)
        self.setStyleSheet("background-color: rgb(98, 160, 234);")
        
        self.txt_1 = QLineEdit(self)
        self.txt_2 = QLineEdit(self)
        self.txt_3 = QLineEdit(self)
        self.lbl_1 = QLabel(self)
        self.lbl_2 = QLabel(self)
        self.lbl_3 = QLabel(self)
        self.clear = QPushButton(self)
        self.calculate = QPushButton(self)
        self.javob = QLabel(self)

        self.txt_1.setAlignment(Qt.AlignCenter)
        self.txt_2.setAlignment(Qt.AlignCenter)
        self.txt_3.setAlignment(Qt.AlignCenter)

        
        # SET GEOMETRY
        self.txt_1.setGeometry(110, 70, 441, 51)
        self.lbl_1.setGeometry(50, 70, 41, 51)
        self.txt_2.setGeometry(110, 150, 441, 51)
        self.txt_3.setGeometry(110, 230, 441, 51)
        self.lbl_2.setGeometry(50, 150, 41, 51)
        self.lbl_3.setGeometry(50, 230, 41, 51)
        self.calculate.setGeometry(310, 310, 241, 61)
        self.clear.setGeometry(50, 310, 241, 61)
        self.javob.setGeometry(50, 390, 500, 150)
        
        # SET STYLE 
        lbl_stl = "font: 24pt \"Roboto\";border-radius:10px 10px 5px 3px;background-color:lightblue;color:red;"
        text_stl = "color:white;border-radius:20px;border:2px solid red;font: 20pt \"Roboto\";background-color: qlineargradient(spread:pad, x1:0.486, y1:0.5625, x2:1, y2:1, stop:0 rgba(21, 70, 98, 255), stop:1 rgba(255, 255, 255, 255));"
        btn_stl = lambda x: f"color:#000;border:2px solid red;border-radius:20px;font: 24pt \"Roboto\";background-color: {x}"
        self.javob.setStyleSheet("padding:10px;font: 24pt \"Roboto\";color:#000;background-color: rgb(220, 138, 221);border-radius:25px;border:2px solid rgb(97, 53, 131)")
        self.lbl_1.setStyleSheet(lbl_stl)
        self.lbl_2.setStyleSheet(lbl_stl)
        self.lbl_3.setStyleSheet(lbl_stl)
        self.txt_1.setStyleSheet(text_stl)
        self.txt_2.setStyleSheet(text_stl)
        self.txt_3.setStyleSheet(text_stl)
        self.calculate.setStyleSheet(btn_stl("rgb(87, 227, 137)"))
        self.clear.setStyleSheet(btn_stl("rgb(246, 97, 81)"))


        self.lbl_1.setText("<center><b>A</b></center>")
        self.lbl_2.setText("<center><b>B</b></center>")
        self.lbl_3.setText("<center><b>C</b></center>")
        self.calculate.setText("CALCULATE")
        self.clear.setText("CLEAR")

        self.calculate.clicked.connect(self.calc)
        self.clear.clicked.connect(self.clean)

    def calc(self):
        try:
            A = int(self.txt_1.text())
            B = int(self.txt_2.text())
            C = int(self.txt_3.text())
            Diskriminant = B ** 2 - 4 * A * C
            X1 = 0
            X2 = 0
            if Diskriminant > 0:
                X1 = (-B + (Diskriminant ** 0.5)) / (2 * A)
                X2 = (-B - (Diskriminant ** 0.5)) / (2 * A)
                self.javob.setText(f"⚫️ Diskriminant = {Diskriminant} ✅ \n⚫️ X1 = {X1} ✅\n⚫️ X2 = {X2} ✅")
            elif Diskriminant == 0:
                X1 = (-B + (Diskriminant ** 0.5)) / (2 * A)
                X2 = (-B - (Diskriminant ** 0.5)) / (2 * A)
                self.javob.setText(f"⚫️ Diskriminant = {Diskriminant} ✅ \n⚫️ X1 = X2 = {X2} ✅")
            else:
                self.javob.setText(f"⚫️ Diskriminant = {Diskriminant} ❎\n⚫️ BO'SH TO'PLAM ❎")
        except:
            self.javob.setText(f"<span style='color:red;'>❌ TO'G'RI KIRITING !!!</span>")
    
    def clean(self):
        self.javob.setText("")
        self.txt_1.setText("")
        self.txt_2.setText("")
        self.txt_3.setText("")


app = QApplication(sys.argv)
Kvadrat_t = Kvadrat_tenglama()
Kvadrat_t.show()
sys.exit(app.exec_())

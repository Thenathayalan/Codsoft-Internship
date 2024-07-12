import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from labels import widgets

class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenCalc")
        self.setFixedSize(QSize(280,520))
        self.setStyleSheet("background-color: #000000")

        self.calc = ""

        Row1 = QHBoxLayout()
        Row2 = QHBoxLayout()
        Row3 = QHBoxLayout()
        Row4 = QHBoxLayout()
        Row5 = QHBoxLayout()
        disp = QHBoxLayout()

        Vertical = QVBoxLayout()

        self.his = widgets.history(self)

        self.Res = widgets.result(self)

        self.c_button = widgets.clear(self); Row1.addWidget(self.c_button)

        pm_button = widgets.plus(self); Row1.addWidget(pm_button)

        p_button = widgets.per(self); Row1.addWidget(p_button)

        d_button = widgets.div(self); Row1.addWidget(d_button)

        sev_button = widgets.sev(self); Row2.addWidget(sev_button)

        eig_button = widgets.eig(self); Row2.addWidget(eig_button)

        nin_button = widgets.nin(self); Row2.addWidget(nin_button)

        mul_button = widgets.mul(self); Row2.addWidget(mul_button)

        fou_button = widgets.fou(self); Row3.addWidget(fou_button)

        fiv_button = widgets.fiv(self); Row3.addWidget(fiv_button)

        six_button = widgets.six(self); Row3.addWidget(six_button)

        sub_button = widgets.sub(self); Row3.addWidget(sub_button)

        one_button = widgets.one(self); Row4.addWidget(one_button)

        two_button = widgets.two(self); Row4.addWidget(two_button)

        thr_button = widgets.thr(self); Row4.addWidget(thr_button)

        add_button = widgets.add(self); Row4.addWidget(add_button)

        zer_button = widgets.zer(self); Row5.addWidget(zer_button); Row5.addSpacing(5)

        dot_button = widgets.dot(self); Row5.addWidget(dot_button)

        eql_button = widgets.eql(self); Row5.addWidget(eql_button)

        disp.addSpacing(10)
        disp.addWidget(self.Res)
        disp.addSpacing(15)
        Vertical.addWidget(self.his)
        Vertical.addLayout(disp)
        Vertical.addLayout(Row1)
        Vertical.addLayout(Row2)
        Vertical.addLayout(Row3)
        Vertical.addLayout(Row4)
        Vertical.addLayout(Row5)

        widget = QWidget()
        widget.setLayout(Vertical)
        self.setCentralWidget(widget)

    def text_changed(self,txt):
        self.calc = txt

    def result(self):
        try:
            if self.calc != "":
                res = eval(self.calc)
                if res !=0:
                    self.Res.setText(str(res))
                    if str(res).endswith('.0'):
                        self.Res.setText(str(res)[:-2])
                else:
                    self.Res.setText("")

        except (SyntaxError,NameError):
            self.Res.setReadOnly(True)
            self.Res.setText("Input Err")
        except ZeroDivisionError:
            self.Res.setReadOnly(True)
            self.Res.setText("Math Err")
        self.Res.setFocus()

    def clear(self):
        self.calc = ""
        self.Res.setText("")
        self.Res.setReadOnly(False)
        self.Res.setFocus()

    def pm(self):
        try:
            self.result()
            txt = self.Res.text()
            txt = -(int(txt))
            self.Res.setText(str(txt))
            self.calc = str(txt)
        except ValueError:
            self.Res.setReadOnly(True)
            self.Res.setText("Value Err")
        self.Res.setFocus()

    def per(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "%" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def div(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "/" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def mul(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "*" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def sub(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "-" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def add(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "+" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def one(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "1" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def two(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "2" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def three(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "3" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def four(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "4" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def five(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "5" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def six(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "6" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def seven(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "7" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def eight(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "8" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def nine(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "9" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def zero(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "0" + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

    def dot(self):
        i = self.Res.cursorPosition()
        txt = self.Res.text()
        self.calc = txt[:i] + "." + txt[i:]
        self.Res.setText(self.calc)
        self.Res.setFocus()

app = QApplication(sys.argv)
window = Main_window()
window.show()
app.exec()

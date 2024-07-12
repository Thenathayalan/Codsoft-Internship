from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

class widgets:

    def history(self):
        label = QLabel()
        label.setFixedHeight(60)
        return label

    def result(self):
        res = QLineEdit()
        res.setAlignment(Qt.AlignRight)
        res.setPlaceholderText("0")
        res.setStyleSheet("background-color:#000000; color:white; font-size:52px; border:0px solid #000000;")
        res.textEdited.connect(self.text_changed)
        res.returnPressed.connect(self.result)
        return res

    def clear(self):
        c = QPushButton("C")
        c.setFixedSize(QSize(60,60))
        c.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #d4d4d2; background-color:#d4d4d2; color:#505050")
        c.clicked.connect(self.clear)
        return c

    def plus(self):
        pm = QPushButton("+/-")
        pm.setFixedSize(QSize(60,60))
        pm.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #d4d4d2; background-color:#d4d4d2; color:#505050")
        pm.clicked.connect(self.pm)
        return pm

    def per(self):
        p = QPushButton("%")
        p.setFixedSize(QSize(60,60))
        p.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #d4d4d2; background-color:#d4d4d2; color:#505050")
        p.clicked.connect(self.per)
        return p

    def div(self):
        d = QPushButton("÷")
        d.setFixedSize(QSize(60,60))
        d.setStyleSheet("font-size: 34px; border-radius:30px; border:2px solid #ff9500; background-color:#ff9500; color:#FFFFFF")
        d.clicked.connect(self.div)
        return d

    def sev(self):
        sev = QPushButton("7")
        sev.setFixedSize(QSize(60,60))
        sev.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        sev.clicked.connect(self.seven)
        return sev

    def eig(self):
        eig = QPushButton("8")
        eig.setFixedSize(QSize(60,60))
        eig.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        eig.clicked.connect(self.eight)
        return eig

    def nin(self):
        nin = QPushButton("9")
        nin.setFixedSize(QSize(60,60))
        nin.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        nin.clicked.connect(self.nine)
        return nin

    def mul(self):
        mul = QPushButton("×")
        mul.setFixedSize(QSize(60,60))
        mul.setStyleSheet("font-size: 34px; border-radius:30px; border:2px solid #ff9500; background-color:#ff9500; color:#FFFFFF")
        mul.clicked.connect(self.mul)
        return mul

    def fou(self):
        fou = QPushButton("4")
        fou.setFixedSize(QSize(60,60))
        fou.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        fou.clicked.connect(self.four)
        return fou

    def fiv(self):
        fiv = QPushButton("5")
        fiv.setFixedSize(QSize(60,60))
        fiv.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        fiv.clicked.connect(self.five)
        return fiv

    def six(self):
        six = QPushButton("6")
        six.setFixedSize(QSize(60,60))
        six.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        six.clicked.connect(self.six)
        return six

    def sub(self):
        sub = QPushButton("−")
        sub.setFixedSize(QSize(60,60))
        sub.setStyleSheet("font-size: 34px; border-radius:30px; border:2px solid #ff9500; background-color:#ff9500; color:#FFFFFF")
        sub.clicked.connect(self.sub)
        return sub

    def one(self):
        one = QPushButton("1")
        one.setFixedSize(QSize(60,60))
        one.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        one.clicked.connect(self.one)
        return one

    def two(self):
        two = QPushButton("2")
        two.setFixedSize(QSize(60,60))
        two.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        two.clicked.connect(self.two)
        return two

    def thr(self):
        thr = QPushButton("3")
        thr.setFixedSize(QSize(60,60))
        thr.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        thr.clicked.connect(self.three)
        return thr

    def add(self):
        add = QPushButton("+")
        add.setFixedSize(QSize(60,60))
        add.setStyleSheet("font-size: 34px; border-radius:30px; border:2px solid #ff9500; background-color:#ff9500; color:#FFFFFF")
        add.clicked.connect(self.add)
        return add

    def zer(self):
        zer = QPushButton("     0")
        zer.setFixedSize(QSize(125,60))
        zer.setStyleSheet("text-align:left; font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        zer.clicked.connect(self.zero)
        return zer

    def dot(self):
        dot = QPushButton(".")
        dot.setFixedSize(QSize(60,60))
        dot.setStyleSheet("font-size: 20px; border-radius:30px; border:2px solid #202020; background-color:#202020; color:#FFFFFF")
        dot.clicked.connect(self.dot)
        return dot

    def eql(self):
        eql = QPushButton("=")
        eql.setFixedSize(QSize(60,60))
        eql.setStyleSheet("font-size: 32px; border-radius:30px; border:2px solid #ff9500; background-color:#ff9500; color:#FFFFFF")
        eql.clicked.connect(self.result)
        return eql

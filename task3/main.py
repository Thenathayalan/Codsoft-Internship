from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QButtonGroup, QLabel, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout,QPushButton, QWidget, QCheckBox, QSpacerItem, QSizePolicy, QLineEdit
import sys
import random
import string

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password_Generator")
        self.setFixedSize(QSize(300, 500))
        self.setStyleSheet("background-color: black; color: white")

        self.main_layout = QVBoxLayout()
        checkbox = QHBoxLayout()
        button1 = QHBoxLayout()
        button2 = QHBoxLayout()

        self.easy = QCheckBox(text="Easy")
        self.medium = QCheckBox(text="Medium")
        self.hard = QCheckBox(text="Hard")

        checkbox.addWidget(self.easy)
        checkbox.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        checkbox.addWidget(self.medium)
        checkbox.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        checkbox.addWidget(self.hard)

        generate = QPushButton("Generate Password")
        generate.setFixedSize(QSize(250,30))
        generate.setStyleSheet("""
            QPushButton {
                border: 1px solid gray; 
                border-radius: 15px;
            }
            QPushButton:hover {
                border-color: cyan;
            }
            QPushButton:pressed {
                background-color: #11171e;
            }
        """)

        copy = QPushButton("Copy to Clipboard")
        copy.setFixedSize(QSize(250,30))
        copy.setStyleSheet("""
            QPushButton {
                border: 1px solid gray; 
                border-radius: 15px;
            }
            QPushButton:hover {
                border-color: cyan;
            }
            QPushButton:pressed {
                background-color: #11171e;
            }
        """)

        button1.addWidget(generate)
        button2.addWidget(copy)

        self.length = QLineEdit()
        self.length.setPlaceholderText("Enter Password_Length")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Click Generate Button")

        len = QLabel("Password Length")
        len.setFixedHeight(20)
        text1 = QLabel("Password Strength")
        text1.setFixedHeight(20)
        text2 = QLabel("Your New Password")
        text2.setFixedHeight(20)
        self.cp = QLabel()
        self.cp.setFixedHeight(15)

        self.main_layout.addWidget(len)
        self.main_layout.addWidget(self.length)
        self.main_layout.addWidget(text1)
        self.main_layout.addLayout(checkbox)
        self.main_layout.addLayout(button1)
        self.main_layout.addWidget(text2)
        self.main_layout.addWidget(self.password)
        self.main_layout.addLayout(button2)
        self.main_layout.addWidget(self.cp)

        checkbox_group = QButtonGroup(self)
        checkbox_group.addButton(self.easy)
        checkbox_group.addButton(self.medium)
        checkbox_group.addButton(self.hard)
        
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

        generate.clicked.connect(self.generate_password)
        copy.clicked.connect(self.copy_to_clipboard)

    def generate_password(self):
        self.cp.setText("")
        length_value = self.length.text()
        if self.easy.isChecked():
            strength = 'easy'
        elif self.medium.isChecked():
            strength = 'medium'
        elif self.hard.isChecked():
            strength = 'hard'
        else:
            strength = 'medium'

        generated_password = self.generate_password_with_strength(int(length_value), strength)
        self.password.setText(generated_password)

    def generate_password_with_strength(self, length, strength):
        if strength == 'easy':
            characters = string.ascii_lowercase
        elif strength == 'medium':
            characters = string.ascii_letters + string.digits
        elif strength == 'hard':
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            raise ValueError("Strength must be 'easy', 'medium', or 'hard'")

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def copy_to_clipboard(self):
        password_text = self.password.text()
        if password_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(password_text)
            self.cp.setText("Copied to clipboard")
        else:
            self.cp.setText("Nothing to copy")

app = QApplication(sys.argv)
window = Main_Window()
window.show()
app.exec()

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QListWidget,
    QMessageBox,
    QWidget
)
import sys
import os

class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do List")
        self.setMinimumSize(QSize(700, 500))
        self.setStyleSheet("background-color: #2f3e46;")

        self.task = ""
        self.selected_task = ""
        self.mem = []
        self.load_tasks()

        layoutV = QVBoxLayout()

        self.text_area = QListWidget()
        self.text_area.setStyleSheet("font: 12pt; border:4px solid; border-radius:12px; background-color: #52796f")
        self.text_area.addItems(self.mem)
        self.text_area.itemClicked.connect(self.Selected_task)
        layoutV.addWidget(self.text_area)
        layoutV.addSpacing(5)

        # Layout for text field and clear button
        layoutH2 = QHBoxLayout()

        self.text_field = QLineEdit()
        self.text_field.setPlaceholderText("Enter New Task or Select Task to Delete")
        self.text_field.setAlignment(Qt.AlignCenter)
        self.text_field.setStyleSheet("border:2px solid #cad2c5; border-radius:10px;")
        self.text_field.textEdited.connect(self.text_edited)
        layoutH2.addWidget(self.text_field)
        layoutH2.addSpacing(10)

        self.clear = QPushButton("Clear")
        self.clear.setFixedWidth(70)
        self.clear.setStyleSheet("border:2px solid #84a98c; color:#000000; border-radius:10px; background-color: #84a98c")
        self.clear.clicked.connect(self.clear_click)
        layoutH2.addWidget(self.clear)

        bottom_label = QLabel()
        bottom_label.setStyleSheet("border:4px solid; border-radius:12px; background-color: #354f52")
        bottom_label.setFixedHeight(100)

        label_layout = QVBoxLayout()

        # Add the horizontal layout with text field and clear button
        label_layout.addLayout(layoutH2)

        # Layout for the add, delete, and help buttons
        layoutH1 = QHBoxLayout()

        layoutH1.addSpacing(20)
        add = QPushButton("Add")
        add.setStyleSheet("border:2px solid #84a98c; color:#000000; border-radius:10px; background-color: #84a98c")
        add.clicked.connect(self.add_click)
        layoutH1.addWidget(add)
        layoutH1.addSpacing(20)

        delete = QPushButton("Delete")
        delete.setStyleSheet("border:2px solid #84a98c; color:#000000; border-radius:10px; background-color: #84a98c")
        delete.clicked.connect(self.del_click)
        layoutH1.addWidget(delete)
        layoutH1.addSpacing(20)

        Help = QPushButton("About")
        Help.setStyleSheet("border:2px solid #84a98c; color:#000000; border-radius:10px; background-color: #84a98c")
        Help.clicked.connect(self.help_click)
        layoutH1.addWidget(Help)
        layoutH1.addSpacing(20)

        label_layout.addLayout(layoutH1)

        bottom_label.setLayout(label_layout)

        layoutV.addWidget(bottom_label)

        widget = QWidget()
        widget.setLayout(layoutV)
        self.setCentralWidget(widget)

    def add_click(self):
        if self.task != "":
            self.text_area.addItem(self.task)
            self.mem.append(self.task)
            self.save_tasks()
        self.text_field.clear()

    def del_click(self):
        if self.selected_task:
            row = self.text_area.row(self.selected_task)
            self.text_area.takeItem(row)
            self.mem.remove(self.selected_task.text())
            self.save_tasks()
            self.selected_task = None
            self.text_area.clearSelection()
        self.text_field.clear()

    def help_click(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("About")
        dlg.setText("This is a simple To do list app \n Give it a try !!!")
        button = dlg.exec()

    def clear_click(self):
        self.text_field.clear()
        self.text_area.clearSelection()

    def text_edited(self, s):
        self.task = s

    def Selected_task(self, t):
        self.selected_task = t
        self.text_field.setText(self.selected_task.text())

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.mem:
                file.write(task + "\n")

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.mem = [line.strip() for line in file]

app = QApplication(sys.argv)
window = Main_window()
window.show()
app.exec()

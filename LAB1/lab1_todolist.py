import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QGridLayout,
                             QButtonGroup, QHBoxLayout,QVBoxLayout)


class ToDoList(QWidget):
    def __init__(self):  # Constructor
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 500, 350)
        self.setWindowTitle('Lab1-2 ToDo List GUI')
        self.setupWidgets()
        self.show()

    def setupWidgets(self):
        main_grid = QGridLayout()
        todo_title = QLabel("To Do List")
        todo_title.setFont(QFont('Arial', 24))
        todo_title.setAlignment(Qt.AlignCenter)
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        # Create section labels for to-do list
        

        # Create must-do section
        subtitle1=QLabel("Must Dos")
        subtitle1.setFont(QFont('Arial', 20))

        # Create checkboxes and line edit widgets
        v1_box=QVBoxLayout()
        v1_box.addWidget(subtitle1)
        for i in range(15):
            h_temp=QHBoxLayout()
            self.check = QCheckBox(self)
            self.todo = QLineEdit(self)
            self.todo.resize(100,20)
            h_temp.addWidget(self.check)
            h_temp.addWidget(self.todo)
            v1_box.addLayout(h_temp)

        # Create labels for appointments section
        subtitle2=QLabel("Appointments")
        subtitle2.setFont(QFont('Arial', 20))
        periods=["Morning","Noon","Evening"]

        # Create vertical layout and add widgets
        v2_box=QVBoxLayout()
        v2_box.addWidget(subtitle2)
        for period in periods:
            period_label=QLabel(period,self)
            period_label.setFont(QFont('Arial', 17))
            v2_box.addWidget(period_label)
            self.things = QTextEdit(self)
            self.things.resize(100,20)
            v2_box.addWidget(self.things)

        v2_box.setContentsMargins(5,5,5,5)

        # Add other layouts to main layout
        h_box=QHBoxLayout()
        h_box.addLayout(v1_box)
        h_box.addLayout(v2_box)

        v_box = QVBoxLayout()
        v_box.addWidget(todo_title)
        v_box.addLayout(h_box);
        v_box.addWidget(close_button)
        self.setLayout(v_box)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoList()
    sys.exit(app.exec_())

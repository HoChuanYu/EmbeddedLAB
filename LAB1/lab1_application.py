import sys

from PyQt5.QtCore import QLine, Qt, qVersion
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QFormLayout, QLineEdit, QTextEdit, QSpinBox,
                             QComboBox, QCheckBox, QGridLayout,QButtonGroup, QHBoxLayout,QVBoxLayout)
#from PyQt5.sip import array


class GetApptForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Lab 1-3 Application Form GUI')
        self.formWidgets()
        self.show()

    def formWidgets(self):
        """
        Create widgets that will be used in the application form.
        """
        # Create widgets
        v_box=QVBoxLayout()
        title=QLabel("Appointment Submission Form")
        title.setFont(QFont('Arial', 24))
        title.setAlignment(Qt.AlignCenter)

        h1_box=QHBoxLayout()
        v1_box=QVBoxLayout()
        v2_box=QVBoxLayout()
        arr=["Full Name","Address","Mobile Number"]
        for element in arr:
            label=QLabel(element,self)
            v1_box.addWidget(label)
        for i in range(3):
            self.entry=QLineEdit(self)
            self.entry.resize(100,20)
            if i==2:
                self.entry.setInputMask("0000-000000;")
            v2_box.addWidget(self.entry)
        h1_box.addLayout(v1_box)
        h1_box.addLayout(v2_box)            

        # Create horizontal layout and add age, height, and weight to h_box
        h2_box=QHBoxLayout()
        age=QLabel("Age")
        height=QLabel("Height")
        weight=QLabel("Weight")
        h2_box.addWidget(age)
        age_entry=QSpinBox(self)
        age_entry.setMinimum(1)
        age_entry.setMaximum(99)
        h2_box.addWidget(age_entry)
        self.height_entry=QLineEdit(self)
        self.weight_entry=QLineEdit(self)
        self.height_entry.setPlaceholderText("cm")
        self.weight_entry.setPlaceholderText("kg")
        h2_box.addWidget(height)
        h2_box.addWidget(self.height_entry)
        h2_box.addWidget(weight)
        h2_box.addWidget(self.weight_entry)
        
        # Create horizontal layout and add time information
        h3_box=QHBoxLayout()
        v3_box=QVBoxLayout()
        v4_box=QVBoxLayout()
        


        # Create form layout
        
        # Add all widgets to form layout
        submit_button = QPushButton("Submit Appointment")
        submit_button.clicked.connect(self.close)

        v_box.addWidget(title)
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addWidget(submit_button)
        self.setLayout(v_box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GetApptForm()
    sys.exit(app.exec_())

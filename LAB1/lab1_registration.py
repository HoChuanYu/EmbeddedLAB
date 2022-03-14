import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QCheckBox, QButtonGroup, QHBoxLayout,
                             QVBoxLayout,QPushButton,QLineEdit)


class CreateNewUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()  # Call our function used to set up window

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Lab1-1 Registration GUI')
        self.displayWidgetsToCollectInfo()
        self.show()

    def displayWidgetsToCollectInfo(self):
        """
        Create widgets that will be used to collect information
        from the user to create a new account.
        """
        # Create label for image
        title = QLabel(self)
        title.setText("Create New Account")
        title.setFont(QFont('Arial', 24))
        title.move(35,15)
        image = "image/grinning-cat.png"
        try:
            with open(image):
                emoji = QLabel(self)
                pixmap = QPixmap(image)
                emoji.setPixmap(pixmap)
                emoji.move(130, 65)
        except FileNotFoundError:
            print("Image not found.")
        # Username and fullname labels and line edit widgets
        username=QLabel(self)
        username.setText("Username:")
        username.move(35,200)
        fullname=QLabel(self)
        fullname.setText("Full name:")
        fullname.move(35,230)
        self.name = QLineEdit(self)
        self.name.resize(200,20)
        self.surname = QLineEdit(self)
        self.surname.resize(200,20)
        self.name.move(100,195)
        self.surname.move(100,225)
        # Create password and confirm password labels and line edit widgets
        password=QLabel(self)
        password.setText("Password:")
        confirm=QLabel(self);
        password.move(35,260)
        confirm.setText("Confirm:")
        confirm.move(35,290)
        self.password_entry = QLineEdit(self)
        self.password_entry.resize(200,20)
        self.confirm_entry = QLineEdit(self)
        self.confirm_entry.resize(200,20)
        self.password_entry.move(100,255)
        self.confirm_entry.move(100,285)
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.confirm_entry.setEchoMode(QLineEdit.Password)
        # Create sign up button
        sign_button = QPushButton("sign up", self)
        sign_button.resize(80,40)
        sign_button.move(150,330)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CreateNewUser()
    sys.exit(app.exec_())

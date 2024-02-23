# login_page.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from assets.styles import input_style, button_style
import json


class LoginPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget
        # Loading the logo image
        logo_image = QPixmap("assets/version2.png")
        layout = QVBoxLayout()

        # Creating a QLabel to display the logo
        logo_label = QLabel()
        logo_label.setPixmap(logo_image.scaledToWidth(200))  # Adjust the width as desired
        logo_label.setAlignment(Qt.AlignCenter)

        # Scaling the logo based on window size
        logo_label.setScaledContents(True)

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.login_button = QPushButton("Log In")
        self.signup_button = QPushButton("Sign Up")

        # Setting placeholder text for input boxes
        self.username_input.setPlaceholderText("Username")
        self.password_input.setPlaceholderText("Password")

        layout = QVBoxLayout()
        layout.addWidget(logo_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

        # Applying the styles
        self.username_input.setStyleSheet(input_style)
        self.password_input.setStyleSheet(input_style)
        self.login_button.setStyleSheet(button_style)
        self.signup_button.setStyleSheet(button_style)

        self.login_button.clicked.connect(self.login)
    
    def login(self):
        username_or_email = self.username_input.text().upper()
        password = self.password_input.text()

        with open('data/users.json', 'r') as f:
            users = json.load(f)

        for user in users:
            if (user['username'].upper() == username_or_email or user['email'].upper() == username_or_email) and user['password'] == password:
                self.stacked_widget.setCurrentIndex(1)  # assuming the notes page is at index 1
                break


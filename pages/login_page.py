from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QAction
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from assets.styles import button_style, login_button_style, login_input_style
from events.buttons.login_button_events import on_login_button_clicked
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
        logo_label.setPixmap(logo_image.scaledToWidth(600))  # Adjust the width as desired
        logo_label.setAlignment(Qt.AlignCenter)

        # Scaling the logo based on window size
        logo_label.setScaledContents(True)

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(lambda: on_login_button_clicked(self))
        self.login_button.setMaximumWidth(200)
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setMaximumWidth(200)

        # Setting placeholder text for input boxes
        self.username_input.setPlaceholderText("Username")
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        # Adding toggle action to password input field
        self.toggle_password_visibility_action = QAction(self)
        self.toggle_password_visibility_action.triggered.connect(self.toggle_password_visibility)
        self.password_input.addAction(self.toggle_password_visibility_action, QLineEdit.TrailingPosition)
        
        # Set icon for the visibility toggle action
        self.toggle_password_visibility_action.setIcon(QIcon('assets/eye_icon_3989747'))  

        layout = QVBoxLayout()
        layout.addWidget(logo_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.signup_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

        # Applying the styles
        self.username_input.setStyleSheet(login_input_style)
        self.password_input.setStyleSheet(login_input_style)
        self.login_button.setStyleSheet(login_button_style)
        self.signup_button.setStyleSheet(button_style)

    def toggle_password_visibility(self):
        if self.password_input.echoMode() == QLineEdit.Password:
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.toggle_password_visibility_action.setIcon(QIcon('assets/toggle_password_visibility_ON'))  # Change icon
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.toggle_password_visibility_action.setIcon(QIcon('assets/eye_icon_3989747'))  # Change icon

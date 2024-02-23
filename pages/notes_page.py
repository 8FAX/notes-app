# notes_page.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton
from events.buttons.save_button_events import save_button_clicked
from assets.styles import input_style, button_style

class NotesPage(QWidget):
    def __init__(self):
        super().__init__()

        self.file_name_input = QLineEdit()
        self.tags_input = QLineEdit()
        self.text_area = QTextEdit()
        self.save_button = QPushButton("Save")

        # Setting placeholder text for input boxes
        self.file_name_input.setPlaceholderText("Enter file name (without extension)")
        self.tags_input.setPlaceholderText("Enter tags separated by commas")
        self.text_area.setPlaceholderText("Start jotting down your thoughts, ideas, and dreams here! Let your creativity flow...")

        # Connecting the save button click event to the save_button_clicked function
        self.save_button.clicked.connect(lambda: save_button_clicked(self.file_name_input, self.tags_input, self.text_area))

        layout = QVBoxLayout()
        layout.addWidget(self.file_name_input)
        layout.addWidget(self.text_area)
        layout.addWidget(self.tags_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        # Applying the styles
        self.file_name_input.setStyleSheet(input_style)
        self.tags_input.setStyleSheet(input_style)
        self.text_area.setStyleSheet(input_style)
        self.save_button.setStyleSheet(button_style)
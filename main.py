import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from styles import input_style, button_style, main_app_style
from datetime import datetime
import json

class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notes App")

        self.text_area = QTextEdit()
        self.save_button = QPushButton("Save")
        self.file_name_input = QLineEdit()
        self.tags_input = QLineEdit()

        # Setting placeholder text for input boxes
        self.file_name_input.setPlaceholderText("Enter file name (without extension)")
        self.tags_input.setPlaceholderText("Enter tags separated by commas")
        self.text_area.setPlaceholderText("Start jotting down your thoughts, ideas, and dreams here! Let your creativity flow...")


        self.save_button.clicked.connect(self.save_notes)

        layout = QVBoxLayout()
        layout.addWidget(self.file_name_input)
        layout.addWidget(self.text_area)
        layout.addWidget(self.tags_input)
        layout.addWidget(self.save_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet(main_app_style)
        self.file_name_input.setStyleSheet(input_style)
        self.tags_input.setStyleSheet(input_style)
        self.save_button.setStyleSheet(button_style)

    def save_notes(self):
        file_name = self.file_name_input.text()
        if file_name:
            tags = [tag.strip() for tag in self.tags_input.text().split(",")]
            notes = {
                "created_at": str(datetime.now()), 
                "content": self.text_area.toPlainText(),
                "tags": tags
            }
            with open(file_name + ".json", "w") as f:
                json.dump(notes, f, indent=4)
            QMessageBox.information(self, "Notes App", "Notes saved successfully!")
        else:
            QMessageBox.warning(self, "Notes App", "Please enter a file name.")

def main():
    app = QApplication(sys.argv)
    window = NotesApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

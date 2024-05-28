from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QToolBar, QComboBox, QAction, QColorDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
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

        # Create the toolbar
        self.toolbar = QToolBar()

        # Bold action
        bold_action = QAction(QIcon(None), "Bold", self)
        bold_action.triggered.connect(self.toggle_bold)
        self.toolbar.addAction(bold_action)

        # Italic action
        italic_action = QAction(QIcon(None), "Italic", self)
        italic_action.triggered.connect(self.toggle_italic)
        self.toolbar.addAction(italic_action)

        # Underline action
        underline_action = QAction(QIcon(None), "Underline", self)
        underline_action.triggered.connect(self.toggle_underline)
        self.toolbar.addAction(underline_action)

        # Font size combobox
        self.font_size_combobox = QComboBox()
        self.font_size_combobox.addItems([str(size) for size in range(8, 31)])
        self.font_size_combobox.currentIndexChanged.connect(self.set_font_size)
        self.toolbar.addWidget(self.font_size_combobox)

        # Font color action
        font_color_action = QAction(QIcon(None), "Font Color", self)
        font_color_action.triggered.connect(self.change_font_color)
        self.toolbar.addAction(font_color_action)

        layout = QVBoxLayout()
        layout.addWidget(self.file_name_input)
        layout.addWidget(self.toolbar)  # Add the toolbar here
        layout.addWidget(self.text_area)
        layout.addWidget(self.tags_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        # Applying the styles
        self.file_name_input.setStyleSheet(input_style)
        self.tags_input.setStyleSheet(input_style)
        self.text_area.setStyleSheet(input_style)
        self.save_button.setStyleSheet(button_style)
        self.text_area.setAcceptRichText(True)

    def toggle_bold(self):
        fmt = self.text_area.currentCharFormat()
        fmt.setFontWeight(QFont.Bold if not fmt.fontWeight() == QFont.Bold else QFont.Normal)
        self.text_area.setCurrentCharFormat(fmt)

    def toggle_italic(self):
        fmt = self.text_area.currentCharFormat()
        fmt.setFontItalic(not fmt.fontItalic())
        self.text_area.setCurrentCharFormat(fmt)

    def toggle_underline(self):
        fmt = self.text_area.currentCharFormat()
        fmt.setFontUnderline(not fmt.fontUnderline())
        self.text_area.setCurrentCharFormat(fmt)

    def set_font_size(self, index):
        size = int(self.font_size_combobox.currentText())
        fmt = self.text_area.currentCharFormat()
        fmt.setFontPointSize(size)
        self.text_area.setCurrentCharFormat(fmt)

    def change_font_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            fmt = self.text_area.currentCharFormat()
            fmt.setForeground(color)
            self.text_area.setCurrentCharFormat(fmt)

import datetime
import json
import os
from PyQt5.QtWidgets import QMessageBox

def sanitize_filename(filename):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '')
    filename = os.path.basename(filename)
    return filename

def save_button_clicked(file_name_input, tags_input, text_area):
    file_name = sanitize_filename(file_name_input.text())
    
    if not file_name:
        QMessageBox.warning(None, "Invalid File Name", "The file name cannot be empty or contain only invalid characters.")
        return

    tags = [tag.strip() for tag in tags_input.text().split(",")]
    text = text_area.toHtml()  # Use toHtml() to get the rich text content

    note = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "os": os.name,  
        "tags": tags,
        "text": text
    }

    try:
        with open(file_name + ".json", "w", encoding="utf-8") as f:
            json.dump(note, f, ensure_ascii=False, indent=4)
        QMessageBox.information(None, "Success", f"Note saved as {file_name}.json")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Failed to save note: {e}")

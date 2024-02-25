import datetime
import json
import os


def sanitize_filename(filename):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '')
    filename = os.path.basename(filename)
    return filename

def save_button_clicked(file_name_input, tags_input, text_area):
    file_name = sanitize_filename(file_name_input.text())
    tags = tags_input.text().split(", ")
    text = text_area.toPlainText()

    note = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "os": os.name,  
        "tags": tags,
        "text": text
    }

    with open(file_name + ".json", "w") as f:
        json.dump(note, f)

# PyQt5 Note-Taking App

This is a simple note-taking app built with PyQt5. It allows users to jot down their thoughts, ideas, and dreams, and save them for later reference.

## Features

- **Note-Taking**: Users can write their notes in a text area. The notes can be as long or as short as they want.

- **Tagging**: Users can add tags to their notes. Tags are separated by commas and can be used to categorize and easily find notes later.

- **Saving Notes**: Users can save their notes by entering a file name and clicking the "Save" button. The notes are saved in JSON format, with the current date and time, the content of the notes, and the list of tags.

## Structure

The application is structured into separate pages, each in its own file:

- `notes_page.py`: This file contains the `NotesPage` class, which sets up the widgets and layout for the notes page.

The application's main function is in `main.py`, which creates an instance of the `MainWindow` class, shows the main window, and starts the application's event loop.

## Future Work

The next step for this project is to add a login page. This will require users to log in before they can create a new note. The login page will be created in a separate file and added to the `QStackedWidget` in the `MainWindow` class.
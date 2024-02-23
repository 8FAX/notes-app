# PyQt5 Note-Taking App

This is a simple note-taking app built with PyQt5. It allows users to jot down their thoughts, ideas, and dreams, and save them for later reference.

## Features

- **Note-Taking**: Users can write their notes in a text area. The notes can be as long or as short as they want.

- **Tagging**: Users can add tags to their notes. Tags are separated by commas and can be used to categorize and easily find notes later.

- **Saving Notes**: Users can save their notes by entering a file name and clicking the "Save" button. The notes are saved in JSON format, with the current date and time, the content of the notes, and the list of tags.

## Structure

The application is structured into separate pages, each in its own file:

- `notes_page.py`: This file contains the `NotesPage` class, which sets up the widgets and layout for the notes page.

- `login_page.py`: This file contains the `LoginPage` class, which handles user authentication and login functionality.

The application's main function is in `main.py`, which creates an instance of the `MainWindow` class, shows the main window, and starts the application's event loop.

Separating the application into separate pages and events in their own files is a good practice for keeping the codebase organized and maintainable as the project grows.

By having each page in its own file, such as `notes_page.py` and `login_page.py`, it becomes easier to locate and modify specific functionality related to that page. This modular approach allows for better code reuse and makes it simpler to add or remove pages in the future.

Similarly, having events in their own files, such as `main.py`, helps to keep the codebase clean and organized. Each event can be defined in its own file, making it easier to understand and modify specific functionality without affecting other parts of the application.

This separation of concerns also promotes code readability and maintainability. It allows developers to focus on specific tasks or features without being overwhelmed by a large and complex codebase.

Overall, organizing pages and events into separate files helps to keep the project structured, scalable, and easier to maintain as it continues to evolve.

## Future Work

The next step for this project is to implement a database to store user information and notes. This will allow for more secure and scalable storage of data. Additionally, further enhancements can be made to the user interface and functionality based on user feedback and requirements.

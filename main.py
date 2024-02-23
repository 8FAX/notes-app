import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from pages.notes_page import NotesPage
from pages.login_page import LoginPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        login_page = LoginPage(self.stacked_widget)
        notes_page = NotesPage()

        self.stacked_widget.addWidget(login_page) 
        self.stacked_widget.addWidget(notes_page)


        self.stacked_widget.setCurrentWidget(login_page)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

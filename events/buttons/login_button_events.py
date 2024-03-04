
from PyQt5.QtCore import QTimer
from assets.styles import login_input_style_fail, login_input_style
from events.client.PWauthentication import authenticate

def on_login_button_clicked(login_page):
    username = login_page.username_input.text()
    password = login_page.password_input.text()
    data = authenticate(username, password)
    if data == True:
        login_page.stacked_widget.setCurrentIndex(1) # Switch to the notes page
    else:
        login_page.password_input.setStyleSheet(login_input_style_fail)
        QTimer.singleShot(3000, lambda: reset_password_field(login_page))
        
def reset_password_field(login_page):
    login_page.password_input.setStyleSheet(login_input_style)
    login_page.password_input.clear()

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QStackedWidget, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
d = {}


def set_login(login: str):
    if login != '':
        d['login'] = login
        return True
    else:
        return 402

def set_password(password: str):
    if password != '':
        d['password'] = password
        return True
    else:
        return 402

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 1200, 800) # Ширина и высота окна 2 последних параметра

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.registration_window = RegistrationWindow()
        self.login_window = LoginWindow()
        self.staff_management_window = StaffManagementWindow()

        self.stacked_widget.addWidget(self.registration_window)
        self.stacked_widget.addWidget(self.login_window)
        self.stacked_widget.addWidget(self.staff_management_window)

        self.show_login_window()

    def show_registration_window(self):
        self.stacked_widget.setCurrentWidget(self.registration_window)

    def show_login_window(self):
        self.stacked_widget.setCurrentWidget(self.login_window)

    def show_staff_management_window(self):
        self.stacked_widget.setCurrentWidget(self.staff_management_window)


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Registration"))

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setMinimumHeight(50)
        self.password_input.setMinimumWidth(80)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.register_button = QPushButton("Register")
        self.register_button.setFont(QFont("Arial", 14))
        self.register_button.setMinimumHeight(50)
        self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        self.back_button = QPushButton("Back to Login")
        self.back_button.setFont(QFont("Arial", 14))
        self.back_button.setMinimumHeight(50)
        self.back_button.clicked.connect(self.go_back)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if set_login(username) != 402 and set_password(password) != 402:
            QMessageBox.information(self, "Registration", "Registration successful")

        elif set_password(password) == 402 or set_login(username) == 402 :
            QMessageBox.information(self, "Registration", "Пароль или логин не может быть пустым")

    def go_back(self):
        self.parentWidget().parentWidget().show_login_window()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Login"))

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.setFont(QFont("Arial", 14))
        self.login_button.setMinimumHeight(50)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.register_button = QPushButton("Register")
        self.register_button.setFont(QFont("Arial", 14))
        self.register_button.setMinimumHeight(50)
        self.register_button.clicked.connect(self.go_to_register)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        QMessageBox.information(self, "Login", "Login successful")
        self.parentWidget().parentWidget().show_staff_management_window()

    def go_to_register(self):
        self.parentWidget().parentWidget().show_registration_window()


class StaffManagementWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Staff Management"))

        # Add staff management UI elements here

        self.logout_button = QPushButton("Logout")
        self.logout_button.setFont(QFont("Arial", 14))
        self.logout_button.setMinimumHeight(50)
        self.logout_button.clicked.connect(self.logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def logout(self):
        self.parentWidget().parentWidget().show_login_window()


def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
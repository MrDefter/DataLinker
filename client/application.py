import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QFrame, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from config import ConfigWidgets

# Окно авторизации
class Authorization(QMainWindow):
    
    # Конструктор
    def __init__(self, app):
        super().__init__()

        # Вызов экземпляра объекта QApplication([])
        self.app = app

        # Вызов экземпляра объекта ConfigWidgets()
        self.config_widgets = ConfigWidgets(self.app)

        # Создание главного окна програмы 
        icon = QIcon("images/image2.png")
        self.setWindowTitle('DataLinker')
        self.setGeometry(0, 0, 1280, 720)
        self.setFixedSize(1280, 720)
        self.config_widgets.center_window(self)
        self.setWindowIcon(icon)

        # Добавление стиля окну
        label = QLabel(self)
        pixmap = QPixmap("images/image1.png")  
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        self.setCentralWidget(label)

        # Создание строки ввода для логина
        self.input_login = QLineEdit(self)
        self.input_login.setGeometry(self.config_widgets.center_widget_x(self, 250), self.config_widgets.center_widget_y(self, 40)-60, 250, 40)
        self.input_login.setStyleSheet("background-color: #FFFAFA; border: 1px solid #FFFAFA;")
        self.input_login.setStyleSheet("font-size: 18px; color: #808080;")
        self.input_login.setPlaceholderText("Введите логин")

        # Создание строки ввода для пароля
        self.input_password = QLineEdit(self)
        self.input_password.setGeometry(self.config_widgets.center_widget_x(self, 250), self.config_widgets.center_widget_y(self, 40)+10, 250, 40)
        self.input_password.setStyleSheet("background-color: #FFFAFA; border: 1px solid #FFFAFA;")
        self.input_password.setStyleSheet("font-size: 18px; color: #808080;")
        self.input_password.setPlaceholderText("Введите пароль")

        # Создание кнопки
        button_login = QPushButton("Вход", self)
        button_login.setGeometry(self.config_widgets.center_widget_x(self, 200), self.config_widgets.center_widget_y(self, 50)+100, 200, 50) 

        # Подключение функции-обработчика к сигналу кнопки
        button_login.clicked.connect(lambda: self.button_clicked_login(self.input_login.text(), self.input_password.text(), self))

    def button_clicked_login(self, login, password, window): 
        
        # Проверка правильности вводимых данных
        if self.config_widgets.check_login(login, password) == True:

            self.main_menu = MainMenu() 
            self.main_menu.show()
            window.hide()


# Окно главного меню
class MainMenu(QMainWindow):

    # Конструктор
    def __init__(self):
        super().__init__()

        # Вызов экземпляра объекта QApplication([])
        self.app = app

        # Вызов экземпляра объекта ConfigWidgets()
        self.config_widgets = ConfigWidgets(self.app)

        # Создание главного окна програмы 
        self.setWindowTitle('Главное меню')
        self.setGeometry(0, 0, 1280, 720)
        self.setFixedSize(1280, 720)
        self.config_widgets.center_window(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Authorization(app)
    window.show()
    sys.exit(app.exec_())

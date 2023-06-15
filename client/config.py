from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import QObject, pyqtSlot, QTimer
from PyQt5.QtGui import QIcon
import time
from database import BaseConfig

class ConfigWidgets(QObject):

    # Конструктор
    def __init__(self, app):
        super().__init__()

        self.app = app

    # Расположение окна по центру   
    def center_window(self, window):
        
        # Нахождение размера экрана монитора и окна приложения
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = window.geometry()

        # Нахождение координат x и y для расположения окна по центру
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2

        window.move(x, y)

    # Расположение кнопки по центру по координате X
    def center_widget_x(self, window, size):

        # Нахождение ширины окна приложения
        window_size = window.size()
        window_width = window_size.width()

        # Вычисление координаты x для расположения виджета по центру по оси x
        x = (window_width - size) // 2

        return x

    # Расположение кнопки по центру по координате Y
    def center_widget_y(self, window, size):

        # Нахождение высоты окна приложение
        window_size = window.size()
        window_height = window_size.height()

        # Вычисление координаты y для расположения виджета по центру по оси y
        y = (window_height - size) // 2

        return y

    # Обработчик для кнопки авторизации
    def check_login(self, login, password):

        # Вызов экземпляра объекта BaseConfig()
        self.base_config = BaseConfig()
        
        # Проверка в базе данных
        if self.base_config.base_connect_login(login, password) == True:

            # Создание и настройка объекта QSystemTrayIcon
            tray_icon = QSystemTrayIcon(self.app)
            icon_successfully = QIcon("images/image2.png")
            tray_icon.setIcon(icon_successfully)
            tray_icon.setVisible(True)

            # Создание всплывающего уведомления
            tray_icon.showMessage("DataLinker", "Авторизация прошла успешно!", QSystemTrayIcon.Information, 5000)

            # Создание таймера для закрытия уведомления через 5 секунд
            timer = QTimer()
            timer.setInterval(5000)
            timer.setSingleShot(True)
            timer.timeout.connect(self.app.quit)
            timer.start()

            # Остановка работы программы на 3 секунды
            time.sleep(3)

            # Открытие окна после авторизации
            return True

        else:

            # Создание и настройка объекта QSystemTrayIcon
            tray_icon = QSystemTrayIcon(self.app)
            icon_successfully = QIcon("images/image2.png")
            tray_icon.setIcon(icon_successfully)
            tray_icon.setVisible(True)

            # Создание всплывающего уведомления
            tray_icon.showMessage("DataLinker", "Авторизация не удалась!" +  "  Количество попыток: " + "тест", QSystemTrayIcon.Information, 5000)

            # Создание таймера для закрытия уведомления через 5 секунд
            timer = QTimer()
            timer.setInterval(5000)
            timer.setSingleShot(True)
            timer.timeout.connect(self.app.quit)
            timer.start()
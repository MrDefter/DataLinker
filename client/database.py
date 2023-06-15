import sqlite3

class BaseConfig():
    
    def base_connect_login(self, login_form, password_form):

        # Установка соединения с базой данных
        conn = sqlite3.connect('data/base.db')

        # Создание объекта для выполнения действий с базой данных
        cursor = conn.cursor()

        # Запрос данных
        cursor.execute('SELECT * FROM users')

        # Получение результаты запроса
        results = cursor.fetchall()

        # Обработка базы данных
        
        for row in results:
            
            
            # Запись в переменные логина и пароля
            login_base = row[1]
            password_base = row[2]

            # Проверка логина и пароля в базе данных
            if login_base == login_form and password_base == password_form:

                return True

            else:

                return False
                
        # Закрыть соединение с базой данных
        conn.close()
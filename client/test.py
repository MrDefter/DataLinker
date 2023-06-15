import sqlite3 
       

conn = sqlite3.connect('base.db')

cursor = conn.cursor()

# Выполняем SQL-запрос для создания таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Сохраняем изменения
conn.commit()

# Установка соединения с базой данных
conn = sqlite3.connect('base.db')

# Создание объекта для выполнения действий с базой данных
cursor = conn.cursor()

username = 'admin'
password = 'admin'

cursor.execute('INSERT INTO users (login, password) VALUES (?, ?)', (username, password))

conn.commit()
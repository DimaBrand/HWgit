#Создайте новую Базу данных
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Выберите случайную запись из БД
# Если каждое число данной записи чётное, то удалите
# эту запись, если нечётное, то обновите данные в ней на (2,2)

# import sqlite3
# import random
#
# conn = sqlite3.connect('name4.db')
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT)""")
# for i in range(5):
#     a = random.randint(0, 9)
#     b = random.randint(0, 9)
#     cursor.execute("""INSERT INTO tab_1(col_1, col_2) VALUES (?,?)""", (a, b))
#
# cursor.execute('''SELECT id FROM tab_1''')
# k = cursor.fetchall()
# print(k)
#
# r = random.choice(k)
# print(r)
# cursor.execute('''SELECT col_1,col_2 FROM tab_1 WHERE id=?''', r)
# k = cursor.fetchall()
# print(k)
# if k[0][0] % 2 == 0 and k[0][1] % 2 == 0:
#     cursor.execute('''DELETE FROM tab_1 WHERE id =? ''', r)
#     # conn.commit()
# else:
#     cursor.execute('''UPDATE tab_1 SET col_1=2,col_2=2 WHERE id=?''', r)
#
# # conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)



#Создайте метод класса для работы с БД.
# Достаточно одной колонки в таблице.
# Тип INT.В БД:Если передан 1 аргумент, вставить в таблицу запись с числом 3.
# Если переданы 2 аргумента: проверить или второй аргумент является числом.
# Если условие верно, то удалить первую запись с БД.
# Если переданы 2 аргумента и их тип значений неизвестен,
# а 3 аргумент является числом, то обновить значение колонки БД на число 77
# в 3 записи.

# import sqlite3
#
# conn = sqlite3.connect('task.lesson20')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT)''')
#
# class A:
#     def method(self, a=None, b=None, c=None):
#         #Если передан 1 аргумент, вставить в таблицу запись с числом 3.
#         if a is not None and b is None and c is None:
#             cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')
#             print('INSERT 3')
#         # Если переданы 2 аргумента: проверить является ли второй аргумент числом
#         # Если условие верно, то удалить первую запись с БД
#         elif a is not None and type(b) is int and c is None:
#             cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
#             print('DELETE ID = 1')
#         # Если переданы 2 аргумента и их тип значений неизвестен,
#         # а 3 аргумент является числом, то обновить значение колонки БД на число 77
#         # в 3 записи.
#         elif a is not None and b is not None and type(c) is int:
#             cursor.execute('''UPDATE tab_1 SET col_1 = 77 WHERE id = 3''')
#             print('UPDATE ID 3')
#
#
# a_obj = A()
# a_obj.method('f','g',3)
#
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# conn.commit()


#Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
# Заполнить её с помощью INSERT данными (3 записи).
# Удалить с помощью DELETE 2 запись.
# Обновить значения 3-ей записи на:
# hello world с помощью UPDATE
# *Записать данные с таблицы в файл в три колонки.
# Первая – id, вторая и третья с данными

# import sqlite3
# import random
#
# conn = sqlite3.connect('task3.db')
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)""")
# for i in range(5):
#     a = "java"
#     b = "python"
#     cursor.execute("""INSERT INTO tab_1(col_1, col_2) VALUES (?,?)""", (a, b))
#
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
#
# cursor.execute('''DELETE FROM tab_1 WHERE id=2 ''')
#     # conn.commit()
#
# cursor.execute('''UPDATE tab_1 SET col_1 = 'hello', col_2 = 'world' WHERE id=3''')
# k = cursor.fetchall()
# # conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
#
# f  = open ('text_1.txt', 'w')
# for i in k:
#
#     s = ','.join([str(x) for x in i])
#     f.write(s+'\n')
#     print(s)
# f.close()
#
# print(k)




# 1. Сформулируйте SQL запрос для создания таблицы book
# (book_id INT …, title TEXT, author TEXT, price INT, amount INT )
# 2. Занесите новую строку в таблицу book с клавиатуры
# 3. Выбрать информацию о всех книгах из таблицы book.
#
# import sqlite3
#
# conn = sqlite3.connect('book.db')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS book(book_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, price
#     INTEGER, amount INTEGER)''')
#
# a = input("Введите название книги: ")
# b = input("Введите имя автора: ")
# c = int(input("Введите стоимость: "))
# d = int(input("Введите количество: "))
# cursor.execute('''INSERT INTO book(title, author, price, amount) VALUES (?,?,?,?)''', (a, b, c, d))
# cursor.execute('''SELECT * FROM book''')
# k = cursor.fetchall()
# print(k)





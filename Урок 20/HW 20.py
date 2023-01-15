import sqlite3

conn = sqlite3.connect('mymovies.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movie_tab(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, release_year INT, genre TEXT)''')

cursor.execute('''SELECT * FROM movie_tab''')

print('Введите "1", чтобы добавить свой фильм')
print('Введите "2", чтобы посмотреть список всех фильмов')
print('Введите "3", чтобы выбрать год выпуска фильма')
print('Введите "4", чтобы выбрать жанр фильма')
print('Введите "0", чтобы выйти')

while True:

    r = int(input('Сделайте ваш выбор: '))

    def movie():
        a = input('Введите название фильма: ')
        b = int(input('Введите год выпуска: '))
        c = input('Введите жанр фильма: ')
        cursor.execute('''INSERT INTO movie_tab(name, release_year, genre) VALUES (?,?,?)''', (a, b, c))
        conn.commit()
    def spisok():
        cursor.execute('''SELECT * FROM movie_tab''')
        m = cursor.fetchall()
        for i in m:
            print(*i)

    def year():
        god = input('Введите ID года фильма, который вы хотите посмотреть: ')
        cursor.execute('''SELECT name, release_year, genre FROM movie_tab WHERE id=?''', god)
        m = cursor.fetchall()
        for i in m:
            print(*i)

    def zhanr():
        zh = input('Введите ID жанра фильма, который хотите посмотреть: ')
        cursor.execute('''SELECT name, release_year, genre FROM movie_tab WHERE id=?''', zh)
        m = cursor.fetchall()
        for i in m:
            print(*i)

    if r == 1:
        movie()
    elif r == 2:
        spisok()
    elif r == 3:
        god()
    elif r == 4:
        zhanr()
    elif r == 0:
        print('До свидания!')
        break
    else:
        print('Введите цифру от 1 до 4!')

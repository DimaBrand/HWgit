# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

def calculator(a, b):

    if s == '+':
        return a + b

    if s == '-':
        return a - b

    if s == '*':
        return a * b

    if s == '**':
        return a ** b

    if s == ('%'):
        return a % b

    if s == '/':
        try:
            return a / b
        except ZeroDivisionError:
            print('На 0 делить нельзя!')

while True:

    a = float(input('a = '))
    b = float(input('b = '))
    s = input('Введите + - * / % ** или "q" для выхода: ')

    if s == 'q':
        break

    print('Результат: ', calculator(a, b))


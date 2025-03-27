import math
from tkinter import *
from tkinter import ttk


# Функция выбора режима работы калькулятора
def choose_regime():
    print('\nВыбирите режим калькулятора:\n\t1)Решение линейного уравнения\n\t2)Решение квадратного уравнения\n\t3)Режим калькулятора\n')
    while True:
        regime = input()
        if regime in ['1', '2', '3']:
            regime = int(regime)
            return regime
        else:
            print('ВВЕДИТЕ 1 ИЛИ 2 ИЛИ 3 !!!!\n')
            pass

# Функция блока калькулятора
def calc():

    # Функция получения операции вычисления
    def get_op():
        while True:
            operator = input('введите операцию\n')
            if operator in ['-', '/', '*', '+']:

                return operator
            else:
                pass

    # Функция получения операндов
    def get_num():
        while True:
            num_1 = input('введите 1\n')
            num_2 = input('введите 2\n')

            try:
                num_1 = float(num_1)
                num_2 = float(num_2)

                return num_1, num_2
            except:
                print('ВВОДИ ЧИСЛА!!!')

    # Запись переменных с операцией и операндами
    op = get_op()
    num1, num2 = get_num()

    # Проверка деления на ноль
    if op == '/':
        while num2 == 0:
            num2 = input('ДЕЛЕНИЕ НА НОЛЬ. ВВЕДИТЕ ЕЩЁ РАЗ!\n')
            num2 = float(num2)
    else:
        pass

    # Блок непосредственного вычисления
    arg = 'x' + op + 'y'
    f = lambda x, y: eval(arg)
    print(f'{num1} {op} {num2} = ', f(num1, num2))

# Функция блока линейного уравнения
def lin_eq():
    print('Форма уравнения: y = k*x + b')
    while True:
        k = input('Введите k\n')
        b = input('Введите b\n')
        y = input('Введите y\n')

        try:
            k = float(k)
            b = float(b)
            y = float(y)

            while k == 0:
                k = input('k не должно быть равно 0! Введите ещё раз\n')
                k = float(k)

            answr = (y - b) / k
            print('Ответ: х =', answr)

            break
        except:
            print('ВВОДИ ЧИСЛА!!!')


# Функция блока квадратного уравнения
def sq_eq():
    print('Форма уравнения: y = a*x^2 + b*x + c')
    while True:
        a = input('Введите a\n')
        b = input('Введите b\n')
        c = input('Введите c\n')
        y = input('Введите y\n')

        try:
            a = float(a)
            b = float(b)
            c = float(c)
            y = float(y)

            c = c - y
            discr = b ** 2 - 4 * a * c

            if discr > 0:
                x1 = (-b + math.sqrt(discr)) / (2 * a)
                x2 = (-b - math.sqrt(discr)) / (2 * a)
                print("Ответ: x_1 = %.6f \n\t   x_2 = %.6f" % (x1, x2))

            elif discr == 0:
                x = -b / (2 * a)
                print("x = %.6f" % x)
            else:
                print("Корней нет")

            break
        except:
            print('ПРОВЕРЬТЕ ВВЕДЁННЫЕ ЗНАЧЕНИЯ!!!')


# Главная функция программы - выбор между режимами и вызов соответствующих функций
def overall_calculator():
    choose_reg = choose_regime()

    # Условие выбора блока линейного уравнения
    if choose_reg == 1:
        lin_eq()

    # Условие выбора блока квадратного уравнения
    elif choose_reg == 2:
        sq_eq()

    # Условие выбора блока калькулятора
    elif choose_reg == 3:
        calc()

# Безконечный вызов главной функции












root = Tk()     # создаем окно main
root.title("Выбирите режим калькулятора")     # устанавливаем заголовок окна
root.geometry("400x140")    # устанавливаем размеры окна

# добавляем кнопку, настраиваем ее форму и цвет
# при нажатии сработает функция hello world
btn1 = ttk.Button(text="Решение линейного уравнения", command=choice_1)
btn2 = ttk.Button(text="Решение квадратного уравнения", command=choice_2)
btn3 = ttk.Button(text="Режим калькулятора", command=choice_3)

btn1.pack(anchor="center", fill=X, expand=True, ipady=10)
btn2.pack(anchor="center", fill=X, expand=True, ipady=10)
btn3.pack(anchor="center", fill=X, expand=True, ipady=10)
root.mainloop()

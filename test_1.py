import math



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

            c = c-y
            discr = b ** 2 - 4 * a * c

            if discr > 0:
                x1 = (-b + math.sqrt(discr)) / (2 * a)
                x2 = (-b - math.sqrt(discr)) / (2 * a)
                print("x1 = %.6f \nx2 = %.6f" % (x1, x2))

            elif discr == 0:
                x = -b / (2 * a)
                print("x = %.6f" % x)
            else:
                print("Корней нет")

            break
        except:
            print('ПРОВЕРЬТЕ ВВЕДЁННЫЕ ЗНАЧЕНИЯ!!!')

sq_eq()
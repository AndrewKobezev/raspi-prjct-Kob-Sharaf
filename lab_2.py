import math
from tkinter import *
from tkinter import ttk


def choice_lin_eq():

    def solve_handlr_lin():

        label = ttk.Label(lin_eq_gui, padding=17, width=40, font=("Arial", 12), justify=LEFT, text=" ")
        label.place(x=200, y=160)

        k = entry_k.get()
        b = entry_b.get()
        y = entry_y.get()

        try:
            k = float(k)
            b = float(b)
            y = float(y)

            if k == 0:
                label_x1 = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text='k не должно быть \nравно 0!')
                label_x1.place(x=200, y=150)
            else:
                x = (y - b) / k
                label_x1 = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text=f'Ответ: х = {x:.4f}')
                label_x1.place(x=200, y=150)

        except:
            label_x1 = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text='ВВОДИ ЧИСЛА!!!')
            label_x1.place(x=200, y=150)

    lin_eq_gui = Tk()
    lin_eq_gui.title("Решение линейного уравнения")  # устанавливаем заголовок окна
    lin_eq_gui.geometry("400x200")  # устанавливаем размеры окна

    label1 = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=CENTER,
                       text="Форма уравнения:\ny = k*x + b\n\nРешение относительно x")
    label2 = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text="Введите:")

    label_k = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text="k = ")
    label_b = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text="b = ")
    label_y = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text="c = ")
    entry_k = ttk.Entry(lin_eq_gui)
    entry_b = ttk.Entry(lin_eq_gui)
    entry_y = ttk.Entry(lin_eq_gui)

    solve_btn = ttk.Button(lin_eq_gui, text="Найти", command=solve_handlr_lin)
    root_btn = ttk.Button(lin_eq_gui, text="Меню", command=root_gui)

    label1.pack(anchor="n")
    label2.pack(anchor="w")

    label_k.place(x=10, y=100)
    label_b.place(x=10, y=130)
    label_y.place(x=10, y=160)
    entry_k.place(x=35, y=100)
    entry_b.place(x=35, y=130)
    entry_y.place(x=35, y=160)

    solve_btn.place(x=200, y=100)
    root_btn.place(x=10, y=10)

def choice_sq_eq():

    # def clear_handlr_sq():
    #     print(0)
    #     label_x.master.destroy()

    def solve_handlr_sq():

        label = ttk.Label(sq_eq_gui, padding=17, width=30, font=("Arial", 12), justify=LEFT, text=" ")
        label.place(x=200, y=160)

        a = entry_a.get()
        b = entry_b.get()
        c = entry_c.get()
        y = entry_y.get()

        try:
            a = float(a)
            b = float(b)
            c = float(c)
            y = float(y)

            c = c - y
            discr = b ** 2 - 4 * a * c

            if discr > 0 & int(a) != 0:
                x1 = (-b + math.sqrt(discr)) / (2 * a)
                x2 = (-b - math.sqrt(discr)) / (2 * a)
                label_x = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT,
                                    text="Ответ: \nx_1 = %.6f \nx_2 = %.6f" % (x1, x2))
                label_x.place(x=200, y=160)

            elif discr == 0:
                x = -b / (2 * a)
                label_x = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text="Ответ: x = %.6f" % x)
                label_x.place(x=200, y=160)

            elif a == 0:
                label_x = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text="Вы ввели линейное\nуравнение!")
                label_x.place(x=200, y=160)
            else:
                label_x = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text="Ответ: \nКорней нет")
                label_x.place(x=200, y=160)

        except:
            label_x = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text="ПРОВЕРЬТЕ \nВВЕДЁННЫЕ \nЗНАЧЕНИЯ!!!")
            label_x.place(x=200, y=160)


    sq_eq_gui = Tk()
    sq_eq_gui.title("Решение квадратного уравнения")  # устанавливаем заголовок окна
    sq_eq_gui.geometry("400x250")  # устанавливаем размеры окна

    label1 = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=CENTER,
                       text="Форма уравнения:\ny = k*x + b\n\nРешение относительно x")
    label2 = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text="Введите:")

    label_a = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text="a = ")
    label_b = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text="b = ")
    label_c = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text="c = ")
    label_y = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text="y = ")
    entry_a = ttk.Entry(sq_eq_gui)
    entry_b = ttk.Entry(sq_eq_gui)
    entry_c = ttk.Entry(sq_eq_gui)
    entry_y = ttk.Entry(sq_eq_gui)

    solve_btn = ttk.Button(sq_eq_gui, text="Найти", command=solve_handlr_sq)
    root_btn = ttk.Button(sq_eq_gui, text="Меню", command=root_gui)
    #clr_btn = ttk.Button(sq_eq_gui, text="Clear", command=clear_handlr_sq)

    label1.pack(anchor="n")
    label2.pack(anchor="w")

    label_a.place(x=10, y=100)
    label_b.place(x=10, y=130)
    label_c.place(x=10, y=160)
    label_y.place(x=10, y=190)
    entry_a.place(x=35, y=100)
    entry_b.place(x=35, y=130)
    entry_c.place(x=35, y=160)
    entry_y.place(x=35, y=190)

    solve_btn.place(x=200, y=100)
    root_btn.place(x=10, y=10)
    #clr_btn.place(x=300, y=100)

def choice_calc():

    def solve_handlr_calc():

        label = ttk.Label(calc_gui, padding=17, width=30, font=("Arial", 12), justify=LEFT, text=" ")
        label.place(x=150, y=160)

        a = entry_a.get()
        b = entry_b.get()

        try:
            x = float(a)
            y = float(b)

            if op.get() == '/':
                if y == 0:
                    label_x = ttk.Label(calc_gui, foreground='#B71C1C', font=("Arial", 12),
                                        justify=LEFT, text='Деление на ноль!!')
                    label_x.place(x=200, y=170)

                else:
                    arg = f'{x}{op.get()}{y}'
                    f = lambda x, y: eval(arg)
                    label_x = ttk.Label(calc_gui, font=("Arial", 12), justify=LEFT,
                                        text=f'Ответ: {x} {op.get()} {y} = {f(x, y)}')
                    label_x.place(x=150, y=160)
            else:
                arg = f'{x}{op.get()}{y}'
                f = lambda x, y: eval(arg)
                label_x = ttk.Label(calc_gui, font=("Arial", 12), justify=LEFT,
                                    text=f'Ответ: {x} {op.get()} {y} = {f(x, y)}')
                label_x.place(x=150, y=160)

        except:
            label_x = ttk.Label(calc_gui, font=("Arial", 12), justify=LEFT, text="ПРОВЕРЬТЕ \nВВЕДЁННЫЕ \nЗНАЧЕНИЯ!!!")
            label_x.place(x=200, y=160)

    calc_gui = Tk()
    calc_gui.title("Режим калькулятора")  # устанавливаем заголовок окна
    calc_gui.geometry("375x250")  # устанавливаем размеры окна

    label1 = ttk.Label(calc_gui, font=("Arial", 12), justify=CENTER, text="Вычислить:")
    label2 = ttk.Label(calc_gui, font=("Arial", 12), justify=CENTER, text="Выберите действие:")

    op = StringVar(calc_gui, value='+')

    label_op = ttk.Label(calc_gui, font=("Arial", 12), justify=LEFT, textvariable=op)

    entry_a = ttk.Entry(calc_gui)
    entry_b = ttk.Entry(calc_gui)

    solve_btn = ttk.Button(calc_gui, text="Найти", command=solve_handlr_calc)
    root_btn = ttk.Button(calc_gui, text="Меню", command=calc_gui)

    op_div_btn = ttk.Radiobutton(calc_gui, text="/", value="/", variable=op)
    op_mult_btn = ttk.Radiobutton(calc_gui, text="*", value="*", variable=op)
    op_summ_btn = ttk.Radiobutton(calc_gui, text="+", value="+", variable=op)
    op_minus_btn = ttk.Radiobutton(calc_gui, text="-", value="-", variable=op)

    label1.place(x=150, y=15)

    label_op.place(x=183, y=50)
    entry_a.place(x=50, y=50)
    entry_b.place(x=200, y=50)

    solve_btn.place(x=250, y=130)
    root_btn.place(x=10, y=10)

    label2.place(x=120, y=75)
    op_div_btn.place(x=50, y=100)
    op_mult_btn.place(x=135, y=100)
    op_summ_btn.place(x=215, y=100)
    op_minus_btn.place(x=295, y=100)


def root_gui():

    root = Tk()     # создаем окно main
    root.title("Выберите режим калькулятора")     # устанавливаем заголовок окна
    root.geometry("400x140")    # устанавливаем размеры окна

    # добавляем кнопку, настраиваем ее форму и цвет
    # при нажатии сработает функция hello world
    btn1 = ttk.Button(root, text="Решение линейного уравнения", command=choice_lin_eq)
    btn2 = ttk.Button(root, text="Решение квадратного уравнения", command=choice_sq_eq)
    btn3 = ttk.Button(root, text="Режим калькулятора", command=choice_calc)

    btn1.pack(anchor="center", fill=X, expand=True, ipady=10)
    btn2.pack(anchor="center", fill=X, expand=True, ipady=10)
    btn3.pack(anchor="center", fill=X, expand=True, ipady=10)
    root.mainloop()

root_gui()
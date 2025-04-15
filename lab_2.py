import math
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# Функция режима решения линейного уравнения
def choice_lin_eq():

    def solve_handlr_lin():

        k = entry_k.get()
        b = entry_b.get()
        y = entry_y.get()

        try:
            k = float(k)
            b = float(b)
            y = float(y)

            if k == 0:
                label_x.config(foreground='red', text='k не должно быть \nравно 0!')
            else:
                x = (y - b) / k
                label_x.config(foreground='black', text=f'Ответ: х = {x:.4f}')
        except:
            label_x.config(foreground='red', text='ВВОДИ ЧИСЛА!!!')

    lin_eq_gui = Tk()
    lin_eq_gui.title("Решение линейного уравнения")  # устанавливаем заголовок окна
    lin_eq_gui.geometry("400x200")  # устанавливаем размеры окна

    label1 = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=CENTER,
                       text="Форма уравнения:\ny = k*x + b\n\nРешение относительно x")
    label2 = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text="Введите:")
    label_x = ttk.Label(lin_eq_gui, padding=17, width=40, font=("Arial", 12), justify=LEFT, text=" ")

    label_k = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text="k = ")
    label_b = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text="b = ")
    label_y = ttk.Label(lin_eq_gui, font=("Arial", 12), justify=LEFT, text="y = ")
    entry_k = ttk.Entry(lin_eq_gui)
    entry_b = ttk.Entry(lin_eq_gui)
    entry_y = ttk.Entry(lin_eq_gui)

    solve_btn = ttk.Button(lin_eq_gui, text="Найти", command=solve_handlr_lin)
    root_btn = ttk.Button(lin_eq_gui, text="Меню", command=root_gui)

    label1.pack(anchor="n")
    label2.pack(anchor="w")
    label_x.place(x=180, y=130)

    label_k.place(x=10, y=100)
    label_b.place(x=10, y=130)
    label_y.place(x=10, y=160)
    entry_k.place(x=35, y=100)
    entry_b.place(x=35, y=130)
    entry_y.place(x=35, y=160)

    solve_btn.place(x=200, y=100)
    root_btn.place(x=10, y=10)

# Функция режима решения квадратного уравнения
def choice_sq_eq():

    def solve_handlr_sq():

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
                label_x.config(foreground='black', text="Ответ: \nx_1 = %.6f \nx_2 = %.6f" % (x1, x2))
            elif discr == 0:
                x = -b / (2 * a)
                label_x.config(foreground='black', text="Ответ: x = %.6f" % x)
            elif a == 0:
                label_x.config(foreground='red', text="Вы ввели линейное\nуравнение!")
            else:
                label_x.config(foreground='black', text="Ответ: \nКорней нет")
        except:
            label_x.config(foreground='red', text="ПРОВЕРЬТЕ \nВВЕДЁННЫЕ \nЗНАЧЕНИЯ!!!")


    sq_eq_gui = Tk()
    sq_eq_gui.title("Решение квадратного уравнения")  # устанавливаем заголовок окна
    sq_eq_gui.geometry("400x250")  # устанавливаем размеры окна

    label1 = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=CENTER,
                       text="Форма уравнения:\ny = a*x^2 + b*x + c\n\nРешение относительно x")
    label2 = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text="Введите:")
    label_x = ttk.Label(sq_eq_gui, font=("Arial", 12), justify=LEFT, text=" ")

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

    label1.pack(anchor="n")
    label2.pack(anchor="w")
    label_x.place(x=200, y=160)

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

# Функция режима калькулятора
def choice_calc():

    def solve_handlr_calc():

        a = entry_a.get()
        b = entry_b.get()

        try:
            x = float(a)
            y = float(b)

            if op.get() == '/':
                if y == 0:
                    label_x.config(foreground='red', text='Деление на ноль!!')

                else:
                    arg = f'{x}{op.get()}{y}'
                    f = lambda x, y: eval(arg)
                    label_x.config(foreground='black', text=f'Ответ: {x} {op.get()} {y} = {f(x, y)}')

            else:
                arg = f'{x}{op.get()}{y}'
                f = lambda x, y: eval(arg)
                label_x.config(foreground='black', text=f'Ответ: {x} {op.get()} {y} = {f(x, y)}')

        except:
            label_x.config(foreground='red', text="ПРОВЕРЬТЕ \nВВЕДЁННЫЕ \nЗНАЧЕНИЯ!!!")

    calc_gui = Tk()
    calc_gui.title("Режим калькулятора")  # устанавливаем заголовок окна
    calc_gui.geometry("375x250")  # устанавливаем размеры окна

    label1 = ttk.Label(calc_gui, font=("Arial", 12), justify=CENTER, text="Вычислить:")
    label2 = ttk.Label(calc_gui, font=("Arial", 12), justify=CENTER, text="Выберите действие:")

    op = StringVar(calc_gui, value='+')

    label_op = ttk.Label(calc_gui, font=("Arial", 12), justify=LEFT, textvariable=op)

    entry_a = ttk.Entry(calc_gui)
    entry_b = ttk.Entry(calc_gui)

    label_x = ttk.Label(calc_gui, font=("Arial", 12), justify=LEFT, text=" ")

    solve_btn = ttk.Button(calc_gui, text="Найти", command=solve_handlr_calc)
    root_btn = ttk.Button(calc_gui, text="Меню", command=root_gui)

    op_div_btn      = ttk.Radiobutton(calc_gui, text="/", value="/", variable=op)
    op_mult_btn     = ttk.Radiobutton(calc_gui, text="*", value="*", variable=op)
    op_summ_btn     = ttk.Radiobutton(calc_gui, text="+", value="+", variable=op)
    op_minus_btn    = ttk.Radiobutton(calc_gui, text="-", value="-", variable=op)

    label1.place(x=150, y=15)
    label_x.place(x=100, y=170)

    label_op.place(x=183, y=50)
    entry_a.place(x=30, y=50)
    entry_b.place(x=230, y=50)

    solve_btn.place(x=250, y=130)
    root_btn.place(x=10, y=10)

    label2.place(x=120, y=75)
    op_div_btn.place(x=50, y=100)
    op_mult_btn.place(x=135, y=100)
    op_summ_btn.place(x=215, y=100)
    op_minus_btn.place(x=295, y=100)

# Функция режима построения графика функции
def choice_plot():
    import re

    def format_formula_latex(expr: str) -> str:
        #Преобразует Python-выражение в формат LaTeX для matplotlib.
        expr = expr.replace("**", "^")
        expr = expr.replace("*", r" ")  # можно убрать "\cdot", если нужно без знака умножения
        expr = re.sub(r'(?<!\^)(\d*)x(\^?\d*)', r'\1x\2', expr)  # формула с x
        return rf"$y = {expr}$"

    def plot_handlr():
        func_str = entry_func.get()
        try:
            x_min = float(entry_xmin.get())
            x_max = float(entry_xmax.get())
            step = float(entry_step.get())
            y_min = float(entry_ymin.get())
            y_max = float(entry_ymax.get())

            if step <= 0 or x_min >= x_max or y_min >= y_max:
                error_label.config(text="Неверные значения диапазонов или шага.")
                return

            x = np.arange(x_min, x_max, step)
            y = eval(func_str, {"x": x, "np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                                "log": np.log, "exp": np.exp, "sqrt": np.sqrt, "abs": np.abs})

            # Форматированное отображение формулы
            formula_latex = format_formula_latex(func_str)

            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(x, y, label=formula_latex)
            ax.set_title(f"График функции:\n{formula_latex}", fontsize=12)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.grid(True)
            ax.set_ylim(y_min, y_max)
            ax.legend()

            canvas = FigureCanvasTkAgg(fig, master=plot_gui)
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=180, width=580, height=400)

            toolbar = NavigationToolbar2Tk(canvas, plot_gui)
            toolbar.update()
            toolbar.place(x=10, y=590)

            error_label.config(text="")

        except Exception as e:
            error_label.config(text=f"Ошибка: {str(e)}")

    plot_gui = Tk()
    plot_gui.title("Построение графика функции")
    plot_gui.geometry("600x640")

    label_func = ttk.Label(plot_gui, font=("Arial", 12), text="Функция y = f(x):")
    entry_func = ttk.Entry(plot_gui, width=40)
    entry_func.insert(0, "x**3-3*x")

    label_xmin = ttk.Label(plot_gui, text="X мин:")
    entry_xmin = ttk.Entry(plot_gui, width=10)
    entry_xmin.insert(0, "-5")

    label_xmax = ttk.Label(plot_gui, text="X макс:")
    entry_xmax = ttk.Entry(plot_gui, width=10)
    entry_xmax.insert(0, "5")

    label_step = ttk.Label(plot_gui, text="Шаг:")
    entry_step = ttk.Entry(plot_gui, width=10)
    entry_step.insert(0, "0.1")

    label_ymin = ttk.Label(plot_gui, text="Y мин:")
    entry_ymin = ttk.Entry(plot_gui, width=10)
    entry_ymin.insert(0, "-5")

    label_ymax = ttk.Label(plot_gui, text="Y макс:")
    entry_ymax = ttk.Entry(plot_gui, width=10)
    entry_ymax.insert(0, "5")

    solve_btn = ttk.Button(plot_gui, text="Построить график", command=plot_handlr)
    root_btn = ttk.Button(plot_gui, text="Меню", command=root_gui)
    error_label = ttk.Label(plot_gui, foreground="red", font=("Arial", 10))

    # Расположение виджетов
    label_func.place(x=10, y=10)
    entry_func.place(x=10, y=35)

    label_xmin.place(x=10, y=70)
    entry_xmin.place(x=60, y=70)

    label_xmax.place(x=140, y=70)
    entry_xmax.place(x=200, y=70)

    label_step.place(x=280, y=70)
    entry_step.place(x=330, y=70)

    label_ymin.place(x=10, y=100)
    entry_ymin.place(x=60, y=100)

    label_ymax.place(x=140, y=100)
    entry_ymax.place(x=200, y=100)

    solve_btn.place(x=230, y=140)
    root_btn.place(x=10, y=140)
    error_label.place(x=10, y=170)




# Функция выбора режима калькулятора / меню
def root_gui():

    root = Tk()     # создаем окно root
    root.title("Выберите режим калькулятора")     # устанавливаем заголовок окна
    root.geometry("400x180")    # устанавливаем размеры окна

    # добавляем кнопки
    btn1 = ttk.Button(root, text="Решение линейного уравнения", command=choice_lin_eq)      # при нажатии сработает функция choice_lin_eq
    btn2 = ttk.Button(root, text="Решение квадратного уравнения", command=choice_sq_eq)     # при нажатии сработает функция choice_sq_eq
    btn3 = ttk.Button(root, text="Режим калькулятора", command=choice_calc)     # при нажатии сработает функция choice_calc
    btn4 = ttk.Button(root, text="Режим построения графика функции", command=choice_plot)  # при нажатии сработает функция choice_plot

    btn1.pack(anchor="center", fill=X, expand=True, ipady=10)
    btn2.pack(anchor="center", fill=X, expand=True, ipady=10)
    btn3.pack(anchor="center", fill=X, expand=True, ipady=10)
    btn4.pack(anchor="center", fill=X, expand=True, ipady=10)
    root.mainloop()

root_gui()
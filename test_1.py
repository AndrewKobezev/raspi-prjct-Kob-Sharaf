from tkinter import *
from tkinter import ttk




# def clear_handlr_sq():
#     print(0)
#     label_x.master.destroy()

def solve_handlr_calc():

    label = ttk.Label(calc_gui, padding=17, width=30, font=("Arial", 12), justify=LEFT, text=" ")
    label.place(x=150, y=160)

    a = entry_a.get()
    b = entry_b.get()

    try:
        x = float(a)
        y = float(b)

        if op.get() == '/':
            if y==0:
                label_x = ttk.Label(calc_gui, foreground='#B71C1C' , font=("Arial", 12),
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



calc_gui.mainloop()
#
# def exa():
#     # Функция получения операции вычисления
#     def get_op():
#         while True:
#             operator = input('введите операцию\n')
#             if operator in ['-', '/', '*', '+']:
#
#                 return operator
#             else:
#                 pass
#
#     # Функция получения операндов
#     def get_num():
#         while True:
#             num_1 = input('введите 1\n')
#             num_2 = input('введите 2\n')
#
#             try:
#                 num_1 = float(num_1)
#                 num_2 = float(num_2)
#
#                 return num_1, num_2
#             except:
#                 print('ВВОДИ ЧИСЛА!!!')
#
#     # Запись переменных с операцией и операндами
#     op = get_op()
#     num1, num2 = get_num()
#
#     # Проверка деления на ноль
#     if op == '/':
#         while num2 == 0:
#             num2 = input('ДЕЛЕНИЕ НА НОЛЬ. ВВЕДИТЕ ЕЩЁ РАЗ!\n')
#             num2 = float(num2)
#     else:
#         pass
#
#     # Блок непосредственного вычисления
#     arg = 'x' + op + 'y'
#     f = lambda x, y: eval(arg)
#     print(f'{num1} {op} {num2} = ', f(num1, num2))



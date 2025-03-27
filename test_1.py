from tkinter import *
from tkinter import ttk


def choice_1():
    print("1")
def choice_2():
    print("2")
def choice_3():
    print("3")

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


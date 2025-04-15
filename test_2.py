import flet as ft
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def main(page: ft.Page):
    page.title = "Математические режимы"

    def go_to(e, content):
        page.clean()
        page.add(content)

    def root_gui():
        def build_menu():
            page.clean()
            page.add(
                ft.Column([
                    ft.ElevatedButton("Решение линейного уравнения", on_click=lambda e: go_to(e, lin_eq_view())),
                    ft.ElevatedButton("Решение квадратного уравнения", on_click=lambda e: go_to(e, sq_eq_view())),
                    ft.ElevatedButton("Калькулятор", on_click=lambda e: go_to(e, calc_view())),
                    ft.ElevatedButton("Построение графика функции", on_click=lambda e: go_to(e, plot_view())),
                ], spacing=20)
            )

        return build_menu

    def lin_eq_view():
        k_field = ft.TextField(label="k")
        b_field = ft.TextField(label="b")
        y_field = ft.TextField(label="y")
        result_text = ft.Text("", size=16)

        def solve_lin_eq(e):
            try:
                k = float(k_field.value)
                b = float(b_field.value)
                y = float(y_field.value)
                if k == 0:
                    result_text.value = "k не должно быть равно 0!"
                else:
                    x = (y - b) / k
                    result_text.value = f"Ответ: x = {x:.4f}"
            except:
                result_text.value = "ВВОДИ ЧИСЛА!!!"
            page.update()

        return ft.Column([
            ft.Text("Форма уравнения: y = kx + b", size=18),
            k_field, b_field, y_field,
            ft.ElevatedButton("Найти", on_click=solve_lin_eq),
            result_text,
            ft.TextButton("Назад в меню", on_click=lambda e: root_gui()())
        ], spacing=10)

    def sq_eq_view():
        a_field = ft.TextField(label="a")
        b_field = ft.TextField(label="b")
        c_field = ft.TextField(label="c")
        y_field = ft.TextField(label="y")
        result_text = ft.Text("", size=16)

        def solve_sq_eq(e):
            try:
                a = float(a_field.value)
                b = float(b_field.value)
                c = float(c_field.value)
                y = float(y_field.value)
                c -= y
                discr = b ** 2 - 4 * a * c

                if a == 0:
                    result_text.value = "Это линейное уравнение!"
                elif discr > 0:
                    x1 = (-b + math.sqrt(discr)) / (2 * a)
                    x2 = (-b - math.sqrt(discr)) / (2 * a)
                    result_text.value = f"Ответ: x1 = {x1:.6f}, x2 = {x2:.6f}"
                elif discr == 0:
                    x = -b / (2 * a)
                    result_text.value = f"Ответ: x = {x:.6f}"
                else:
                    result_text.value = "Корней нет"
            except:
                result_text.value = "ПРОВЕРЬТЕ ВВЕДЁННЫЕ ЗНАЧЕНИЯ!!!"
            page.update()

        return ft.Column([
            ft.Text("Форма: y = ax² + bx + c", size=18),
            a_field, b_field, c_field, y_field,
            ft.ElevatedButton("Найти", on_click=solve_sq_eq),
            result_text,
            ft.TextButton("Назад в меню", on_click=lambda e: root_gui()())
        ], spacing=10)

    def calc_view():
        a_field = ft.TextField(label="a")
        b_field = ft.TextField(label="b")
        operation = ft.Dropdown(
            label="Операция",
            options=[
                ft.dropdown.Option("+"),
                ft.dropdown.Option("-"),
                ft.dropdown.Option("*"),
                ft.dropdown.Option("/")
            ],
            value="+"
        )
        result_text = ft.Text("", size=16)

        def solve_calc(e):
            try:
                x = float(a_field.value)
                y = float(b_field.value)
                op = operation.value
                if op == "/" and y == 0:
                    result_text.value = "Деление на ноль!!"
                else:
                    result = eval(f"{x}{op}{y}")
                    result_text.value = f"Ответ: {x} {op} {y} = {result}"
            except:
                result_text.value = "ПРОВЕРЬТЕ ВВЕДЁННЫЕ ЗНАЧЕНИЯ!!!"
            page.update()

        return ft.Column([
            a_field, b_field, operation,
            ft.ElevatedButton("Вычислить", on_click=solve_calc),
            result_text,
            ft.TextButton("Назад в меню", on_click=lambda e: root_gui()())
        ], spacing=10)

    def plot_view():
        func_field = ft.TextField(label="Функция (например: x**2)")
        result_text = ft.Text("", size=16)
        graph_container = ft.Container()

        def plot_handler(e):
            try:
                x = np.linspace(-10, 10, 400)
                y = eval(func_field.value)
                fig, ax = plt.subplots()
                ax.plot(x, y)
                ax.set_title("График функции")
                buffer = BytesIO()
                fig.savefig(buffer, format="png")
                plt.close(fig)
                buffer.seek(0)
                img_data = base64.b64encode(buffer.read()).decode("utf-8")
                graph_container.content = ft.Image(src_base64=img_data, width=600, height=400)
                result_text.value = "График построен"
            except Exception as ex:
                result_text.value = f"Ошибка: {ex}"
            page.update()

        return ft.Column([
            ft.Text("Построение графика функции", size=18),
            func_field,
            ft.ElevatedButton("Построить", on_click=plot_handler),
            result_text,
            graph_container,
            ft.TextButton("Назад в меню", on_click=lambda e: root_gui()())
        ], spacing=10, scroll=ft.ScrollMode.ALWAYS)

    root_gui()()

ft.app(target=main)

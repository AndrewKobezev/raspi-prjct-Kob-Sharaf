from tkinter import *
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


# plot function is created for
# plotting the graph in
# tkinter window
def plot():
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5), dpi=100)
    def f():
        return 4 * x - x**2

    x = np.linspace(-9, 9, 100)
    y = f()

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


# the main Tkinter window
window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("500x600")

# button that displays the plot
plot_button = Button(master=window,
                     command=plot,
                     height=2,
                     width=10,
                     text="Plot")

# place the button
# in main window
plot_button.pack()

# run the gui
window.mainloop()



#
# def choice_plot():
#
#     def plot():
#         # the figure that will contain the plot
#         fig = Figure(figsize=(5, 5),
#                      dpi=100)
#
#         # list of squares
#         y = [i ** 2 for i in range(101)]
#
#         # adding the subplot
#         plot1 = fig.add_subplot(111)
#
#         # plotting the graph
#         plot1.plot(y)
#
#         # creating the Tkinter canvas
#         # containing the Matplotlib figure
#         canvas = FigureCanvasTkAgg(fig, master=window)
#         canvas.draw()
#
#         # placing the canvas on the Tkinter window
#         canvas.get_tk_widget().pack()
#
#         # creating the Matplotlib toolbar
#         toolbar = NavigationToolbar2Tk(canvas, window)
#         toolbar.update()
#
#         # placing toolbar on the Tkinter window
#         canvas.get_tk_widget().pack()
#
#
#     plot_gui = Tk()
#     plot_gui.title("Режим построения графика функции")  # устанавливаем заголовок окна
#     plot_gui.geometry("375x250")  # устанавливаем размеры окна
#
#     label1 = ttk.Label(plot_gui, font=("Arial", 12), justify=CENTER, text="Вычислить:")
#     label2 = ttk.Label(plot_gui, font=("Arial", 12), justify=CENTER, text="Выберите действие:")
#
#     op = StringVar(plot_gui, value='+')
#
#     label_op = ttk.Label(plot_gui, font=("Arial", 12), justify=LEFT, textvariable=op)
#
#     entry_a = ttk.Entry(plot_gui)
#     entry_b = ttk.Entry(plot_gui)
#
#     solve_btn = ttk.Button(plot_gui, text="Найти", command=plot)
#     root_btn = ttk.Button(plot_gui, text="Меню", command=0)
#
#     op_div_btn      = ttk.Radiobutton(plot_gui, text="/", value="/", variable=op)
#     op_mult_btn     = ttk.Radiobutton(plot_gui, text="*", value="*", variable=op)
#     op_summ_btn     = ttk.Radiobutton(plot_gui, text="+", value="+", variable=op)
#     op_minus_btn    = ttk.Radiobutton(plot_gui, text="-", value="-", variable=op)
#
#     label1.place(x=150, y=15)
#
#     label_op.place(x=183, y=50)
#     entry_a.place(x=30, y=50)
#     entry_b.place(x=230, y=50)
#
#     solve_btn.place(x=250, y=130)
#     root_btn.place(x=10, y=10)
#
#     label2.place(x=120, y=75)
#     op_div_btn.place(x=50, y=100)
#     op_mult_btn.place(x=135, y=100)
#     op_summ_btn.place(x=215, y=100)
#     op_minus_btn.place(x=295, y=100)
#

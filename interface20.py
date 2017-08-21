# -*- coding: utf-8 -*-
"""
tkinter - библиотека с функциями для построения простого интерфейса.
	ttk - расширение библиотеки tkinter, улучшающая графику;
"""


import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from metod_vrasheniya20 import jacobi1
from LU_decomp import lu


TITLE_FONT = ("Helvetica", 18, "bold")
DOP_FONT = ("Consolas",15,"bold")
DOP_FONT2 = ("Arial",13,"bold")


class SampleApp(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # контейнер в котором мы храним наши фреймы
        # по порядку
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, FirstMethod, SecondMethod):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        """ Вызывает страницу по переданому названию """
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):
    """ Страница основного меню """


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Меню", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        str_inf = "Курсовой проект\n Разработчик : Соловых А.В \n Группа : ТМП62\n Задание: Разработка программы решения системы линейных уравнений:\n -метод вращения(метод якоби) \n -метод LU разложения матриц"
        label2 = tk.Label(self, text=str_inf,font=DOP_FONT)
        label2.place(x=40, y=340)
        label11 = tk.Label(self, text="Выберите нужный метод:",font=DOP_FONT2)
        label11.pack()
        button1 = ttk.Button(self, text="Метод Якоби(вращения матриц)",
                             command=lambda: controller.show_frame("FirstMethod"))
        button2 = ttk.Button(self, text="Метод LU-разложение(на треугольные матрицы)",
                             command=lambda: controller.show_frame("SecondMethod"))
        button1.pack()
        button2.pack()


class FirstMethod(tk.Frame):
    """ Страница для метода якоби """


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Метод Якоби", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text='Вернуться в гланое меню',
                            command=lambda: controller.show_frame("MainMenu"))

        def jacobi_call():
            """ Построение интерфейса для ввода данных """
            n = v.get()
            for widget in self.winfo_children():
                if widget not in (
                button, n_ntr, button1, label, helping_label2, helping_label3, helping_label4, helping_label5):
                    widget.destroy()
            if (n != "") and (int(n) in range(2, 5)):
                n = int(n)
                arr_txt = [[0] * n for i in range(0, n)]
                arr_txt1 = [[0] for i in range(0, n)]
                for i in range(0, n):
                    # helping_label = tk.Label(self, text="x0+")
                    # helping_label.place(x=60, y=130 + i * 30, width=40, height=30)
                    for j in range(0, n):

                        if j != (n - 1):
                            helping_string = "x" + str(j) + "+"
                        elif j == (n - 1):
                            helping_string = "x" + str(j) + "="

                        helping_label = tk.Label(self, text=helping_string)
                        arr_txt[i][j] = tk.Entry(self)
                        helping_label.place(x=100 + j * 80, y=130 + i * 30, width=40, height=30)
                        arr_txt[i][j].place(x=60 + j * 80, y=130 + i * 30, width=40, height=30)
                    arr_txt1[i] = tk.Entry(self)
                    arr_txt1[i].place(x=60 + n * 80, y=130 + 30 * i, width=40, height=30)
                output = tk.Text(self, bg="lightblue", font="Arial 12")
                output.place(x=470, y=130, width=300, height=300)
                helping_label4.place(x=60, y=100)
                helping_label5.place(x=470, y=435)

                def inserter(value):
                    """ Функция вывода переданных значений """
                    value1 = ""
                    for i in range(0, len(value)):
                        value1 = value1 + "x" + str(i) + " = " + str(value[i]) + "\n" + "\n"

                    output.delete("0.0", "end")
                    output.insert("0.0", value1)

                def convert():
                    """ Получение значений и передача их функции """
                    arr_ntr = [[0] * n for i in range(0, n)]
                    arr_ntr1 = [[0] for i in range(0, n)]
                    for i in range(0, n):
                        for j in range(0, n):
                            arr_ntr[i][j] = float(arr_txt[i][j].get())
                        arr_ntr1[i] = float(arr_txt1[i].get())
                    print(*arr_ntr)
                    print(*arr_ntr1)
                    inserter(jacobi1(arr_ntr, arr_ntr1))

                btn3 = ttk.Button(self, text="Решить",
                                  command=convert)
                btn3.place(x=385, y=260, width=60, height=30)

            else:
                messagebox.showinfo("Razmernost", "Viberite razmernost: 2 - 4")

        button1 = ttk.Button(self, text="ok",
                             command=jacobi_call)  # lambda: messagebox.showinfo("Razmernost", "Viberite razmernost: 2 - 4"))
        v = tk.StringVar(self)
        v.set('2')
        n_ntr = ttk.OptionMenu(self, v, '2', '2', '3', '4')  # tk.Entry(self, width=3) #sdelat combobox i kopitrnut
        button.place(x=550, y=20)
        n_ntr.place(x=330, y=50)
        button1.place(x=370, y=48)
        dop_infa = "Метод Якоби — разновидность метода простой итерации \nдля решения системы линейных алгебраических уравнений.\n Назван в честь Карла Густава Якоби.\nПри большом числе неизвестных метод Гаусса \nстановится весьма сложным в плане вычислительных и временных затрат. \nПоэтому иногда удобнее использовать приближенные (итерационные) \nчисленные методы, метод Якоби относится к таким."
        helping_label2 = tk.Label(self, text="Выберите размерность матрицы и нажмите ОК")
        helping_label2.place(x=60, y=50)
        helping_label3 = tk.Label(self, text=dop_infa)  # TODO: vnesti infu
        helping_label3.place(x=30, y=400)
        helping_label4 = tk.Label(self, text="Введите коэффициенты уравнений ниже:")

        helping_label5 = tk.Label(self, text="""Окно вывода результатов.\nВ случае если ничего не выводится - коэффициенты\nзаданы не правильно\nлибо невозможно найти корни.""")

        def destroy():
            for widget in self.winfo_children():
                if widget not in (button, n_ntr, button1, button2, label):
                    widget.destroy()

                    # button2 = ttk.Button(self, text="Clear this page",
                #                     command=destroy)
                # button2.place(x=500, y=100)


class SecondMethod(tk.Frame):
    """ Страница метод LU-разложения """


    def __init__(self, parent, controller):
        # self.destroy()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="LU декомпозиция", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Вернуться в гланое меню",
                            command=lambda: controller.show_frame("MainMenu"))

        def lu_call():
            """ Построение интерфейса для ввода данных """
            n = v.get()
            for widget in self.winfo_children():
                if widget not in (
                button, n_ntr, button1, label, helping_label2, helping_label3, helping_label4, helping_label5):
                    widget.destroy()
            if (n != "") and (int(n) in range(2, 6)):
                n = int(n)
                arr_txt = [[0] * n for i in range(n)]
                # arr_txt1 = [[0] * n for i in range(n)]
                arr_ntr = [[0] * n for i in range(n)]
                # arr_ntr1 = [[0] * n for i in range(n)]
                # messagebox.showinfo("Razmernost", "ok")
                for i in range(0, n):
                    for j in range(0, n):
                        arr_txt[i][j] = tk.Entry(self)
                        arr_txt[i][j].place(x=100 + j * 50, y=150 + i * 30, width=40, height=30)
                    # arr_txt1[i] = tk.Entry(self)
                    # arr_txt1[i].place(x=100+n*50, y=100+30*i, width=40, height=30)
                output = tk.Text(self, bg="lightblue", font="Arial 8")
                output.place(x=450, y=150, width=300, height=300)
                helping_label4.place(x=60, y=100)
                helping_label5.place(x=450, y=455)

                def inserter2(value, value2):
                    """ Функция вывода переданных значений """
                    output.delete("0.0", "end")
                    value = "U = \n" + str(value) + " \n \n"
                    value2 = "L = \n" + str(value2)
                    output.insert("0.0", value)
                    output.insert("16.0", value2)

                def convert():
                    """ Получение значений и передача их функции """
                    for i in range(0, n):
                        for j in range(0, n):
                            arr_ntr[i][j] = float(arr_txt[i][j].get())
                        # arr_ntr1[i] = float(arr_txt1[i].get())
                    L, U = lu(arr_ntr)
                    inserter2(L, U)

                btn3 = ttk.Button(self, text="Решить",
                                  command=convert)
                btn3.place(x=385, y=310, width=60, height=30)

            else:
                messagebox.showinfo("Razmernost", "Viberite razmernost: 2 - 7")

        button1 = ttk.Button(self, text="ok",
                             command=lu_call)  # lambda: messagebox.showinfo("Razmernost", "Viberite razmernost: 2 - 4"))
        v = tk.StringVar(self)
        v.set('2')
        n_ntr = ttk.OptionMenu(self, v, '2', '2', '3', '4', '5')
        button.place(x=550, y=20)
        n_ntr.place(x=330, y=50)
        button1.place(x=370, y=48)
        helping_label2 = tk.Label(self, text="Выберите размерность матрицы и нажмите ОК")
        helping_label2.place(x=60, y=50)
        helping_label4 = tk.Label(self, text="Введите элементы матриц в поля ввода:")

        dop_infa = "LU-разложение (LU-декомпозиция, LU-факторизация) — представление \nматрицы A в виде произведения двух матриц, A=LU, \nгде L — нижняя треугольная матрица, \nа U — верхняя треугольная матрица. \nLU-разложение используется для решения \nсистем линейных уравнений, \nобращения матриц и вычисления определителя.\nЭтот метод является одной из разновидностей метода Гаусса."

        helping_label3 = tk.Label(self, text=dop_infa)  # TODO: vnesti infu
        helping_label3.place(x=10, y=400)
        helping_label5 = tk.Label(self, text="""Окно вывода результатов.\nВ случае если ничего не выводится - элементы\nматрицы заданы не правильно\nлибо невозможно найти решения.""")

        def destroy():
            for widget in self.winfo_children():
                if widget not in (button, n_ntr, button1, button2, label):
                    widget.destroy()

                    # button2 = ttk.Button(self, text="Clear this page",
                #                     command=destroy)
                # button2.place(x=450, y=100)


if __name__ == "__main__":
    app = SampleApp()
    app.minsize(800, 600)
    app.maxsize(800, 600)
    app.mainloop()

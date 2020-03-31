import subprocess
import psutil
import time
from tkinter import *
from tkinter import messagebox


all_processes = []

# Класс можно свернуть
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Консольный месенджер v0.02 pre-alpha")
        self.parent.geometry()

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        button_s = Button(
            self,
            text="Запустить сервер и клиенты",
            background="#737A61",
            foreground="#fff",
            padx="20",
            pady="8",
            font="16",
            height=2,
            width=40,
            border=8,
            command=click_s)
        button_s.grid(row=2, column=0)
        
        button_x = Button(
            self,
            text="Закрыть все окна",
            background="#7C7863",
            foreground="#fff",
            padx="20",
            pady="8",
            font="16",
            height=2,
            width=40,
            border=8,
            command=click_x)
        button_x.grid(row=3, column=0)

        button_q = Button(
            self,
            text="Выход",
            background="#7C6D63",
            foreground="#fff",
            padx="20",
            pady="8",
            font="16",
            height=2,
            width=40,
            border= 8,
            command=click_q)
        button_q.grid(row=4, column=0)

        button_c = Button(
            self,
            text="Комментарий для Дмитрия",
            background="#555",
            foreground="#fff",
            padx="20",
            pady="8",
            font="16",
            height=2,
            width=40,
            border=8,
            command=click_с)
        button_c.grid(row=5, column=0)

        self.pack()


# s - запустить сервер и клиенты
def click_s():
    all_processes.append(
        subprocess.Popen(
            'python hw_3_1_server.py',
            creationflags=subprocess.CREATE_NEW_CONSOLE))
    time.sleep(0.1)
    all_processes.append(
        subprocess.Popen(
            'python hw_3_1_client.py -n cl_1',
            creationflags=subprocess.CREATE_NEW_CONSOLE))
    time.sleep(0.1)
    all_processes.append(
        subprocess.Popen(
            'python hw_3_1_client.py -n cl_2',
            creationflags=subprocess.CREATE_NEW_CONSOLE))
    time.sleep(0.1)
    all_processes.append(
        subprocess.Popen(
            'python hw_3_1_client.py -n cl_3',
            creationflags=subprocess.CREATE_NEW_CONSOLE))

    print(all_processes)


# x - закрыть все окна
def click_x():
    # останавливается процесс /bin/sh, процессы клиентов и сервера продолжают
    # работать (**доработать**)
    for p in all_processes:
        main_process = psutil.Process(p.pid)
        print(print(p.pid), main_process)
        for child_process in main_process.children(recursive=True):
            child_process.terminate()

    all_processes.clear()
    print(all_processes)


# q - выход
def click_q():
    quit()


def click_с():
    messagebox.showinfo('Комментарий по ДЗ и по курсу',
                        'В этом ДЗ я сильно изменил клиент и сервер. '
                        'Вычистил лишний мусор и прокоментировал все для себя: для своей библиотеки и репозитория.\n'
                        'И сделал крутой лаунчер =)\n\n'
                        'Ваш курс - один из лучших курсов на всём GeekBrains. '
                        'Настолько подробно еще никто не рассказывал. \n'
                        'Богатая библиотека дополнительных материалов, коды примеров, '
                        'примеры практических заданий ... \n'
                        'Все это сделало обучение на Вашем курсе, как по маслу. \n'
                        '\n'
                        'Без всего этого я врятли смог догнать курс с 6 марта, который начался аж 17 февраля.\n'
                        'Спасибо Вам за то, что были моим преподавателем. Благодаря Вам и Вашим дополнительным '
                        'материалам, мне начало нравиться кодить.\n'
                        '\n'
                        'Я приобрел себе электронную книгу, создал там объемную библиотеку по Python.\n'
                        'Я зарегистрировался на сайтах, таких как https://ru.stackoverflow.com/, '
                        'https://www.cyberforum.ru/ и еще нескольких.\n'
                        'Я начал очень активно пользоваться github.\n'
                        'Я даже посетил хакатон) Но моих навыков хватило, чтобы просто наблюдать...'
                        '\n\n'
                        'Еще раз огромное Вам спасибо! За всё!')


def main():
    root = Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()

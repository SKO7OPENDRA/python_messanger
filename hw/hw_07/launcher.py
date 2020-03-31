import subprocess
import psutil
import time
from tkinter import *


all_processes = []

# Класс можно свернуть
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Консольный месенджер v0.02 pre-alpha")
        self.parent.geometry("400x190")

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)

        button_s = Button(
            self,
            text="Запустить сервер и клиенты",
            background="#555",
            foreground="#ccc",
            padx="20",
            pady="8",
            font="16",
            height=2,
            width=40,
            command=click_s)
        button_s.grid(row=2, column=0)
        button_x = Button(
            self,
            text="Закрыть все окна",
            background="#555",
            foreground="#ccc",
            padx="20",
            pady="8",
            font="16",
            height=2,
            width=40,
            command=click_x)
        button_x.grid(row=3, column=0)
        button_q = Button(
            self,
            text="Выход",
            background="#555",
            foreground="#ccc",
            padx="20",
            pady="8",
            font="16",
            height=2,
            width=40,
            command=click_q)
        button_q.grid(row=4, column=0)

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


def main():
    root = Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()

import tkinter as tk

__version__ = "1.0b"
PROGRAM_NAME = "Quaero! 3.0::Блокнот"

def About():
    window = tk.Toplevel()
    window.focus_force()
    window.title("О программе")
    window.overrideredirect(0)
    window.geometry("400x300+150+150")
    my_string = tk.StringVar(window)
    my_string.set("{}, версия {}".format(PROGRAM_NAME, __version__))
    label = tk.Label(window, textvariable=my_string)
    label.configure(font = "Tahoma 13", relief='groove', cursor='watch')
    label.pack()

    tk.Button(window, text="ОК", command=window.destroy).place(x=200, y=150)
    window.bind("<Escape>", lambda x: window.destroy())


def Help():
    window = tk.Toplevel()
    window.focus_force()
    window.title("Справка")
    window.overrideredirect(0)
    window.geometry("400x300+150+150")
    my_string = tk.StringVar(window)
    my_string.set("{}, версия {}".format(PROGRAM_NAME, __version__))
    help_text = tk.Text(window, wrap='word')
    help_text.insert(1.0, my_string.get())
    help_text.configure(font = "Tahoma 13", relief='groove', cursor='arrow')
    help_text.pack()
    help_text.configure(state=tk.DISABLED)

    tk.Button(window, text="ОК", command=window.destroy).place(x=200, y=150)
    window.bind("<Escape>", lambda x: window.destroy())
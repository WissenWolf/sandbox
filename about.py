import tkinter as tk

def About():
    window = tk.Toplevel()
    window.focus_force()
    window.title("О программе")
    window.overrideredirect(0)
    window.geometry("400x300+150+150")
    my_string = tk.StringVar(window)
    my_string.set("Quaero! 3.0 - автоматизированная \nсистема управления библиотекой")
    label = tk.Label(window, textvariable=my_string)
    label.configure(font = "Tahoma 13", relief='groove', cursor='watch')
    label.pack()

    # tk.Label(window, text="Quaero! 3.0 - автоматизированная \nсистема управления библиотекой").pack()
    tk.Button(window, text="ОК", command=window.destroy).place(x=200, y=150)
    window.bind("<Escape>", lambda x: window.destroy())
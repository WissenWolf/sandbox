import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import os
import about
from tooltip import ToolTip
# import toolbar

PROGRAM_NAME = "Quaero! 3::Блокнот"

root = tk.Tk()
root.geometry("600x450+200+100")
root.title(PROGRAM_NAME)
imgicon = tkinter.PhotoImage(file=r"icons\quaero.png")
root.call('wm', 'iconphoto', root._w, imgicon)

file_name = None
last_saved=True
last_key_system=False
toolbar_visible = True

def callback(event=None):
    pass
def show_toolbar(status):
    print(status)
    if status == 0:
        shortcut_bar.pack_forget()
    elif status == 1:
        shortcut_bar.pack(expand='no', fill='x') # todo заменить на grid

def not_saved(event):
    global last_saved, last_key_system
    print (event)
    if event.keycode < 30:
        last_key_system=True
        print("Это не считается")
    elif event.keycode >= 30:
        if last_key_system:
            last_key_system=False
            pass
        else:
            last_key_system = False
    # elif event.key
            last_saved=False
    print (last_saved)

def new_file(event=None):
    global file_name
    file_name = None
    content_text.delete(1.0, tk.END)
    content_text.edit_reset()
    root.title('{} :: {}'.format("Новый документ", PROGRAM_NAME))
    print("Начинаем новую жизнь с чистого листа")  # отладочная информация


def cut(event=None):
    content_text.event_generate("<<Cut>>")
    print("Выбран cut")


def copy(event=None):
    content_text.event_generate("<<Copy>>")
    print("Выбран copy")


def save(event=None):
    print("Выбран save")
    content_text.event_generate("<<Save>>")
    global file_name
    if not file_name:
        saveas()
    else:
        write_to_file(file_name)
    return "break"


def saveas(event=None):
    content_text.event_generate("<<SaveAs>>")
    print("Выбран save as")
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                           filetypes=[("Text Documents", "*.txt"),
                                                                      ("All Files", "*.*")])
    if input_file_name:
        global file_name
    file_name = input_file_name
    write_to_file(file_name)
    root.title('{} - {}'.format(os.path.basename(file_name),
                                PROGRAM_NAME))
    return "break"


def write_to_file(file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass
        # pass for now but we show some warning - we do this in next iteration


def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",
                                                         filetypes=[("Text Documents", "*.txt"),
                                                                    ("All Files", "*.*"), ])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} :: {}'.format(os.path.basename(file_name),
                                     PROGRAM_NAME))
        content_text.delete(1.0, tk.END)
        with open(file_name, encoding='utf-8') as _file:
            content_text.insert(1.0, _file.read())
    return 'break'


def paste(event=None):
    content_text.event_generate("<<Paste>>")
    print("Выбран paste")


def show_help(event):
    about.Help()


def show_about(event):
    about.About()


def redo(event=None):
    print("Выбран redo")
    content_text.event_generate("<<Redo>>")
    return 'break'

def undo(event=None):
    print("Выбран undo")
    content_text.event_generate("<<Undo>>")
    return 'break'


def select_all(event=None):
    content_text.tag_add('sel', '1.0', 'end')
    return "break"


def exit_editor(event=None):
    global last_saved
    if not last_saved:
        answer = tkinter.messagebox.askyesnocancel(title="документ не сохранён", message="Сохранить документ?")
        print (answer)
        if answer==True:
            if save():
                root.destroy()
            else:
                return 'break'
        elif answer==False:
            root.destroy()
        elif answer==None:
            return 'break'
    else:
        root.destroy()
    #     root.destroy()


def find_text(event=None):
    print("Найди то, не знаю что...")

    search_toplevel = tk.Toplevel(root)

    search_toplevel.title('Find Text')
    search_toplevel.transient(root)
    search_toplevel.resizable(False, False)
    tk.Label(search_toplevel, text="Find All:").grid(row=0, column=0,
                                                     sticky='e')
    search_entry_widget = tk.Entry(search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2,
                             sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = tk.IntVar()
    ignore_case_value.set(1)
    tk.Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(
        row=1, column=1, sticky='e', padx=2, pady=2)
    tk.Button(search_toplevel, text="Find All", underline=0,
              command=lambda: search_output(search_entry_widget.get(),
                                            ignore_case_value.get(), content_text, search_toplevel,
                                            search_entry_widget)).grid(row=0, column=2, sticky='e' + 'w', padx=2,
                                                                       pady=2)

    def close_search_window():
        content_text.tag_remove('match', '1.0', tk.END)

        search_toplevel.destroy()

    search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
    return "break"


def search_output(needle, if_ignore_case, content_text, search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', tk.END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos,
                                            nocase=if_ignore_case, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
            content_text.tag_config('match', foreground='red', background='yellow')
            search_box.focus_set()
            search_toplevel.title('{} matches found'.format(matches_found))


# блок меню
main_menu = tk.Menu(root)

file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новый", accelerator="Ctrl + N", compound='left', command=new_file)
file_menu.add_command(label="Открыть", accelerator="Ctrl + O", compound='left', command=open_file)
file_menu.add_command(label="Сохранить", accelerator="Ctrl + S", compound='left', command=save)
file_menu.add_command(label="Сохранить как", accelerator="Ctrl + Shift + S", compound='left', command=saveas)
file_menu.add_command(label="Выйти", accelerator="Ctrl + Q", compound='left', command=lambda: exit_editor())

edit_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Правка", menu=edit_menu)
edit_menu.add_command(label="Undo", accelerator="Ctrl + Z", compound='left', command=callback)
edit_menu.add_command(label="Redo", accelerator="Ctrl + Y", compound='left', command=callback)
edit_menu.add_command(label="Cut", accelerator="Ctrl + X", compound='left', command=cut)
edit_menu.add_command(label="Copy", accelerator="Ctrl + C", compound='left', command=copy)
edit_menu.add_command(label="Paste", accelerator="Ctrl + V", compound='left', command=paste)
edit_menu.add_command(label="Выделить всё", accelerator="Ctrl + A", compound='left', command=select_all)
edit_menu.add_command(label="Искать", accelerator="Ctrl+F", compound='left', command=find_text)

view_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Вид", menu=view_menu)
view_menu.add_checkbutton(label="Показывать номера строк", variable=None)

show_toolbar_var = tk.IntVar()
show_toolbar_var.set(1)
view_menu.add_checkbutton(label="Показывать тулбар", variable=show_toolbar_var, command=lambda : show_toolbar(show_toolbar_var.get()))
view_menu.add_checkbutton(label="Строка состояния", variable=None)
view_menu.add_command(label="Настройки", compound='left', command=callback)

theme_name = tk.StringVar()
themes_menu = tk.Menu(view_menu)
view_menu.add_cascade(label="Themes", menu=themes_menu)
themes_menu.add_radiobutton(label="Default", variable=theme_name)
themes_menu.add_radiobutton(label="Darkula", variable=theme_name)

about_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Помощь", menu=about_menu)
about_menu.add_command(label="Помощь", accelerator="F1", compound='left', command=about.Help)
about_menu.add_command(label="О программе", compound='left', command=about.About)

root.config(menu=main_menu)
root.protocol('WM_DELETE_WINDOW', exit_editor)
# end блок меню

# toolbar
shortcut_bar = tk.Frame(root, height=25, background='light sea green')

icons = ('new_file', 'open_file', 'save', 'cut', 'copy', 'paste', 'undo', 'redo', 'find_text')
tips  = ("новый документ", "открыть", "сохранить", "вырезать", "скопировать", "вставить", "отменить", "вернуть", "искать")

for i, icon in enumerate(icons):
    tool_bar_icon = tkinter.PhotoImage(file='icons/{}.gif'.format(icon))

    cmd = eval(icon)
    tool_bar = tk.Button(shortcut_bar, image=tool_bar_icon, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side='left')
    ToolTip(tool_bar, text=tips[i])

shortcut_bar.pack(expand='no', fill='x')
# end toolbar


root.bind("<Control-N>", lambda x: new_file())
root.bind("<Control-n>", lambda x: new_file())
root.bind("<Control-q>", lambda x: exit_editor())
root.bind("<Control-Q>", lambda x: exit_editor())
root.bind("<Control-O>", lambda x: open_file())
root.bind("<Control-o>", lambda x: open_file())
root.bind("<Control-S>", lambda x: save())
root.bind("<Control-s>", lambda x: save())
root.bind("<Control-Shift-S>", lambda x: saveas())
root.bind("<Control-Shift-KeyPress-s>", lambda x: saveas())
# root.bind("<Control-Shift-KeyPress-83>", lambda x: saveas())
# root.bind("<Key>", lambda x: print(x))

root.bind_all('<F1>', show_help)

content_text = tk.Text(root, wrap='word', undo=1, maxundo=6) # @todo перенести maxundo в настройки
content_text.pack(expand='yes', fill='both')
content_text.focus_set()
scroll_bar = tk.Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

content_text.bind('<Control-y>', redo)  # handling Ctrl + smallcase y
content_text.bind('<Control-Y>', redo)  # handling Ctrl + uppercase y
content_text.bind('<Control-A>', select_all)
content_text.bind('<Control-a>', select_all)
content_text.bind('<Control-x>', cut)
content_text.bind('<Control-c>', copy)
content_text.bind('<Control-v>', paste)
content_text.bind('<Control-f>', find_text)
content_text.bind('<Control-F>', find_text)
content_text.bind("<Key>", lambda x: not_saved(x))

tk.mainloop()

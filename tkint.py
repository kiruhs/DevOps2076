import tkinter as tk
from codecs import ignore_errors
from tkinter import ttk
from tkinter.constants import RIGHT, LEFT, TOP, BOTTOM, DISABLED, ACTIVE, BOTH
from time import sleep

from sqlalchemy.log import rootlogger

# print(tkinter.Tcl().eval("info patchlevel"))

# window = tk.Tk()
# window.title("App in Tkinter")
# window.attributes("-fullscreen", True)
# window.attributes("-alpha", 0.7) # transparency
# window.attributes("-toolwindow", True)
# window.geometry("400x250+600+250")
# window.resizable(False, False)
# window.minsize(150,100)
# window.maxsize(600, 350)
# window.iconbitmap(default="drill.ico")
# label = tk.Label(window, text="Hello DevOps!", bg='lightblue', height=5, width=30, relief=tk.RAISED, font=("Arial", 10, "bold"))
# label.grid(row=1, column=3, columnspan=3, pady=20)
# clicks = 0
# def click_button():
#     global clicks
#     clicks += 1
#     label['text'] = f"Clicks: {clicks}"
#     if clicks > 4:
#         btn['state'] = ACTIVE
#     if clicks >=8:
#         # label.destroy()
#         window.quit()


# btn1 = tk.Button(text="Right", command=click_button)
# # btn1.pack(side=RIGHT)
# btn1.place(relx=0.8, rely=0.8, anchor='nw', width=50, height=30) #, relwidth=0.13, relheight=0.08)
# btn2 = tk.Button(text="Left", command=click_button, state=DISABLED)
# btn2.pack(side=LEFT)
# btn = tk.Button(text='Spanned', command=click_button)
# btn.grid(row=3, column=0, columnspan=3, ipadx=15, ipady=5, sticky="WE")
# window.mainloop()

# Button on parent window closes the child window
# parent = tk.Tk()
# parent.title("Parent button")
# parent.geometry("+100+200")
# child = tk.Toplevel(parent)
# my_button = tk.Button(parent, text="Quit", height=3, width=40, command=child.destroy)
# my_button.pack()
# child.title("Child button")
# child.geometry("+400+300")
# parent.mainloop()

# parent = tk.Tk()
# parent.title("Parent button")
# parent.geometry("+100+200")
# child = tk.Toplevel(parent)
# child.title("Child button")
# child.geometry("+400+300")
#
# def add_label():
#     my_label = tk.Label(parent, text="I'm a result of child button click")
#     my_label.pack()
#     my_entry = tk.Entry(parent)
#     my_entry.pack()
#     def add_entered_text():
#         my_txt = my_entry.get()
#         entered_text = tk.Label(child, text=my_txt)
#         entered_text.pack()
#     entry_button = tk.Button(parent, text="Enter", height=1, width=50, command=add_entered_text)
#     entry_button.pack()
# my_button = tk.Button(child, text="Add label", height=1, width=50, command=add_label, bg='green')
# my_button.pack()
# exit_button = tk.Button(parent, text="Quit", height=1, width=50, command=child.destroy)
# exit_button.pack()
# parent.mainloop()
# child.mainloop()

# combobox exists in ttk only, not presented in tk

# root = tk.Tk()
# root.geometry("200x100")
# my_str_var = tk.StringVar()
# my_combobox = ttk.Combobox(root, textvariable=my_str_var, values=["Java", "Linux", "Python"])
# my_combobox.pack()
# def selected(event):
#     selection = my_combobox.get()
#     label["text"] = f"You choose {selection}"
#
# label = tk.Label()
# label.pack()
# my_combobox.bind("<<ComboboxSelected>>", selected)
#
# root.mainloop()

# resize font according to window size

# def resize_font(event):
#     width = event.width
#     height = event.height
#     # font_size = int(min(width,height)/10)
#     font_size = int((width**2 + height**2) ** 0.5 / 15)
#     label.config(font=("Helvetica", font_size))
#
# root = tk.Tk()
# root.title("Dynamic font resize")
# root.geometry("300x150")
# label = tk.Label(root, text="Resize the window!", font=("Helvetica", 30))
# label.pack(expand=True, fill=tk.BOTH)
# root.bind("<Configure>", resize_font)
# root.mainloop()

# Button resize
# root = tk.Tk()
# root.title("Dynamic button resize")
# root.geometry("300x150")
# button = tk.Button(root, text="Resize Me", bg="yellow")
# button.grid(row=0, column=0, sticky="nsew")
# root.grid_rowconfigure(0,weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.mainloop()

# resize button text
# root = tk.Tk()
# root.title("Dynamic button resize")
# root.geometry("300x150")
# root.grid_rowconfigure(0,weight=1)
# root.grid_columnconfigure(0, weight=1)
#
# button = tk.Button(root, text="My Button")
# button.grid(row=0, column=0, sticky="nsew")
#
# def resize(e):
#     button.config(font=("Helvetica", e.height//10))
# root.bind("<Configure>", resize)
# root.mainloop()

# Checkbox
# root = tk.Tk()
# my_bool = tk.BooleanVar()
# my_checkbox = tk.Checkbutton(root, text="Check when this option is True", variable=my_bool)
# my_checkbox.pack()
# root.mainloop()

# spinbox
# root = tk.Tk()
# root.geometry("300x200")
# lbl = tk.Label(root, text="")
# def on_spinbox_change():
#     value = spinbox.get()
#     lbl['text'] = value
#     # print("Value changed to:", value)
#
# spinbox = tk.Spinbox(root, from_=0, to=100, increment=5, width=10, relief="sunken", font=("Arial", 12),repeatdelay=500, repeatinterval=100, bg="lightgrey", fg="blue", command=on_spinbox_change)
# spinbox.config(wrap=True, cursor="hand2", justify="center", bd=3, state="normal")
# lbl.pack()
# spinbox.pack()
# root.mainloop()

# root = tk.Tk()
# root.geometry("300x200")
# text_var = tk.DoubleVar()
# # lbl = tk.Label(root, text="")
#
# spinbox = tk.Spinbox(root, from_=0.6, to=50.0, increment=.1,
#                      textvariable=text_var, width=10, relief="sunken", font=("Arial", 12),
#                      repeatdelay=500, repeatinterval=50, bg="lightgrey", fg="blue")
# spinbox.config(wrap=True, cursor="hand2", justify="center", bd=3, state="normal")
# # lbl.pack()
# spinbox.pack()
# spinbox.pack(padx=20, pady=30)
# root.mainloop()

# root = tk.Tk()
# mytext = tk.Text(root)
# mytext.insert("1.0","- Python exercises, solutions -")
# mytext.insert("1.20", "practice, ")
# mytext.insert('end', "good work")
#
# mytext.insert("end", "\nit will a new line entry")
#
# mytext.delete("1.0", "1.2")
# mytext.delete("end - 6 chars", "end")
# mytext.pack()
# root.mainloop()

# Radio button
# root = tk.Tk()
# root.title("Radiobutton")
# root.geometry("350x200")
# selected = tk.StringVar()
# selected.set("1")
# radio1 = tk.Radiobutton(root, text="First", variable=selected, value=1)
# radio2 = tk.Radiobutton(root, text="Second", variable=selected, value=2)
# radio3 = tk.Radiobutton(root, text="Third", variable=selected, value=3)
# radio1.grid(column=0, row=0)
# radio2.grid(column=1, row=0)
# radio3.grid(column=2, row=0)
# root.mainloop()

# from tkinter import ttk

# root = tk.Tk()
# root.title("Pizza favorites")
# style = ttk.Style()
# style.theme_use('clam')
# style.configure("Treeview", background="green", foreground="white")
# style.configure("Treeview.Heading", background="grey", foreground="white")
# treeview = ttk.Treeview(root)
# treeview['columns'] = ("Name", "ID", "Pizza type")
# treeview.column("#0", width=20, )
# treeview.column("Name", width=120, anchor='center')
# treeview.column("ID", width=120, anchor='center')
# treeview.column("Pizza type", width=120, anchor='center')
# treeview.heading("#0", text="#")
# treeview.heading("Name", text="Name")
# treeview.heading("ID", text="ID")
# treeview.heading("Pizza type", text="Pizza type")
#
# treeview.insert("", "end", values=("John", 12345, "Peperoni"))
# treeview.insert("", "end", values=("Mary", 32145, "Margarita"))
#
# treeview.pack(padx=10, pady=10)
# root.mainloop()

# progress bar

# def update_prog():
#     new_value = prog_var.get()
#     new_value += 10
#     if new_value >= 100:
#         new_value = 0
#     prog_var.set(new_value)
#     root.after(1000, update_prog)
#
# root = tk.Tk()
# root.title("Progress bar example")
# prog_var = tk.DoubleVar()
# prog_bar = ttk.Progressbar(root, variable=prog_var, maximum=100)
# prog_bar.pack(padx=20, pady=20, fill='x')
#
# prog_but = tk.Button(root, text="progress", command=update_prog)
# prog_but.pack()
#
# root.mainloop()

# class CustomButton(tk.Button):
#     def __init__(self,master=None, **kwargs):
#         super().__init__(master, **kwargs)
#         self.config(relief=tk.FLAT, bd=5, padx=50, pady=20, font=("Arial", 20),
#                     foreground="white", background="blue", cursor="hand2")
#
#         self.bind("<Enter>", self.on_hover)
#         self.bind("<Leave>", self.on_leave)
#         self.bind("<Button-1>", self.on_click)
#
#     def on_hover(self, event):
#         self.config(background="grey")
#
#     def on_leave(self, event):
#         self.config(background="blue")
#
#     def on_click(self, event):
#         self.config(foreground="red")
#
# root = tk.Tk()
# root.title("My custom button")
# root.geometry("200x350")
# custom_button1 = CustomButton(root, text="My Button1")
# custom_button2 = CustomButton(root, text="My Button2")
# custom_button1.pack()
# custom_button2.pack()
# built_in_button = tk.Button(root, text="Built-in button")
# built_in_button.pack()
# root.mainloop()

from tkinter import filedialog, messagebox
import os
os.environ['LANG'] = 'en_US.UTF-8'

def new():
    print("New file")

def open_file():
    filepath = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if filepath:
        print(filepath)
        try:
            with open(filepath, encoding="utf-8", errors="ignore") as file:
                content = file.read()
                messagebox.showinfo("File content", content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file:\n {e}")
    else:
        messagebox.showwarning("No file selected")

def exit2():
    root.destroy()

# def show_menu(event=None):
#     # Получаем левый верхний угол окна
#     x = root.winfo_rootx()
#     y = root.winfo_rooty() + 30  # немного ниже верхней границы
#
#     # Показываем меню строго по левому краю окна
#     menu_bar.post(x, y)


root = tk.Tk()
root.title("Menu demonstration")
# root.geometry("600x400+0+0")
menu_bar = tk.Menu(root)
file = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file)
file.add_command(label="New", command=new)
file.add_command(label="Open", command=open_file)
file.add_command(label="Save", command=None)
file.add_command(label="Exit", command=exit2)

edit = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut", command=None, )
edit.add_command(label="Copy", command=None)
edit.add_command(label="Paste", command=None)
edit.add_command(label="Select All", command=None)
edit.add_separator()
edit.add_command(label="Find...", command=None)
edit.add_command(label="Find Again", command=None)

hlp = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=hlp)
hlp.add_command(label="Help", command=None, )


root.config(menu=menu_bar)
# root.bind("<Button-3>", show_menu)
root.mainloop()

# def update_size(val):
#     try:
#         new_font_size = int(float(val))
#         label.config(font=("Roboto", new_font_size))
#     except ValueError:
#         pass
#
# root = tk.Tk()
# root.title("Font size control")
# var = tk.StringVar()
# text = tk.Entry(root, textvariable=var)
# txt = text.get()
# text.pack()
# root.update()
# initial_font_size = 16
# label = tk.Label(root, text="Hello", font=("Roboto",initial_font_size))
# label.pack(pady=10)
#
# font_size_scaler = ttk.Scale(root, from_=10, to=36, orient="horizontal", length=200, command=update_size)
# font_size_scaler.set(16)
# font_size_scaler.pack(pady=10)
#
# root.mainloop()


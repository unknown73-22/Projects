import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.config(bg="#111111")

text_widget = tk.Text(root, bg="#444444", fg="#FFFFFF")
text_widget.pack(side="left", fill="both", expand=True)

def create_file():
    text_widget.delete("1.0", "end")

def save_file():
    if file_path is None:
        save_file_as()
    else:
        with open(file_path, "w") as file:
            file.write(text_widget.get("1.0", "end-1c"))

def save_file_as():
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, "w") as file:
        file.write(text_widget.get("1.0", "end-1c"))

def open_file():
    global file_path
    file_path = filedialog.askopenfilename()
    with open(file_path, "r") as file:
        text_widget.delete("1.0", "end")
        text_widget.insert("end", file.read())

menu_bar = tk.Menu(root, bg="#444444", fg="#FFFFFF")
file_menu = tk.Menu(menu_bar, tearoff=0, bg="#444444", fg="#FFFFFF")
file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
file_menu.add_command(label="Open", command=open_file)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

file_path = None

root.mainloop()

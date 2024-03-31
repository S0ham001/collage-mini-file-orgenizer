import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    path = entry_path.get()
    sort_method = var_sort_method.get()

    if not path:
        messagebox.showerror("mistake!", " I think you did not entered path. \n                    -or- \n The given path is not valid")

        return

    for filename in os.listdir(path):

        if os.path.isfile(os.path.join(path, filename)):

            filename, extension = os.path.splitext(filename)
            
            dest_folder = os.path.join(path, extension[1:])

            os.makedirs(dest_folder, exist_ok=True)

            shutil.move(os.path.join(path, filename + extension), os.path.join(dest_folder, filename + extension))

    messagebox.showinfo("complete", "Done!")
    exit()


root = tk.Tk()


root.title("File Organizer")

label_path = tk.Label(root, text="Path:")
label_path.grid(row=1, column=0)


entry_path = tk.Entry(root, width=40)

entry_path.grid(row=1, column=1)


button_browse = tk.Button(root, text="Browse", command=lambda: entry_path.insert(tk.END, filedialog.askdirectory()))

button_browse.grid(row=1, column=2)


label_sort_method = tk.Label(root, text="Sort type:")
label_sort_method.grid(row=2, column=0)


sort_methods = ["A-Z & 0-9", "By Date"]

var_sort_method = tk.StringVar(root)

var_sort_method.set(sort_methods[0])

option_sort_method = tk.OptionMenu(root, var_sort_method, *sort_methods)

option_sort_method.grid(row=2, column=1)

button_organize = tk.Button(root, text="sort", command=organize_files)

button_organize.grid(row=3, column=1)


root.mainloop()

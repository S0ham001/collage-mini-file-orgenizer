import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

def organize_files_by_name(path):

    def get_folder_name(filename):
        
        first_letter = filename[0].upper()
        
        if first_letter.isalpha():
            return first_letter
        
        else:
            return "Other"

    for filename in os.listdir(path):
        
        if os.path.isfile(os.path.join(path, filename)):
            
            dest_folder_name = get_folder_name(filename)
            dest_folder = os.path.join(path, dest_folder_name)

            os.makedirs(dest_folder, exist_ok=True)

            shutil.move(os.path.join(path, filename), os.path.join(dest_folder, filename))

def organize_files_by_extension(path):
    
    for filename in os.listdir(path):
        
        if os.path.isfile(os.path.join(path, filename)):

            filename, extension = os.path.splitext(filename)
            
            dest_folder = os.path.join(path, extension[1:])

            os.makedirs(dest_folder, exist_ok=True)

            shutil.move(os.path.join(path, filename + extension), os.path.join(dest_folder, filename + extension))

def organize_files_by_date(path):
    
    for filename in os.listdir(path):
    
        if os.path.isfile(os.path.join(path, filename)):
        
            mod_time = os.path.getmtime(os.path.join(path, filename))
            mod_date = datetime.fromtimestamp(mod_time)
            
            dest_folder_name = mod_date.strftime("%d-%m-%Y")
            
            dest_folder = os.path.join(path, dest_folder_name)

            os.makedirs(dest_folder, exist_ok=True)

            shutil.move(os.path.join(path, filename), os.path.join(dest_folder, filename))

def organize_files():
    path = entry_path.get()
    sort_method = var_sort_method.get()

    if not path:
        messagebox.showerror("Error!", "Please enter a valid path.")
        
        return

    if sort_method == "A-Z":
        
       
        organize_files_by_name(path)
    
    elif sort_method == "Extension":
    
        organize_files_by_extension(path)
    
    elif sort_method == "Date":
    
        organize_files_by_date(path)

    messagebox.showinfo("Complete", "Done!")
    
    
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

sort_methods = ["A-Z", "Extension", "Date"]
var_sort_method = tk.StringVar(root)
var_sort_method.set(sort_methods[1])

for i, method in enumerate(sort_methods):
    tk.Radiobutton(root, text=method, variable=var_sort_method, value=method).grid(row=2, column=i)

button_organize = tk.Button(root, text="Sort", command=organize_files)
button_organize.grid(row=3, column=1)

root.mainloop()

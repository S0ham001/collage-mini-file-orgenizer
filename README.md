# 🗂️ File Organizer GUI

A simple **Python GUI application** built using **Tkinter** that helps you organize files in a selected folder based on **file name**, **file extension**, or **modification date**.

---

## 🚀 Features

- **Organize by Name (A–Z):**  
  Moves files into folders based on the **first letter** of the filename.  
  Example:  
A/
B/
C/
Other/

vbnet
Copy code

- **Organize by Extension:**  
Groups files into folders based on their **file extensions**.  
Example:  
jpg/
png/
pdf/
txt/

vbnet
Copy code

- **Organize by Date:**  
Organizes files into folders named after their **last modified date (DD-MM-YYYY)**.  
Example:  
01-10-2025/
02-10-2025/

yaml
Copy code

---

## 🧠 How It Works

The script scans the specified directory, determines how to sort the files based on your selected option, and automatically creates destination folders to move them accordingly.

It uses:
- `os` → For file path operations  
- `shutil` → To move files  
- `datetime` → To format file modification dates  
- `tkinter` → For GUI and user interaction  

---

## 🖥️ User Interface

When you run the script, a simple window appears:

1. **Path Field:** Choose the folder you want to organize.  
2. **Browse Button:** Opens a dialog to select a directory.  
3. **Sort Type:** Choose between:
 - A-Z  
 - Extension  
 - Date  
4. **Sort Button:** Starts the organization process.

After completion, a message box appears showing **“Done!”**

---

## 🛠️ Installation

1. **Clone or Download** this repository:
 ```bash
 git clone https://github.com/your-username/file-organizer-gui.git
 cd file-organizer-gui
Install Python (if not already installed):

Download Python

Make sure python and pip are available in your PATH.

Run the Script:

bash
Copy code
python file_organizer.py

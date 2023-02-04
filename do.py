import tkinter as tk
from tkinter import filedialog, ttk

def select_files():
    files = filedialog.askopenfilenames(title = "Select files to process", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
    print(files)

def process_files():
    print("Processing selected files")

root = tk.Tk()
root.withdraw()

splash = tk.Toplevel()
splash.title("Welcome to the File Processor")

label = tk.Label(splash, text="File Processor", font=("TkDefaultFont", 20))
label.pack(pady=10)

select_files_button = tk.Button(splash, text = "Select Files", command = select_files)
select_files_button.pack(pady=10)

process_files_button = tk.Button(splash, text = "Process Files", command = process_files)
process_files_button.pack(pady=10)

options = ["Option 1", "Option 2", "Option 3"]
selected_option = tk.StringVar()
selected_option.set(options[0])

dropdown = ttk.OptionMenu(splash, selected_option, *options)
dropdown.pack(pady=10)

splash.mainloop()

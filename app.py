import tkinter as tk
from tkinter import ttk
from modules.module1 import Check_if_legal, get_attributes, get_data
#from functions import on_check_click, on_procede_click, show_attributes

def on_check_click():
    link = link_entry.get()
    legal_status = Check_if_legal(link)
    result_label.config(text=f"Legal to scrape: {legal_status}")
    if legal_status:
        procede_button.config(state=tk.NORMAL)
    else:
        procede_button.config(state=tk.DISABLED)

row__num_for_get_data = 10 # default 

def on_procede_click():
    attributes = get_attributes(link_entry.get())
    show_attributes(attributes)
    num_attributes = len(attributes)
    row__num_for_get_data += num_attributes//3

def show_attributes(attributes):
    for checkbox in checkboxes:
        checkbox.grid_forget()

    checkboxes.clear()
    for i, attr in enumerate(attributes):
        var = tk.IntVar()
        checkbox = tk.Checkbutton(root, text=attr, variable=var)
         #checkboxes.append(checkbox)
        checkboxes.append((checkbox, var))  # Storing both checkbox and its associated var
        checkbox.grid(row=i // 3 + 3, column=i % 3, sticky="w", padx=5, pady=2 )
        

def on_get_data_click(selected_format):
    link = link_entry.get()
    checked_attributes = [checkbox[0]['text'] for checkbox in checkboxes if checkbox[1].get() == 1]
    get_data(link, checked_attributes, selected_format)
       
# Create the main window
root = tk.Tk()
root.title("Data Harvester")

# Label and input field for the link
link_label = tk.Label(root, text="Paste the link of the webpage to scrape:")
link_label.grid(row=0, column=0, padx=5, pady=5)

link_entry = tk.Entry(root)
link_entry.grid(row=0, column=1, padx=5, pady=5)

# Button to check legality
check_button = tk.Button(root, text="Check", command=on_check_click)
check_button.grid(row=0, column=2, padx=5, pady=5)

# Label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=1, columnspan=3, padx=5, pady=5)

# Button to proceed
procede_button = tk.Button(root, text="Procede", command=on_procede_click, state=tk.DISABLED)
procede_button.grid(row=2, columnspan=3, padx=5, pady=5)

# Checkboxes for attributes
checkboxes = []

# Create "Get Data" button and choose format dropdown
format_options = ['.csv', '.txt']
selected_format = tk.StringVar()
selected_format.set(format_options[0])  # Default format

choose_format_label = tk.Label(root, text="Choose format:")
choose_format_label.grid(row=row__num_for_get_data, column=0, padx=5, pady=5)

format_dropdown = ttk.Combobox(root, textvariable=selected_format, values=format_options)
format_dropdown.grid(row=row__num_for_get_data, column=1, columnspan=2, padx=5, pady=5)

get_data_button = tk.Button(root, text="Get Data", command=lambda: on_get_data_click(selected_format.get()))
get_data_button.grid(row=row__num_for_get_data+1, columnspan=3, padx=5, pady=(10, 5))

# Start the Tkinter event loop
root.mainloop()

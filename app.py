import tkinter as tk
from tkinter import ttk, filedialog
from modules.module1 import Check_if_legal, get_attributes, get_class_data, get_table, get_element
from modules.global_variables import Check_if_robot_txt_exists


def on_check_click():
    link = link_entry.get()
    robot_txt_result = Check_if_legal(link)
    
    if Check_if_robot_txt_exists:
        open_text_content(robot_txt_result, "robot.txt")
        Class_names_button.config(state=tk.NORMAL)
    else:
        result_label.config(text=f"{robot_txt_result}")
        Class_names_button.config(state=tk.NORMAL)

row__num_for_get_data = 10 # default 

def on_procede_click():
    attributes = get_attributes(link_entry.get())
    '''
    show_attributes(attributes)
    num_attributes = len(attributes)
    row__num_for_get_data += num_attributes//3
    '''
    show_attributes(attributes)

   

def on_get_data_click(selected_format):
    link = link_entry.get()
    checked_attributes = [checkbox[0]['text'] for checkbox in checkboxes if checkbox[1].get() == 1]
    result = get_class_data(link, checked_attributes)
    name = "Checked Attributes:" +   ", ".join(checked_attributes) 
    open_text_content(result, name)
    
def on_get_table_click(selected_format):
    link = link_entry.get()
    res = get_table(link,  selected_format)
    result_text.config(text= res)
    
def on_get_element_click():
    link = link_entry.get()
    element = element_entry.get()
    res = get_element(link,  element)
    name = "Result with element: "+ element
    open_text_content(res, name)
  
def open_text_content(data, title):
    new_window = tk.Toplevel(root)
    new_window.title(title)

    text_widget = tk.Text(new_window, wrap="word")
    text_widget.insert("1.0", data)

    scrollbar = tk.Scrollbar(new_window, command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)

    text_widget.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def show_attributes(attributes):
    # Create a new window for displaying attributes
    attribute_window = tk.Toplevel(root)
    attribute_window.title("Attributes")
    
    # Create a canvas to hold the checkboxes and add a scrollbar
    canvas = tk.Canvas(attribute_window)
    scrollbar = ttk.Scrollbar(attribute_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame to hold the checkboxes
    checkbox_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=checkbox_frame, anchor="nw")
    
    # Button and label before the list of checkboxes
    label_before_checkboxes = tk.Label(checkbox_frame, text="Choose chexboxes to get text content inside them", fg="blue")
    label_before_checkboxes.grid(row=0, column=0, padx=5, pady=2, sticky="w")
    button_before_checkboxes = tk.Button(checkbox_frame, text="Get content", command=lambda: on_get_data_click(selected_format.get()))
    button_before_checkboxes.grid(row=0, column=1, padx=5, pady=2, sticky="w")

    checkboxes.clear()
    for i, attr in enumerate(attributes):
        var = tk.IntVar()
        checkbox = tk.Checkbutton(checkbox_frame, text=attr, variable=var)
        checkboxes.append((checkbox, var))
        checkbox.grid(row=(i // 4) + 2, column=i % 4, sticky="w", padx=5, pady=2)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Set the canvas to expand with the window
    attribute_window.update()
    canvas.config(scrollregion=canvas.bbox("all"))

# Create the main window
root = tk.Tk()
root.title("Data Harvester")

link_label = tk.Label(root, text="Paste the link of the webpage to scrape:")
link_label.grid(row=0, column=0, padx=5, pady=5)

link_entry = tk.Entry(root)
link_entry.grid(row=0, column=1, padx=5, pady=5)

link_label = tk.Label(root, text="Check 'robot.txt' to know if the data is allowed to scrape ")
link_label.grid(row=1, column=0, padx=5, pady=5)

check_button = tk.Button(root, text="Check", command=on_check_click)
check_button.grid(row=1, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=2, columnspan=3, padx=5, pady=5)

class_label = tk.Label(root, text="Option 1.Text from elements with choosen classes")
class_label.grid(row=2, column=0, padx=5, pady=5)

Class_names_button = tk.Button(root, text="Get data ", command=on_procede_click, state=tk.NORMAL)
Class_names_button.grid(row=2, column =1, padx=5, pady=5)

checkboxes = []


format_options = ['.csv', '.txt', '.json']
selected_format = tk.StringVar()
selected_format.set(format_options[0])  # Default format

Element_label = tk.Label(root, text="Option 2. Get data within HTML element")
Element_label.grid(row=row__num_for_get_data, column=0, padx=5, pady=5)

element_entry = tk.Entry(root)
element_entry.grid(row=row__num_for_get_data, column=1, padx=5, pady=5)

get_Element_button = tk.Button(root, text="Get data", command=lambda: on_get_element_click())
get_Element_button.grid(row=row__num_for_get_data, column = 2, padx=5, pady=5)

choose_format_label = tk.Label(root, text="Option 3. Table. Choose format:")
choose_format_label.grid(row=row__num_for_get_data+1, column=0, padx=5, pady=5)

format_dropdown = ttk.Combobox(root, textvariable=selected_format, values=format_options)
format_dropdown.grid(row=row__num_for_get_data+1, column=1, padx=5, pady=5)

get_data_button = tk.Button(root, text="Get Tables", command=lambda: on_get_table_click(selected_format.get()))
get_data_button.grid(row=row__num_for_get_data+1, column = 2, padx=5, pady=5)


result_text = tk.Label(root,fg="blue", text="Result:")
result_text.grid(row=row__num_for_get_data+2, column=0, columnspan=2, rowspan=2, pady=10)

# Start the Tkinter 
root.mainloop()

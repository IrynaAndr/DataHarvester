import os
import csv
import requests
from bs4 import BeautifulSoup
from tkinter import filedialog

def generate_filename(url, file_format):
    domain_name = url.split('//')[-1].replace('/', '_').replace('.', '_')
    return f"{domain_name}_table_data{file_format}"

def save_csv_data(url, filename):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        table_data = []
        for row in soup.find_all('tr'):
            row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
            table_data.append(row_data)

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(table_data)
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        new_filepath = os.path.join(downloads_path, filename)
        os.rename(filename, new_filepath)
        return(f"File saved to: {new_filepath}")
    except Exception as e:
        return (f"An error occurred: {e}")

def save_txt_data(url, filename):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        #  Extract data from a table
        text_data = ""
        for row in soup.find_all('tr'):
            row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
            text_data += '\t'.join(row_data) + '\n'

        with open(filename, 'w', encoding='utf-8') as txtfile:
            txtfile.write(text_data)
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        new_filepath = os.path.join(downloads_path, filename)
        os.rename(filename, new_filepath)
        return(f"File saved to: {new_filepath}")
    except Exception as e:
        return (f"An error occurred: {e}")
    
''' Example 
url = "https://en.wikipedia.org/wiki/Table_(information)"
file_format = ".txt"  # or "txt"

# Generate the filename
filename = generate_filename(url, file_format)

# Choose the appropriate save function based on the file format
if file_format == ".csv":
    print(save_txt_data(url, filename))
elif file_format == ".txt":
    print(save_txt_data(url, filename))
'''





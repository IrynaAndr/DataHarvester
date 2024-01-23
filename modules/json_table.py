import os
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json

def get_class_names(url):
    try:
        
        response = requests.get(url)
        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table')
            if table:
                # Find all table rows (excluding the header row if applicable)
                rows = table.find_all('tr')[1:]  # Exclude header row if present

                # getting class names inside tr as 'key' for json 
                first_row = rows[0] if rows else None
                class_names = [cell['class'][0] for cell in first_row.find_all(['td', 'th'])] if first_row else []

                return class_names
            else:
                return 'Table not found on the page.'
        else:
            return f"Failed to retrieve the webpage. Status code: {response.status_code}"

    except requests.RequestException as e:
        return f"Error during request: {e}"

def save_data_to_json(url):
    try:

        class_names = get_class_names(url)

        if class_names:
            response = requests.get(url)
            if response.status_code == 200:
                
                soup = BeautifulSoup(response.text, 'html.parser')
                table = soup.find('table')
                if table:
                    data_list = []
                    rows = table.find_all('tr')[1:]  # Exclude header row if present
                    for row in rows:
                        
                        cells = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                        row_dict = dict(zip(class_names, cells))
                        data_list.append(row_dict)

                    url_parsed = urlparse(url)
                    filename = url_parsed.netloc + url_parsed.path.replace('/', '_') + '_table_data.json'
                    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

                    # Save the data to a JSON file with the derived filename in the Downloads folder
                    json_file_path = os.path.join(downloads_folder, filename)
                    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
                        json.dump(data_list, jsonfile, indent=2)

                    
                    return f'JSON file created successfully. Saved to: {json_file_path}'
                else:
                    return 'Table not found on the page.'
            else:
                return f"Failed to retrieve the webpage. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"



url = 'https://www.scrapethissite.com/pages/forms/'
#print(save_data_to_json(url))

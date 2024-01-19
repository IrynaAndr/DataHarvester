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

                # Extract class names from the first row
                first_row = rows[0] if rows else None
                class_names = [cell['class'][0] for cell in first_row.find_all(['td', 'th'])] if first_row else []

                return class_names
            else:
                print('Table not found on the page.')
                return 'Table not found on the page.'
        else:
            msg = f"Failed to retrieve the webpage. Status code: {response.status_code}"
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return msg

    except requests.RequestException as e:
        msg = f"Error during request: {e}"
        return msg

def save_data_to_json(url):
    try:

        class_names = get_class_names(url)

        if class_names:
            # Send a GET request to the URL
            response = requests.get(url)

            if response.status_code == 200:
                
                soup = BeautifulSoup(response.text, 'html.parser')
                table = soup.find('table')
                if table:
                    # Initialize a list to store dictionaries for each row
                    data_list = []

                    # Find all table rows (excluding the header row if applicable)
                    rows = table.find_all('tr')[1:]  # Exclude header row if present

                    # Iterate through rows and extract data
                    for row in rows:
                        # Extract text from each cell in the row
                        cells = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]

                        # Create a dictionary for the row
                        row_dict = dict(zip(class_names, cells))

                        # Append the row dictionary to the list
                        data_list.append(row_dict)

                    # Extract the filename from the URL
                    url_parsed = urlparse(url)
                    filename = url_parsed.netloc + url_parsed.path.replace('/', '_') + '_table_data.json'

                    # Get the path to the Downloads folder
                    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

                    # Save the data to a JSON file with the derived filename in the Downloads folder
                    json_file_path = os.path.join(downloads_folder, filename)
                    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
                        json.dump(data_list, jsonfile, indent=2)

                    msg = f'JSON file created successfully. Saved to: {json_file_path}'
                    return msg
                else:
                    msg = 'Table not found on the page.'
                    return msg
            else:
                msg = f"Failed to retrieve the webpage. Status code: {response.status_code}"
                return msg
    except Exception as e:
        msg = f"An error occurred: {e}"
        return msg

# Replace this URL with the actual URL of the webpage containing the table
url = 'https://en.wikipedia.org/wiki/Table_(information)'

# Call the function to save data to JSON
#print(save_data_to_json(url))
save_data_to_json(url)
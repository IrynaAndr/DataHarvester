import requests
from bs4 import BeautifulSoup

def get_text_from_element(url, element_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            elements_with_tag = soup.find_all(element_name)
            text_content_list = [' '.join(element.stripped_strings) for element in elements_with_tag]
            return text_content_list
        else:
            return(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            
    except requests.RequestException as e:
        return(f"Error during request: {e}")
        
'''
url = 'https://en.tutiempo.net/climate/1959/ws-783670.html'

# ('p', 'div', 'span', etc.)
element_name_to_extract = 'p'

text_content_list = get_text_from_element(url, element_name_to_extract)
if text_content_list:
    print(f'Text content of elements with tag name "{element_name_to_extract}":')
    for text_content in text_content_list:
        print(text_content)
'''

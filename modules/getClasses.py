import requests
from bs4 import BeautifulSoup

def get_all_class_names(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all elements with a class attribute
            elements_with_class = soup.find_all(class_=True)


            class_names = [class_name for element in elements_with_class for class_name in element['class']]
            class_names = list(set(class_names))

            return class_names
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return None
    
def get_text_from_classes(url, class_names_list):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            result_dict = {}

            for class_name in class_names_list:
                elements_with_class = soup.find_all(class_=class_name)
                text_content_list = [' '.join(element.stripped_strings) for element in elements_with_class]
                result_dict[class_name] = text_content_list

            return result_dict
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return None
    
def dict_to_text(dict):
    all_text_content = ""
    for class_name, text_content_list in dict.items():
        all_text_content += f"Text from elements with class '{class_name}':\n"
        for i, text_content in enumerate(text_content_list):
            all_text_content += f"  Element {i + 1}: {text_content}\n"

    return all_text_content  

'''
url = "https://en.tutiempo.net/climate/1959/ws-783670.html"
class_names_list = ["medias", "cf"]
result = get_text_from_classes(url, class_names_list)
print(dict_to_text(result))
'''

'''
url = "https://en.tutiempo.net/climate/1959/ws-783670.html"
class_names_list = ["medias", "cf"]
result = get_text_from_classes(url, class_names_list)

if result is not None:
    for class_name, text_content_list in result.items():
        print(f"Text from elements with class '{class_name}':")
        for i, text_content in enumerate(text_content_list):
            print(f"  Element {i + 1}: {text_content}")
else:
    print("Failed to retrieve text content.")
'''
    





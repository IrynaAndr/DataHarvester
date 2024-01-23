from modules.json_table import save_data_to_json
from modules.csv_txt_table import generate_filename, save_csv_data, save_txt_data
from modules.check_safety import get_robots_txt
from modules.getClasses import get_all_class_names, get_text_from_classes, dict_to_text
from modules.get_data_in_element import get_text_from_element

def Check_if_legal(link):
    return(get_robots_txt(link))

def get_attributes(link):
    class_names = get_all_class_names(link)
    return class_names
    
    
def get_class_data(link, checked_attributes):
    #print("Link:", link)
    #print("Checked Attributes:", checked_attributes)
    result = get_text_from_classes(link, checked_attributes)

    if result is not None:
        return dict_to_text(result)
    else:
        return("Failed to retrieve text content.")
        
def get_table(link, selected_format):
    print("Link:", link)
    print("Selected Format:", selected_format)
    filename = generate_filename(link, selected_format)
    if selected_format == '.csv':
        return(save_csv_data(link, filename))
       
    elif selected_format == '.json':
        return save_data_to_json(link)
    else:
        return(save_txt_data(link, filename))
        
def get_element(link, element):
    text_content_list = get_text_from_element(link, element)
    all_text_content = ""
    if text_content_list:
        for text_content in text_content_list:
            all_text_content += text_content + '\n' 
    return all_text_content

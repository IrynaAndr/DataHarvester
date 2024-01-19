import requests
from urllib.parse import urlparse, urlunparse
from modules.global_variables import Check_if_robot_txt_exists

def get_base_url(url):
    parsed_url = urlparse(url)

    # Extract the scheme, netloc, and path
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc
    path = parsed_url.path

    # Reconstruct the URL with only the scheme and netloc
    base_url = urlunparse((scheme, netloc, '', '', '', ''))

    return base_url

def change_variable_value(new_value):
    global Check_if_robot_txt_exists
    Check_if_robot_txt_exists = new_value
    
def get_robots_txt(url):
    base_url = get_base_url(url)
    robots_txt_url = f"{base_url}/robots.txt"

    try:
        response = requests.get(robots_txt_url)
        if response.status_code == 200:
            change_variable_value(True)
            return( robots_txt_url + "\n" + response.text)
        else:
            change_variable_value(False)
            return(f"robots.txt can't be retrieved. Status code: {response.status_code}. \n If not sure check policies of the website. \n Web scraping is legal if data publicly available on the internet.")

    except requests.RequestException as e:
        return(f"Error: {e}")


'''
# Example 
website_url = "https://en.tutiempo.net/climate/1959/ws-783670.html"
print(get_robots_txt(website_url))
'''
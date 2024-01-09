def Check_if_legal(link):
     # Use existing libraries or methods to determine if the site is legal to scrape
    # Perform checks or use libraries like robots.txt parsers, etc.
    # Return True if legal, False otherwise (for demonstration purposes)
    if "example.com" in link:
        return True
    else:
        return False
def get_attributes(link):
    # Here, you would implement the logic to retrieve attributes from the provided link
    # Replace this with actual code that retrieves attributes from the website
    # For demonstration, returning a list of mock attributes
    return ["Attribute1", "Attribute2", "Attribute3", "Attribute4", "Attribute5", "Attribute6", "Attribute7", "Attribute8", "Attribute9"]

def get_data(link, checked_attributes, selected_format):
    # Here, create the file with the checked attributes based on the chosen format
    # For demonstration purposes, just printing the attributes and format
    print("Link:", link)
    print("Checked Attributes:", checked_attributes)
    print("Selected Format:", selected_format)
    # Replace this with code to create a file with the given data and chosen format
    # For example, write the attributes to a CSV or text file based on the selected format
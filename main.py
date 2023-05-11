import json
import random
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

def start_driver(main_url):
    driver.get(main_url)
    driver.implicitly_wait(2)

def html_to_json(element):
    tag = element.name
    attributes = element.attrs
    
    # Extract the text of the current layer only
    pieces = [text.strip() for text in element.find_all(string=True, recursive=False)]
    text = " ".join(pieces)
    # generate an id based on ramdom number and hash of the element
    element_id = hash(element)
    
    children_json = []

    for child in element.children:
        if child.name:
            child_json = html_to_json(child)
            children_json.append(child_json)

    json_element = {
        'tag': tag,
        'attributes': attributes,
        'children': children_json,
        'text': text,
        'elementId': element_id
    }

    return json_element

def json_to_html(json_element):
    tag = json_element.get('tag', 'div')
    attributes = json_element.get('attributes', {})
    children_json = json_element.get('children', [])
    text = json_element.get('text', '')
    html_element = BeautifulSoup('', 'html.parser').new_tag(name=tag, attrs=attributes)
    html_element.string = text
    
    for child_json in children_json:
        child_html = json_to_html(child_json)
        html_element.append(child_html)

    return html_element

# user_data_dir = "/Users/charanreddy/user_data"
options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument(f"user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
actions = ActionChains(driver)
start_driver(main_url='https://www.google.com')
driver.implicitly_wait(10)

# Get the HTML content of the page
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')

# Remove the style attribute from each element
elements_with_style = soup.select('[style]')
for element in elements_with_style:
    del element['style']
    
# Remove the script, style, noscript, link, and meta tags
for tag in soup(['script', 'style', 'noscript', 'link', 'meta']):
    tag.extract()

# save the raw html
with open('raw.html', 'w') as f:
    # prettify the html
    clean_html_content = soup.prettify()
    f.write(str(clean_html_content))

soup = BeautifulSoup(clean_html_content, 'html.parser')
parent_element = soup.find('html')

if parent_element:
    element_dict = html_to_json(parent_element)

    html_string = json_to_html(element_dict)

    # Save the restored HTML
    with open('restored_html.html', 'w') as f:
        html_string = html_string.prettify()
        f.write(str(html_string))

    # Save the dictionary as a JSON file
    with open('json.json', 'w') as json_file:
        json.dump(element_dict, json_file, indent=4, ensure_ascii=False)
else:
    print(f'Element not found')

# Close the WebDriver
driver.quit()

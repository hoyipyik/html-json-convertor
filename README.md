# HTML parser

## Main.py

This file will use a headless browser to get the html. Then it will filter the useless JavaScript, style, link and metadata. The cleaned file will be saved as raw.html

After that, the cleaned html will be converted to json, which will be saved as json.json.

Finnaly, the app will convert json.json back to html, which will be saved as restored_html.html.

## Json_file_convertor

This folder contains some functions to insert, remove and upgrade the json file n json.json.

## neo4j_handler

This folder includes manipulation functions on neo4j database. 


By Alex.Ho

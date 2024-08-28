import csv
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


# Function to read CSV file
def read_csv(csv_path):
    with open(csv_path, newline="",encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        data = [row for row in reader]
    return data

# Function to read JSON file
def read_json(json_path):
    with open(json_path, encoding='utf-8') as file:
        data = json.load(file)
    return data

# Function to read XML file
def read_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Extract data for the whole file
    data = []
    for item in root.findall(root[0].tag):
        record = {child.tag: child.text for child in item}
        data.append(record)
    return data

# Function to scrape HTML file
def scrape_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'lxml')
    table = soup.find('table')

    #Extract hearders
    headers = [th.text for th in table.find('tr').find_all('th')]

    # Extract data for the whole file
    data = []
    for row in table.find_all('tr')[1:]:
        values = [td.text for td in row.find_all('td')]
        data.append(dict(zip(headers, values)))
    return data
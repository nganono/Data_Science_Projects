#Import libraries
from read_data import read_csv, read_json, read_xml, scrape_html
from db_operations import store_data_in_db, retrieve_data

def main():
    # Paths to the data files
    csv_path = "../Data/london_weather.csv"
    json_path = "../Data/london_weather.json"
    xml_path = "../Data/london_weather.xml"
    html_path = "../Data/london_weather.html"
    db_path = "../Data/aggregateddata.db"
    
    # Read data from files
    csv_data = read_csv(csv_path)
    json_data = read_json(json_path)
    xml_data = read_xml(xml_path)
    html_data = scrape_html(html_path)

    # Store data in the SQLite database
    store_data_in_db(db_path, "CSV_Data", csv_data)
    store_data_in_db(db_path, "JSON_Data", json_data)
    store_data_in_db(db_path, "XML_Data", xml_data)
    store_data_in_db(db_path, "HTML_Data", html_data)

    # Retrieve and print the data from the SQLite database
    print("CSV Data from Database:")
    print(retrieve_data(db_path, "CSV_Data"))
    
    print("\nJSON Data from Database:")
    print(retrieve_data(db_path, "JSON_Data"))
    
    print("\nXML Data from Database:")
    print(retrieve_data(db_path, "XML_Data"))
    
    print("\nHTML Data from Database:")
    print(retrieve_data(db_path, "HTML_Data"))

if __name__ == "__main__":
    main()
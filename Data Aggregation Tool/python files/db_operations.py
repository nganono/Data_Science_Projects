#import library
import sqlite3

# Function to create a table query in the SQLite database with appropriate data types
def create_table_query(dict_first_row):
    columns = list(dict_first_row.keys())
    first_row = list(dict_first_row.values())

    # Maps Python data types to SQL data types
    datatype = []
    for data in first_row:
        # Check the type of data and assign the appropriate SQL data type
        if isinstance(data, int):
            datatype.append("INTEGER")
        elif isinstance(data, float):
            datatype.append("REAL")
        elif isinstance(data, str):
            # Determine if the string represents a number
            try:
                float(data)
                datatype.append("REAL")
            except ValueError:
                datatype.append("TEXT")
        else:
            datatype.append("TEXT")

    # Create SQL column definitions
    column_definitions = []
    for col, dtype in zip(columns, datatype):
        column_definitions.append(f'"{col}" {dtype}')  # Quote column names to handle special characters

    # Join the column definitions with commas
    return ", ".join(column_definitions)


# Function to create a table in the SQLite database
def create_table(cursor, table_name, query):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({query})")
    print(f"Table '{table_name}' created successfully.")

# Function to insert data into the SQLite table
def insert_data(cursor, table_name, data):
    if not data:
        return  # No data to insert

    columns = data[0].keys()
    placeholders = ", ".join(["?" for _ in columns])
    
    query = f"INSERT INTO {table_name} ({', '.join(f'\"{col}\"' for col in columns)}) VALUES ({placeholders})"
    
    # Prepare data in tuple form for insertion
    values_list = [tuple(row.values()) for row in data]
    
    cursor.executemany(query, values_list)


# Function to store data into the SQLite database
def store_data_in_db(db_path, table_name, data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Generate the table creation query based on data
    create_table_query_str = create_table_query(data[0])
    
    # Create the table
    create_table(cursor, table_name, create_table_query_str)
    
    # Insert the data into the table
    insert_data(cursor, table_name, data)
    
    # Commit and close the connection
    conn.commit()
    conn.close()

# Function to retrieve data from the SQLite table
def retrieve_data(db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    conn.close()
    return rows


"""
To connect to a SQL Server database from Python, you can use the pyodbc or pymssql library. The most commonly used and flexible is pyodbc.

✅ Step-by-step code using pyodbc:

1. Install pyodbc (if not already installed):
bash
Copy
Edit
pip install pyodbc

2. Python code to connect to SQL Server:
python
Copy
Edit
import pyodbc

# Define your connection parameters
server = 'your_server_name'         # e.g., 'localhost' or '192.168.1.100\SQLEXPRESS'
database = 'your_database_name'     # e.g., 'MonkeyDB'
username = 'your_username'          # e.g., 'sa'
password = 'your_password'          # e.g., 'yourStrong(!)Password'
driver = '{ODBC Driver 17 for SQL Server}'  # Check installed drivers using pyodbc.drivers()

# Create connection string
connection_string = f'''
    DRIVER={driver};
    SERVER={server};
    DATABASE={database};
    UID={username};
    PWD={password};
    TrustServerCertificate=yes;
'''

# Connect to the database
try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Connection successful!")

    # Example query
    cursor.execute("SELECT TOP 5 * FROM Monkeys")
    for row in cursor.fetchall():
        print(row)

    # Close the connection
    conn.close()

except Exception as e:
    print("Connection failed:", e)


"""

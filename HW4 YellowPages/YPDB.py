import sqlite3
connection = sqlite3.connect("yellow_pages.db")
print("Database opened successfully")
cursor = connection.cursor()
#delete
#cursor.execute('''DROP TABLE Company_Info;''')
connection.execute("create table Company_Info (Company_Name TEXT NOT NULL,Phone VARCHAR(12) PRIMARY KEY, Email TEXT UNIQUE NOT NULL, Address TEXT )")
print("Table created successfully")
connection.close() 
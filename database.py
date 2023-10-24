import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

# Creating a table
conn.execute('''CREATE TABLE COMPANY1(
ID INT PRIMATY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("Table created successfully")
conn.close()
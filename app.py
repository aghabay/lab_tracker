import sqlite3
connection = sqlite3.connect("main.db") # this line will create a db

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS vms (Title TEXT, Director, TEXT, Year INT)''')

connection.commit()
connection.close()
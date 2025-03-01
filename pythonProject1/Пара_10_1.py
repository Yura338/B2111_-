import sqlite3

connection = sqlite3.connect("Para_10.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE first_table (name TEXT);")
print(connection)
print(cur)
connection.close()

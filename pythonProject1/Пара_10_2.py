import sqlite3

connection = sqlite3.connect("Para_10.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
connection.commit()
connection.close()

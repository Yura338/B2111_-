import sqlite3

connection = sqlite3.connect("Para_10.sl3", 5)
cur = connection.cursor()
cur.execute("SELECT rowid, name FROM first_table(name TEXT);")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()

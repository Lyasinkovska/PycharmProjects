import sqlite3

connection = sqlite3.connect("draft.db")

cursor = connection.cursor()

'''cursor.execute("""CREATE TABLE family(
				name VARCHAR(20),
				surname VARCHAR(20),
				age INTEGER,
				sex TEXT
				)
				"""
)'''
cursor.execute("""INSERT INTO family VALUES ('Liudmyla', 'Yasinkovska', 29, 'female')""")
cursor.execute("""INSERT INTO family VALUES ("Yura", "Mamonov", 37, "male")""")
cursor.execute("""SELECT * FROM family""")
print(cursor.fetchall())

connection.commit()
#connection.close()

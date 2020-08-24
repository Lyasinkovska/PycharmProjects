import sqlite3

connection = sqlite3.connect("draft.db")

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS family(
				name VARCHAR(20),
				surname VARCHAR(20),
				age INTEGER,
				sex TEXT
				)
				"""
)
#cursor.execute("""INSERT INTO family VALUES ('Liudmyla', 'Yasinkovska', 29, 'female')""")
cursor.execute("""INSERT INTO family VALUES ("Yura", "Mamonov", 37, "male")""")
cursor.execute("SELECT name, surname FROM family WHERE name = 'Yura' AND surname = 'Mamonov'")
print(cursor.fetchone())
print(cursor.fetchall())

connection.commit()
#connection.close()

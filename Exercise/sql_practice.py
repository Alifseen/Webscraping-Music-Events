import sqlite3

## Establish Connection
connection = sqlite3.connect("../files/data.db")
cursor = connection.cursor()

## Reading a Database
cursor.execute("SELECT * FROM events")
print(cursor.fetchall())

## Reading filtered Database
cursor.execute("SELECT band, date FROM events")
print(cursor.fetchall())

## Reading a Database based on Condition
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
print(cursor.fetchall())

## Adding a new row
cursor.execute("INSERT INTO events VALUES('Fish','Fish City','2088.10.16')")
connection.commit()

cursor.execute("SELECT * FROM events")
print(cursor.fetchall())

## Adding multiple rows using ? placeholder
new_rows = [
    ("Cat", "Cat City", "2088.10.14"),
    ("Chicken", "Chicken City", "2088.10.13")
]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

cursor.execute("SELECT * FROM events")
print(cursor.fetchall())

## Delete a row
cursor.execute("DELETE FROM events WHERE band='Fish'")
cursor.execute("DELETE FROM events WHERE band='Chicken'")
cursor.execute("DELETE FROM events WHERE band='Cat'")
connection.commit()

cursor.execute("SELECT * FROM events")
print(cursor.fetchall())

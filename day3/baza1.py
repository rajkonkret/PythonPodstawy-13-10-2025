# baza danych - system do przechowywania i przetwarzania danych

# sql, nosql
import sqlite3

sql_connection = None

try:
    sql_connection = sqlite3.connect("baza.db")
    cursor = sql_connection.cursor()
    print("Baza została podłaączona")

    query = """CREATE TABLE IF NOT EXISTS developers
    (id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL NOT NULL);"""

    cursor.execute(query)
    sql_connection.commit()
except sqlite3.Error as e:
    print("Błąd:", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")

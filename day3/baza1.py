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

    # cursor.execute(query)
    # sql_connection.commit()

    insert = """
    INSERT INTO developers(id,name,salary)
             VALUES (3, 'Tomek', 35000);
             """

    # cursor.execute(insert)
    # sql_connection.commit()

    update = """
    UPDATE developers
    SET salary=40000
             WHERE id=3;"""
    # cursor.execute(update)
    # sql_connection.commit()

    for row in cursor.execute("SELECT * FROM developers;"):
        print(row)# (3, 'Tomek', 40000.0)

except sqlite3.Error as e:
    print("Błąd:", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")

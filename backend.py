import sqlite3

#connection to the database
def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

#insertion of data to the database
def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn,))
    conn.commit()
    conn.close()

#searching data from the database
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#selecting all data from the database
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM books")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#updating specified data to the database
def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE books SET title=?, author=?, year=?, isbn=?  WHERE id=?",(title,author,year,isbn,id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()

#deleting specified data from the database
def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM books WHERE id=?",(id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
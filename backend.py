import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn,))
    conn.commit()
    conn.close()

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn,))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM books")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(id,title,author,price,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE books SET title=?, author=?, year=?, isbn=?  WHERE id=?",(title,author,year,isbn,id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM books WHERE id=?",(id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
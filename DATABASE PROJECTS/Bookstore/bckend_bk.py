import sqlite3 as sq

def connect(dbname):
    conn = sq.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE if not exists BOOKSTORE(id INTEGER primary key,title text,author text,year INTEGER check(year>0 and year<=2018),isbn INTEGER UNIQUE);""")
    conn.commit()
    return conn

def insert(conn,title,author,year,isbn):
    cursor = conn.cursor()
    book = (title,author,year,isbn)
    cursor.execute("INSERT INTO bookstore VALUES(NULL,?,?,?,?);",book)
    conn.commit()
    
def update(conn,id,title,author,year,isbn):
    cursor = conn.cursor()
    book = (title,author,year,isbn,id)
    cursor.execute("UPDATE bookstore SET title = ?,author = ?,year = ?,isbn = ? WHERE id = ?",book)
    conn.commit()
    
def delete(conn,id = ''):
    cursor = conn.cursor()
    book = (id,)
    cursor.execute("DELETE from bookstore WHERE id = ?",book)
    conn.commit()
    
def search(conn,title = '',author = '',year = 2018,isbn = 1):
    cursor = conn.cursor()
    book = (title,author,year,isbn)
    print(book)
    cursor.execute("SELECT * FROM bookstore WHERE title = ? or author = ? or year = ? or isbn = ? ",book)
    c = cursor.fetchall()
    return c
    
def view(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookstore")
    c = cursor.fetchall()
    return c
 
def close(conn):
    conn.close()       

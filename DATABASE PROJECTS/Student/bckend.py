import sqlite3 as sq

def connect(dbname):
    conn = sq.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE if not exists STUDENT(id INTEGER primary key,name text,age Number,aim text);""")
    conn.commit()
    return conn

def insert(conn,name,age,aim):
    cursor = conn.cursor()
    st = (name,age,aim)
    cursor.execute("INSERT INTO student VALUES(NULL,?,?,?);",st)
    conn.commit()
    
def update(conn,id = 0,name = '',age = 0,aim = ''):
    cursor = conn.cursor()
    st = (name,age,aim,id)
    cursor.execute("UPDATE student SET name = ?,age = ?,aim = ? WHERE id = ?",st)
    conn.commit()
    
def delete(conn,id = ''):
    cursor = conn.cursor()
    st = (id,)
    cursor.execute("DELETE from student WHERE id = ?",st)
    conn.commit()
    
def search(conn,id = '',name = '',age = '',aim = ''):
    cursor = conn.cursor()
    st = (name,age,aim,id)
    cursor.execute("SELECT * FROM student WHERE name = ? or age = ? or aim = ? or id = ?",st)
    c = cursor.fetchall()
    return c
    
def view(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    c = cursor.fetchall()
    return c
 
def close(conn):
    conn.close()       
    



import Student.bckend as b

conn = b.connect('student.db')
'''
b.insert(conn,'Dheeraj',20,'Doctor')
b.insert(conn,'Rama',22,'Engineer')
b.insert(conn,'Gaurav',24,'Wildlife PhotoGrapher')
b.insert(conn,'Sudha',23,'Politician')
b.insert(conn,'Manav',22,'Interior Designer')

b.update(conn,name = 'Dheeraj',age = 20,aim = 'Dentist',id = 1)

b.delete(conn,name = 'Dheeraj')
'''

b.search(conn,name = 'Rama')
b.view(conn)
b.close(conn)
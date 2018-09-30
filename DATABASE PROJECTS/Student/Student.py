from tkinter import *
import bckend as bk
class Student:
    
    def __init__(self,window):

        self.Ilabel = Label(window,text = 'ID',width = 10,height = 1)
        self.IEntry = Entry(window)
        self.Nlabel = Label(window,text = 'Name',width = 10,height = 1)
        self.NEntry = Entry(window)
        self.Alabel = Label(window,text = 'Age',width = 10,height = 1)
        self.AEntry = Entry(window)
        self.Mlabel = Label(window,text = 'Aim',width = 10,height = 1)
        self.MEntry = Entry(window)
        
        self.Ilabel.place(x = 0, y = 10)
        self.IEntry.place(x = 100, y = 10)
        self.Nlabel.place(x = 300, y = 10)
        self.NEntry.place(x = 400, y = 10)
        self.Alabel.place(x = 0, y = 40)
        self.AEntry.place(x = 100, y = 40)
        self.Mlabel.place(x = 300, y = 40)
        self.MEntry.place(x = 400, y = 40)
        
        self.viewArea = Listbox(window, height=10, width=40)
        self.viewArea.place(x = 0,y = 100)
        self.viewArea.bind('<<ListboxSelect>>', self.highlight_row)

        self.butView = Button(window, text = 'View all',width = 20,height = 1,command = lambda:self.viewall(self.conn))
        self.butSearch = Button(window, text = 'Search entry',width = 20,height = 1,command = lambda:self.search_entry(self.conn))
        self.butAdd = Button(window, text = 'Add entry',width = 20,height = 1,command = lambda:self.add_entry(self.conn))
        self.butUpdate = Button(window, text = 'Update selected',width = 20,height = 1,command = lambda:self.update_selected(self.conn))
        self.butDelete = Button(window, text = 'Delete selected',width = 20,height = 1,command = lambda:self.delete_selected(self.conn))
        
        self.butView.place(x = 410,y = 80)
        self.butSearch.place(x = 410,y = 120)
        self.butAdd.place(x = 410,y = 160)
        self.butUpdate.place(x = 410,y = 200)
        self.butDelete.place(x = 410,y = 240)

        self.conn = bk.connect('student.db')
        self.viewall(self.conn)
         
    def highlight_row(self,event):
        try:
            index = self.viewArea.curselection()[0]
            self.highlight_tuple = self.viewArea.get(index)
            self.IEntry.delete(0,END)
            self.IEntry.insert(END,self.highlight_tuple[0])
            self.NEntry.delete(0, END)
            self.NEntry.insert(END,self.highlight_tuple[1])
            self.AEntry.delete(0, END)
            self.AEntry.insert(END,self.highlight_tuple[2])
            self.MEntry.delete(0, END)
            self.MEntry.insert(END,self.highlight_tuple[3])
        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute

    def viewall(self,conn):
        self.viewArea.delete(0,END)
        c = bk.view(conn)
        for row in c:
            print(row)
            self.viewArea.insert(END,row)
            
    def search_entry(self,conn):
        id = self.IEntry.get()
        name = self.NEntry.get()
        age = self.AEntry.get()
        aim = self.MEntry.get()
        c = bk.search(conn,id = id,name = name,age = age,aim = aim)
        self.viewArea.delete(0,END)
        for row in c:
            print(row)
            self.viewArea.insert(END,row)
        
    def add_entry(self,conn):
        name = self.NEntry.get()
        age = self.AEntry.get()
        aim = self.MEntry.get()
        bk.insert(conn,name = name,age = age,aim = aim)
        self.viewall(conn)
        
    def update_selected(self,conn):
        id = self.highlight_tuple[0]
        name = self.NEntry.get()
        age = self.AEntry.get()
        aim = self.MEntry.get()
        bk.update(conn,name = name, age = age,aim = aim,id = id)
        self.viewall(conn)
        
    def delete_selected(self,conn):
        id = self.highlight_tuple[0]
        bk.delete(conn,id = id)
        self.viewall(conn)
        
window = Tk()
window.title('Student')
window.geometry("600x300")
obj = Student(window)
window.mainloop()
        
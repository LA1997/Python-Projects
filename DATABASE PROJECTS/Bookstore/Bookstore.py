from tkinter import *
import bckend_bk as bk

class BookStore:
    def __init__(self,window):

        self.Tlabel = Label(window,bg = 'Black',fg = 'White',text = 'Title',width = 10,height = 1)
        self.TEntry = Entry(window)
        self.Alabel = Label(window,bg = 'Black',fg = 'White',text = 'Author',width = 10,height = 1)
        self.AEntry = Entry(window)
        self.Ylabel = Label(window,bg = 'Black',fg = 'White',text = 'Year',width = 10,height = 1)
        self.YEntry = Entry(window)
        self.Ilabel = Label(window,bg = 'Black',fg = 'White',text = 'ISBN',width = 10,height = 1)
        self.IEntry = Entry(window)
        
        self.Tlabel.place(x = 0, y = 10)
        self.TEntry.place(x = 100, y = 10)
        self.Alabel.place(x = 300, y = 10)
        self.AEntry.place(x = 400, y = 10)
        self.Ylabel.place(x = 0, y = 40)
        self.YEntry.place(x = 100, y = 40)
        self.Ilabel.place(x = 300, y = 40)
        self.IEntry.place(x = 400, y = 40)
        
        self.viewArea = Listbox(window, bg = 'Orange',height=11, width=50)
        self.viewArea.place(x = 0,y = 100)
        self.viewArea.bind('<<ListboxSelect>>', self.highlight_row)

        self.butView = Button(window, bg = 'Orange',text = 'View all',width = 20,height = 1,command = lambda:self.viewall(self.conn))
        self.butSearch = Button(window, bg = 'Orange', text = 'Search entry',width = 20,height = 1,command = lambda:self.search_entry(self.conn))
        self.butAdd = Button(window, bg = 'Orange', text = 'Add entry',width = 20,height = 1,command = lambda:self.add_entry(self.conn))
        self.butUpdate = Button(window, bg = 'Orange', text = 'Update selected',width = 20,height = 1,command = lambda:self.update_selected(self.conn))
        self.butDelete = Button(window, bg = 'Orange',text = 'Delete selected',width = 20,height = 1,command = lambda:self.delete_selected(self.conn))
        self.butView.place(x = 410,y = 100)
        self.butSearch.place(x = 410,y = 140)
        self.butAdd.place(x = 410,y = 180)
        self.butUpdate.place(x = 410,y = 220)
        self.butDelete.place(x = 410,y = 260)

        self.conn = bk.connect('bookstore.db')
        self.viewall(self.conn)
        
    def highlight_row(self,Event):
        try:
            index = self.viewArea.curselection()[0]
            self.highlight_tuple = self.viewArea.get(index)
            self.TEntry.delete(0,END)
            self.TEntry.insert(END,self.highlight_tuple[1])
            self.AEntry.delete(0,END)
            self.AEntry.insert(END,self.highlight_tuple[2])
            self.YEntry.delete(0,END)
            self.YEntry.insert(END,self.highlight_tuple[3])
            self.IEntry.delete(0,END)
            self.IEntry.insert(END,self.highlight_tuple[4])
        except IndexError:
            pass
        
    def viewall(self,conn):
        self.viewArea.delete(0,END)
        c = bk.view(self.conn)
        for row in c:
            print(row)
            self.viewArea.insert(END,row)
    
    def search_entry(self,conn):
        self.viewArea.delete(0,END)
        title = self.TEntry.get()
        author = self.AEntry.get()
        year = self.YEntry.get()
        isbn = self.IEntry.get()
        c = bk.search(self.conn,title = title,author = author,year = year,isbn = isbn)
        for row in c:
            print(row)
            self.viewArea.insert(END,row)
                   
    def add_entry(self,conn):
        title = self.TEntry.get()
        author = self.AEntry.get()
        year = self.YEntry.get()
        isbn = self.IEntry.get()
        bk.insert(conn,title = title,author = author,year = year,isbn = isbn)
        self.viewall(conn)
        
    def update_selected(self,conn):
        id = self.highlight_tuple[0]
        title = self.TEntry.get()
        author = self.AEntry.get()
        year = self.YEntry.get()
        isbn = self.IEntry.get()
        bk.update(conn,id = id,title = title,author = author,year = year,isbn = isbn)
        self.viewall(conn)
        
    def delete_selected(self,conn):
        id = self.highlight_tuple[0]
        bk.delete(conn,id = id)
        self.viewall(conn)
        
window = Tk()
window.title('BookStore')
window.config(bg = 'Black')
window.geometry("600x300")
obj = BookStore(window)
window.mainloop()
        
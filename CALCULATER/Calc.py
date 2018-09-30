import sqlite3 as sq
from tkinter import *
from math import *
import unicodedata as ud 
import tkinter.messagebox
window = Tk()

txtframe = Frame(window)
txtframe.grid(row = 2,column = 0)

butframe = Frame(window)
butframe.grid(row = 3,column = 0)

sciframe = Frame(window)
#sciframe.grid(row = 4,column = 0)

viewArea = Listbox(window, height=10, width=50)
#viewArea.grid(row = 1,column = 0)

hist_button_frame = Frame(window)
hist_button_frame.grid(row = 0, column = 0)

scr = Entry(txtframe,width = 21,font = ("Calibri",20))
scr.grid(row = 0,column = 0)
scr.focus_set()

htoggle = IntVar()
htoggle.set(0)

stoggle = IntVar()
stoggle.set(0)

window.title('Calculator')

conn = sq.connect('CalcHist.db')
cursor = conn.cursor()
        
def replace():
    
    div = '\u00F2'
    newtext = scr.get().replace(str('\u00F7'),'/')
    newtext = scr.get().replace('x','*')
    scr.delete(0,END)
    scr.insert(0,newtext)
    
def print_char(ch):
    if(ch == str('\u00F7')):
        scr.insert(END,'/')
    else:
        scr.insert(END,ch)
    
def print_sci(ch):
    li = ['Sin(','Cos(','Tan(','Exp(','Log(','Ln(']
    val = scr.get()
    res = 0
    if(val == None):
        scr.insert(0, 'INVALID INPUT!!!')
    else:
        val = float(val)
        op = li.index(ch)
        if(op == 0):
            res = sin(val)
        elif(op == 1):
            res = cos(val)
        elif(op == 2):
            res = tan(val)
        elif(op == 3):
            res = exp(val)
        elif(op == 4):
            res = log(val,10)
        elif(op == 5):
            res = log(val)
        scr.insert(0,ch + str(val) + ') = ' + str(res))
    exp_tuple = (ch + str(val) +') ', str(res))
    cursor.execute("INSERT INTO CALCHIST VALUES(NULL,?,?,NULL,NULL);",exp_tuple)
    conn.commit()
        
def clear_all():
    scr.delete(0,END)

def clear():
    txt = scr.get()[:-1]
    scr.delete(0,END)
    scr.insert(END,txt)

def square():
    try:
        expn = scr.get()
        value = eval(expn)
        exp_tuple = (expn,pow(value,2))
        print(exp_tuple)
        cursor.execute("INSERT INTO CALCHIST VALUES(NULL,?,?,1,0);",exp_tuple)
        conn.commit()
        
    except SyntaxError or NameError:
        scr.delete(0,END)
        scr.insert(0,'INVALID INPUT !!!')
    else:
        sqrtval = pow(value,2)
        scr.insert(END,'\u00B2'+' = '+str(sqrtval))
    
def sqroot():
    try:
        expn = scr.get()
        value = eval(expn)
        exp_tuple = (expn,sqrt(value))
        print(exp_tuple)
        cursor.execute("INSERT INTO CALCHIST VALUES(NULL,?,?,0,1);",exp_tuple)
        conn.commit()
        
    except SyntaxError or NameError:
        scr.delete(0,END)
        scr.insert(0,'INVALID INPUT !!!')
    else:
        sqrtval = sqrt(value)
        scr.delete(0,END)
        scr.insert(END,'\u221A'+str(value)+' = '+str(sqrtval))
        
def equals():
    replace()
    expn = scr.get()
    print(expn)
    try:
        value = eval(scr.get())
        cursor.execute("""CREATE TABLE if not exists CALCHIST(id INTEGER primary key,exp text,result text,sq INTEGER,sqroot INTEGER);""")
        conn.commit()
        exp_tuple = (expn,value)
        cursor.execute("INSERT INTO CALCHIST VALUES(NULL,?,?,NULL,NULL);",exp_tuple)
        conn.commit()
        
    except SyntaxError or NameError:
        scr.delete(0,END)
        scr.insert(0,'INVALID INPUT !!!')
    
    else:
        scr.delete(0,END)
        scr.insert(END,value)
        
def highlight_row():
    try:
        index = viewArea.curselection()[0]
        #self.highlight_tuple = self.viewArea.get(index)
            
        print(index)
        return index
    except IndexError:
        pass
    
def show_hist(htoggle):
    if(htoggle.get() == 0):    
        viewArea.grid(row = 1,column = 0)
        viewButton.grid(row = 1,column = 1)
        del_sel_button.grid(row = 1,column = 2)
        delButton.grid(row = 1,column = 3)
        histButText.set('Hide History')
        htoggle.set(1)
        
    else:
        viewArea.grid_remove()
        viewButton.grid_remove()
        del_sel_button.grid_remove()
        delButton.grid_remove()
        histButText.set('Show History')
        htoggle.set(0)

def view_hist():
    viewArea.delete(0,END)
    cursor.execute("SELECT * FROM CALCHIST")
    c = cursor.fetchall()
    for lm in c:
        if (lm[3] != None and lm[4]!= None):
            if(lm[3] == 1):
                viewArea.insert(END,lm[1] + '\u00B2' + ' = ' + str(lm[2]))
            elif(lm[4] == 1):
                viewArea.insert(END,'\u221A' + lm[1] + ' = ' + str(lm[2]))
        else:
            viewArea.insert(END,lm[1] + ' = ' + lm[2])
                
def del_sel():
    index = highlight_row()
    id = index + 1
    expn = (id,)
    cursor.execute("DELETE from CALCHIST WHERE id = ?",expn)
    cursor.execute("UPDATE CALCHIST set id = id - 1 where id > ?",expn)
    conn.commit()
    view_hist()

def del_comp():
    answer = tkinter.messagebox.askokcancel('Warning','Are you sure you want to delete the entire history?')
    if(answer):
        cursor.execute("DELETE from CALCHIST")
    conn.commit()
    view_hist()
    
def show_sci(stoggle):
    if(stoggle.get() == 0):
        sciframe.grid(row = 4,column = 0)
        sci_text.set('HIDE SCIENTIFIC CALCULATOR')
        stoggle.set(1)
        
    else:
        sciframe.grid_remove()
        sci_text.set('SHOW SCIENTIFIC CALCULATOR')
        stoggle.set(0)
        

histLabel = Label(hist_button_frame,text = 'History: ')
histLabel.grid(row = 0,column = 0)

histButText = StringVar()
histButton = Button(hist_button_frame,textvariable = histButText, width = 30,height = 1,command = lambda: show_hist(htoggle))
histButText.set('Show History')
histButton.grid(row = 0,column = 1,columnspan = 3)

viewButton = Button(hist_button_frame,text = 'View/Update\nHistory',width = 9,height = 2,command = view_hist)
#viewButton.grid(row = 1,column = 1)

del_sel_button = Button(hist_button_frame,text = 'Delete\nSelected',width = 9,height = 2,command = del_sel)
#del_sel_button.grid(row = 0,column = 2)

delButton = Button(hist_button_frame,text = 'Delete\nComplete',width = 9,height = 2,command = del_comp)
#delButton.grid(row = 0,column = 3)
    
but7 = Button(butframe,text = '7',width = 4,height = 2,command = lambda:print_char('7'))
but7.grid(row = 0,column = 0)
but8 = Button(butframe,text = '8',width = 4,height = 2,command = lambda:print_char('8'))
but8.grid(row = 0,column = 1)
but9 = Button(butframe,text = '9',width = 4,height = 2,command = lambda:print_char('9'))
but9.grid(row = 0,column = 2)
butdiv = Button(butframe,text = '\u00F7',width = 4,height = 2,command = lambda:print_char('\u00F7'))
butdiv.grid(row = 0,column = 3)
butAC = Button(butframe,text = 'AC',width = 4,height = 2,command = clear_all)
butAC.grid(row = 0,column = 4)
butC = Button(butframe,text = 'C',width = 4,height = 2,command = clear)
butC.grid(row = 0,column = 5)

but4 = Button(butframe,text = '4',width = 4,height = 2,command = lambda:print_char('4'))
but4.grid(row = 1,column = 0)
but5 = Button(butframe,text = '5',width = 4,height = 2,command = lambda:print_char('5'))
but5.grid(row = 1,column = 1)
but6 = Button(butframe,text = '6',width = 4,height = 2,command = lambda:print_char('6'))
but6.grid(row = 1,column = 2)
butmul = Button(butframe,text = 'x',width = 4,height = 2,command = lambda:print_char('x'))
butmul.grid(row = 1,column = 3)
butopbr = Button(butframe,text = '(',width = 4,height = 2,command = lambda:print_char('('))
butopbr.grid(row = 1,column = 4)
butclbr = Button(butframe,text = ')',width = 4,height = 2,command = lambda:print_char(')'))
butclbr.grid(row = 1,column = 5)

but1 = Button(butframe,text = '1',width = 4,height = 2,command = lambda:print_char('1'))
but1.grid(row = 2,column = 0)
but2 = Button(butframe,text = '2',width = 4,height = 2,command = lambda:print_char('2'))
but2.grid(row = 2,column = 1)
but3 = Button(butframe,text = '3',width = 4,height = 2,command = lambda:print_char('3'))
but3.grid(row = 2,column = 2)
butmin = Button(butframe,text = '-',width = 4,height = 2,command = lambda:print_char('-'))
butmin.grid(row = 2,column = 3)
butsqr = Button(butframe,text = '\u221A',width = 4,height = 2,command = sqroot)
butsqr.grid(row = 2,column = 4)
butsq = Button(butframe,text = 'x'+'\u00B2',width = 4,height = 2,command = square)
butsq.grid(row = 2,column = 5)

but0 = Button(butframe,text = '0',width = 4,height = 2,command = lambda:print_char('0'))
but0.grid(row = 3,column = 0)
butpr = Button(butframe,text = '.',width = 4,height = 2,command = lambda:print_char('.'))
butpr.grid(row = 3,column = 1)
butper = Button(butframe,text = '%',width = 4,height = 2,command = lambda:print_char('%'))
butper.grid(row = 3,column = 2)
butplus = Button(butframe,text = '+',width = 4,height = 2,command = lambda:print_char('+'))
butplus.grid(row = 3,column = 3)
buteq = Button(butframe,text = '=',width = 12,height = 2,command = equals)
buteq.grid(row = 3,column = 4,columnspan = 2)

sci_text = StringVar()
sciBut = Button(butframe,textvariable = sci_text,width = 30,height = 2,command = lambda:show_sci(stoggle))
sci_text.set('SHOW SCIENTIFIC CALCULATOR')
sciBut.grid(row = 4,column = 0,columnspan = 6)

butsin = Button(sciframe,text = 'Sin',width = 4,height = 2,command = lambda:print_sci('Sin('))
butsin.grid(row = 0,column = 0)
butcos = Button(sciframe,text = 'Cos',width = 4,height = 2,command = lambda:print_sci('Cos('))
butcos.grid(row = 0,column = 1)
buttan = Button(sciframe,text = 'Tan',width = 4,height = 2,command = lambda:print_sci('Tan('))
buttan.grid(row = 0,column = 2)
butexp = Button(sciframe,text = 'Exp',width = 4,height = 2,command = lambda:print_sci('Exp('))
butexp.grid(row = 0,column = 3)
butlog = Button(sciframe,text = 'Log',width = 4,height = 2,command = lambda:print_sci('Log('))
butlog.grid(row = 0,column = 4)
butln = Button(sciframe,text = 'Ln',width = 4,height = 2,command = lambda:print_sci('Ln('))
butln.grid(row = 0,column = 5)


window.mainloop()
import re
from datetime import *
from tkinter import *
import tkinter.ttk as ttk
import PIL.Image,PIL.ImageTk
import tkinter as tk
class Gui:
    def __init__(self,window):
        
        self.tlabel = Label(window,text = 'AGE CALCULATOR',bg = 'Orange',fg = 'Black',font = ('times',20,'bold'))
        self.tlabel.place(x = 300, y = 10)
        
        self.blabel = Label(window,text = 'Enter your birth day',bg = 'Orange',fg = 'Black',font = ('times',15,'bold'))
        self.blabel.place(x = 150, y = 195)
        
        self.nd = [val for val in range(1,32)]
        self.nm = [val for val in range(1,13)]
        self.ny = [val for val in range(1900,datetime.now().year + 1)]
        
        self.dvar = StringVar(window)
        self.mvar = StringVar(window)
        self.yvar = StringVar(window)
        self.dvar.set(1)
        self.mvar.set(1)
        self.yvar.set(1900)
        self.dMenu = ttk.Combobox(window, textvariable=self.dvar, values = self.nd,width = 5)
        #self.dMenu = OptionMenu(window, self.dvar, *self.nd)
        self.dMenu.place(x = 350, y = 200)
        
        self.mMenu = ttk.Combobox(window, textvariable=self.mvar, values = self.nm,width = 5)
        #self.mMenu = OptionMenu(window, self.mvar, *self.nm)
        self.mMenu.place(x = 410, y = 200)
        
        self.yMenu = ttk.Combobox(window, textvariable=self.yvar, values = self.ny,width = 5)
        #self.yMenu = OptionMenu(window, self.yvar, *self.ny)
        self.yMenu.place(x = 480, y = 200)
        
        cur_var = StringVar()
        cur_var.set('Current Date is: {}/{}/{} {}:{}:{}'.format(int(datetime.now().year), int(datetime.now().month), int(datetime.now().day), int(datetime.now().hour), int(datetime.now().minute), float(datetime.now().second)))
        self.curLabel = Label(window,textvariable = cur_var,bg = 'Orange',fg = 'Black',font = ('times',20,'bold'))
        self.curLabel.place(x = 200, y = 100)
        self.mvar.trace('w', self.change_day)
        self.yvar.trace('w', self.change_day)
    
        w = 600
        h = 400
        im = PIL.Image.open('images.png')
        im.putalpha(30)
        im.save('images1.png')
        im1 = PIL.Image.open('images1.png')
        im1 = im1.resize((w,h), PIL.Image.ANTIALIAS)
        self.image1 = PIL.ImageTk.PhotoImage(im1) 
        self.rvar = StringVar()
        self.rLabel = Label(window,image = self.image1,compound=tkinter.CENTER,font = ("Helvetica", 10, "bold italic"),textvariable = self.rvar,height = h,width = w,bg = '#FFBD33',fg = 'Black') 
        self.rLabel.place(x = 100, y = 300)
        self.rLabel.config(anchor = NW, justify = LEFT)
        
        self.Cbutton = Button(window,text = 'CALCULATE',height = 1,width = 20,bg = 'Blue',fg = 'White',font = ('times',10,'bold'),command = self.calc)
        self.Cbutton.place(x = 600,y = 200)
    
    def calc(self):
        
        s_year, s_month, s_day, s_hours, s_minutes, s_seconds = int(datetime.now().year), int(datetime.now().month), int(datetime.now().day), int(datetime.now().hour), int(datetime.now().minute), float(datetime.now().second)
        
        print(s_year, s_month, s_day, s_hours, s_minutes, s_seconds)
        s_mic = datetime.now().microsecond
        s_mil = s_mic/1000
        
        birth_year, birth_month, birth_day = int(self.yvar.get()), int(self.mvar.get()), int(self.dvar.get())
        dd = (datetime(s_year,s_month,s_day) - datetime(birth_year,birth_month,birth_day)).days
        hh = dd * 24 + s_hours
        min = hh * 60 + s_minutes
        sec = min * 60 + s_seconds
        mlsec = sec * 1000 + s_mil
        mcsec = mlsec * 1000 + s_mic
        
        if s_day < birth_day:
            s_day += 30
            s_month -= 1
        if s_month < birth_month:
            s_month += 12
            s_year -= 1
        
        year = s_year - birth_year
        month = s_month - birth_month
        day = s_day - birth_day
        
        str = ''
        str += 'Your age is: {} years, {} months and {} days'.format(year,month,day) + '\n\tor\nYour age is: {} months and {} days'.format((year * 12) + month,day) + '\n\tor\nYour age is: {} weeks and {} days'.format((dd // 7),(dd % 7)) + '\n\tor\nYour age is: {} days'.format(dd) + '\n\tor\nYour age is: {} hours'.format(hh) + '\n\tor\nYour age is: {} minutes'.format(min) + '\n\tor\nYour age is: {} seconds'.format(sec) + '\n\tor\nYour age is: {} milliseconds'.format(mlsec) + '\n\tor\nYour age is: {} microseconds'.format(mcsec)
        self.rvar.set(str)
    
        print('--------------------------------------------------------------------')

    def leap(self,year):
        if ((year % 4) == 0):
            if ((year % 100) == 0):
                if ((year % 400) == 0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
    def dappend(self,val):
        if(val not in self.nd):
            self.nd.append(val)
            
    def dremove(self,val):
        if(val in self.nd):
            self.nd.remove(val)
            
    def change_day(self,*args):
        day = int(self.dvar.get())
        month = int(self.mvar.get())
        year = int(self.yvar.get())
        if(month in [2,4,6,9,11]):
            if(month == 2):
                if(self.leap(year)):
                    print('leap')
                    if(day > 29):
                        self.dvar.set(29)
                    self.dappend(29)
                    self.dremove(30)
                    self.dremove(31)
                    
                else:
                    if(day > 28):
                        self.dvar.set(28)
                    self.dremove(29)
                    self.dremove(30)
                    self.dremove(31)
                    
            else:
                if(day > 30):
                    self.dvar.set(30)
                self.dappend(29)
                self.dappend(30)
                self.dremove(31)
                
        else:
            self.dappend(29)
            self.dappend(30)
            self.dappend(31)
            
        print(self.nd)   
        self.dMenu.destroy()
        self.dMenu = ttk.Combobox(window, textvariable=self.dvar, values = self.nd,width = 5)
        self.dMenu.place(x = 350, y = 200)
        
                
                       
        
        
''' 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
 
# link function to change dropdown
tkvar.trace('w', change_dropdown)
'''
window = Tk()
window.config(bg = 'Orange')
window.geometry('800x700')
window.title('Age Calculator')
obj = Gui(window)
window.mainloop()

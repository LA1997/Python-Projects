import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:

    #variables
    root = Tk()

    #default window width and height
    thisWidth = 300
    thisHeight = 300
    thisTextArea = Text(root)
    thisMenuBar = Menu(root)
    thisFileMenu = Menu(thisMenuBar,tearoff=0)
    thisEditMenu = Menu(thisMenuBar,tearoff=0)
    thisHelpMenu = Menu(thisMenuBar,tearoff=0)
    thisScrollBar = Scrollbar(thisTextArea)
    file = None

    def __init__(self,width = 0,height = 0):
        #initialization

        #set icon
        try:
                self.root.wm_iconbitmap("Notepad.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
                pass

        #set window size (the default is 300x300)

        try:
            self.thisWidth = width
        except KeyError:
            pass

        try:
            self.thisHeight = height
        except KeyError:
            pass

        #set the window text
        self.root.title("Untitled - Notepad")

        #center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        left = (screenWidth / 2) - (self.thisWidth / 2)
        top = (screenHeight / 2) - (self.thisHeight /2)

        self.root.geometry('%dx%d+%d+%d' % (self.thisWidth, self.thisHeight, left, top))

        #to make the textarea auto resizable
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.thisTextArea.grid(sticky=N+E+S+W)

        self.thisFileMenu.add_command(label="New",command=self.newFile)
        self.thisFileMenu.add_command(label="Open",command=self.openFile)
        self.thisFileMenu.add_command(label="Save",command=self.saveFile)
        self.thisFileMenu.add_separator()
        self.thisFileMenu.add_command(label="Exit",command=self.quitApplication)
        self.thisMenuBar.add_cascade(label="File",menu=self.thisFileMenu)

        self.thisEditMenu.add_command(label="Cut",command=self.cut)
        self.thisEditMenu.add_command(label="Copy",command=self.copy)
        self.thisEditMenu.add_command(label="Paste",command=self.paste)
        self.thisMenuBar.add_cascade(label="Edit",menu=self.thisEditMenu)

        self.thisHelpMenu.add_command(label="About Notepad",command=self.showAbout)
        self.thisMenuBar.add_cascade(label="Help",menu=self.thisHelpMenu)

        self.root.config(menu=self.thisMenuBar)

        self.thisScrollBar.pack(side=RIGHT,fill=Y)
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)
    
        
    def quitApplication(self):
        self.root.destroy()
        #exit()

    def showAbout(self):
        showinfo("Notepad","Created by: LOKESH AGGARWAL");

    def openFile(self):
        
        self.file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.file == "":
            #no file to open
            self.file = None
        else:
            #try to open the file
            #set the window title
            self.root.title(os.path.basename(self.file) + " - Notepad")
            self.thisTextArea.delete(1.0,END)

            file = open(self.file,"r")

            self.thisTextArea.insert(1.0,file.read())

            file.close()

        
    def newFile(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.thisTextArea.delete(1.0,END)

    def saveFile(self):

        if self.file == None:
            #save as new file
            self.file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.file == "":
                self.file = None
            else:
                #try to save the file
                file = open(self.file,"w")
                file.write(self.thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.root.title(os.path.basename(self.file) + " - Notepad")
                
            
        else:
            file = open(self.file,"w")
            file.write(self.thisTextArea.get(1.0,END))
            file.close()

    def cut(self):
        self.thisTextArea.event_generate("<<Cut>>")

    def copy(self):
        self.thisTextArea.event_generate("<<Copy>>")

    def paste(self):
        self.thisTextArea.event_generate("<<Paste>>")

    def run(self):

        #run main application
        self.root.mainloop()




#run main application
notepad = Notepad(width=1500,height=1000)
notepad.run()

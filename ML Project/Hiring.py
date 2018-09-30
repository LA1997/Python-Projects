from tkinter import *
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as py
from statistics import mode, StatisticsError
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm, datasets
import pickle

class Hiring:
    def to_binary(self,pred):
        return int(pred > 0.5)

    def trainLogisticReg(self,X,y):
        model = LogisticRegression()
        model.fit(X,y)
        return model

    def trainDecisionTree(self,X,y):
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X,y)
        return clf 
    
    def trainRandomForest(self,X,y):
        clf = RandomForestClassifier(n_estimators = 10)            
        clf = clf.fit(X,y)
        return clf

    def trainSVM(self,X,y):
        C = 2.0
        svc = svm.SVC(kernel='linear', C=C).fit(X, y)
        filename = 'svm.sav'
        pickle.dump(svc,open(filename,'wb'))
        return svc
    
    def __init__(self):
        
        self.window = Tk()
        self.window.title('desoix.com')
        self.window.config(bg = '#FFBD33')
        self.window.geometry('1000x700')
        self.window.attributes('-fullscreen',True)
        self.state = True
        self.window.bind("<F11>", self.toggle_fullscreen)
        self.window.bind("<Escape>", self.end_fullscreen)
        
        self.Hfont = ('Verdana', 40, 'bold')
        self.Lfont = ('times',15,'bold')
        self.Hlabel = Label(self.window,text = 'Private Limited',bg = '#FFBD33',fg = 'Black',font = self.Hfont)
        self.Hlabel.place(x = 470,y = 45)
        self.logo1 = PhotoImage(file = 'logo.png')
        self.img = Label(self.window,image = self.logo1).place(x = 100,y = 10)
        
        self.Nlabel = Label(self.window,text = 'NAME',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Nlabel.place(x = 70,y = 200)
        self.Plabel = Label(self.window,text = 'PERCENTAGE',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Plabel.place(x = 70,y = 250)
        self.Blabel = Label(self.window,text = 'BACKLOG',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Blabel.place(x = 70,y = 300)
        self.Ilabel = Label(self.window,text = 'INTERNSHIPS',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Ilabel.place(x = 70,y = 350)
        self.Flabel = Label(self.window,text = 'FIRST ROUND',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Flabel.place(x = 70,y = 400)
        self.Clabel = Label(self.window,text = 'COMMUNICATION SKILLS',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Clabel.place(x = 70,y = 450)
        
        self.Nentry = Entry(self.window,font = self.Lfont)
        self.Nentry.place(x = 400,y = 200)
        self.Pentry = Entry(self.window,font = self.Lfont)
        self.Pentry.place(x = 400,y = 250)
        self.Bentry = Entry(self.window,font = self.Lfont)
        self.Bentry.place(x = 400,y = 300)
        self.Ientry = Entry(self.window,font = self.Lfont)
        self.Ientry.place(x = 400,y = 350)
        self.Fentry = Entry(self.window,font = self.Lfont)
        self.Fentry.place(x = 400,y = 400)
        self.Centry = Entry(self.window,font = self.Lfont)
        self.Centry.place(x = 400,y = 450)
        
        self.LgButton = Button(self.window,text = 'Logistic Regression',width = 20,bg = '#0f56c6',fg = 'White',font = self.Lfont,command = self.logRegButton)
        self.LgButton.place(x = 700, y = 260)
        self.DtButton = Button(self.window,text = 'Decision Tree',width = 20,bg = '#0f56c6',fg = 'White',font = self.Lfont,command = self.DecisionTreeButton)
        self.DtButton.place(x = 700, y = 320)
        self.RfButton = Button(self.window,text = 'Random Forest',width = 20,bg = '#0f56c6',fg = 'White',font = self.Lfont,command = self.RandomForestButton)
        self.RfButton.place(x = 700, y = 380)
        self.SvButton = Button(self.window,text = 'SVM',width = 20,bg = '#0f56c6',fg = 'White',font = self.Lfont,command = self.SVMButton)
        self.SvButton.place(x = 700, y = 440)
        
        
        self.resultFrame = Frame(self.window)
        self.resultFrame.place(x = 400, y = 500)
        self.subLabel = Label(self.window,text = 'Result',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        #self.subLabel.grid(row = 0,column = 0)
        self.Lglabel = Label(self.window,text = 'Logistic Regression',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Dtlabel = Label(self.window,text = 'Decision Tree',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Rflabel = Label(self.window,text = 'Random Forest',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Svlabel = Label(self.window,text = 'SVM',bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        
        self.Lgvar = StringVar()
        self.Dtvar = StringVar()
        self.Rfvar = StringVar()
        self.Svvar = StringVar()
        
        self.Lgval = Label(self.window,textvariable = self.Lgvar,height = 1,width = 10,bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Dtval = Label(self.window,textvariable = self.Dtvar,height = 1,width = 10,bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Rfval = Label(self.window,textvariable = self.Rfvar,height = 1,width = 10,bg = '#FFBD33',fg = 'Black',font = self.Lfont)
        self.Svval = Label(self.window,textvariable = self.Svvar,height = 1,width = 10,bg = '#FFBD33',fg = 'Black',font = self.Lfont)
    
        self.load_data()
        self.upOn = False
        
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.window.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.window.attributes("-fullscreen", False)
        return "break"
        
    def load_data(self):
        self.df = pd.read_csv("PerpData.csv")
        features = list(self.df.columns[1:6])
        print(features)
        print(len(self.df))
        self.y = self.df['Hired']
        self.X = self.df[features]
        print(self.X)
        print(self.y)   
        
    def updateDb(self):
        print('Hello')
        self.upOn = True
        modellg = self.trainLogisticReg(self.X,self.y)
        modeldt = self.trainDecisionTree(self.X,self.y)
        modelrf = self.trainRandomForest(self.X,self.y)
        modelsv = self.trainSVM(self.X,self.y)
        
        name = self.Nentry.get()
        perc = int(self.Pentry.get())
        backlog = int(self.Bentry.get())
        internship = int(self.Ientry.get())
        frmks = int(self.Fentry.get())
        comm = int(self.Centry.get())
        myvals = [[perc,backlog,internship,frmks,comm]]
        self.res = []
        self.res.append(modellg.predict(myvals)[0])
        self.res.append(modeldt.predict(myvals)[0])
        self.res.append(modelrf.predict(myvals)[0])
        self.res.append(modelsv.predict(myvals)[0])
        
        print(self.res)
        try:
            fres = mode(self.res)
        except StatisticsError:
            fres = 1
            
        print(fres)
        myvals = myvals[0]
        myvals.append(fres)
        myvals.insert(0,name)
        print(myvals)
        self.df.loc[len(self.df)-1] = myvals
        self.df.to_csv('PerpData.csv',index=False)
                
    def HoN(self,val):
        if(val == 0):
            return 'Not Hired'
        else:
            return 'Hired'
        
        
        
    def logRegButton(self):
        self.subLabel.place(x = 400, y = 500)
        self.Lglabel.place(x = 100,y = 560)
        self.Lgval.place(x = 500,y = 560)
        if(not self.upOn):
            self.updateDb()
        self.Lgvar.set(self.HoN(self.res[0]))
        
        
    def DecisionTreeButton(self):
        self.subLabel.place(x = 400, y = 500)
        self.Dtlabel.place(x = 100,y = 600)
        self.Dtval.place(x = 500,y = 600)
        if(not self.upOn):
            self.updateDb()
        self.Dtvar.set(self.HoN(self.res[1]))
        
        
    def RandomForestButton(self):
        self.subLabel.place(x = 400, y = 500)
        self.Rflabel.place(x = 100,y = 640)
        self.Rfval.place(x = 500,y = 640)
        if(not self.upOn):
            self.updateDb()
        self.Rfvar.set(self.HoN(self.res[2]))
        
    def SVMButton(self):
        self.subLabel.place(x = 400, y = 500)
        self.Svlabel.place(x = 100,y = 680)
        self.Svval.place(x = 500,y = 680)
        if(not self.upOn):
            self.updateDb()
        self.Svvar.set(self.HoN(self.res[3]))
        
    
#window.geometry('1200x768')
obj = Hiring()
obj.window.mainloop()

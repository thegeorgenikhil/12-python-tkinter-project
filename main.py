from tkinter import * 
import webbrowser
import csv
import random



window=Tk()
window.title("Movie Reviewer")
window.iconbitmap("Logo.ico")
window.geometry("220x220")

def All():
    f=open("./excel/All.csv")
    mov_reader=csv.reader(f)
    L=[]
    Cust=0
    for rec in mov_reader:
        L.append(rec)
        Cust+=1
    A=random.randint(1,Cust)
    webbrowser.open(L[A][1])

def Malayalam():
    f=open("./excel/Malayalam.csv")
    mov_reader=csv.reader(f)
    L=[]
    Cust=0
    for rec in mov_reader:
        L.append(rec)
        Cust+=1
    A=random.randint(1,Cust)
    webbrowser.open(L[A][1])
    
def Tamil():
    f=open("./excel/Tamil.csv")
    mov_reader=csv.reader(f)
    L=[]
    Cust=0
    for rec in mov_reader:
        L.append(rec)
        Cust+=1
    A=random.randint(1,Cust)
    webbrowser.open(L[A][1])
    
def Hindi():
    f=open("./excel/Hindi.csv")
    mov_reader=csv.reader(f)
    L=[]
    Cust=0
    for rec in mov_reader:
        L.append(rec)
        Cust+=1
    A=random.randint(1,Cust)
    webbrowser.open(L[A][1])
    
def English():
    f=open("./excel/English.csv")
    mov_reader=csv.reader(f)
    L=[]
    Cust=0
    for rec in mov_reader:
        L.append(rec)
        Cust+=1
    A=random.randint(1,Cust)
    webbrowser.open(L[A][1])

def Other():
    f=open("./excel/Other.csv")
    mov_reader=csv.reader(f)
    L=[]
    Cust=0
    for rec in mov_reader:
        L.append(rec)
        Cust+=1
    A=random.randint(1,Cust)
    webbrowser.open(L[A][1])
    
Button1=Button(text="All",bg="white",borderwidth=5,width=10,font=("Times",10, "bold"),command=All)
Button2=Button(text="Malayalam",bg="white",borderwidth=5,width=10,font=("Times",10, "bold"),command=Malayalam)
Button3=Button(text="Tamil",bg="white",borderwidth=5,width=10,font=("Times",10, "bold"),command=Tamil)
Button4=Button(text="Hindi",bg="white",borderwidth=5,width=10,font=("Times",10, "bold"),command=Hindi)
Button5=Button(text="English",bg="white",borderwidth=5,width=10,font=("Times",10, "bold"),command=English)
Button6=Button(text="Other",bg="white",borderwidth=5,width=10,font=("Times",10, "bold"),command=Other)

Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
Button5.pack()
Button6.pack()



window.mainloop()

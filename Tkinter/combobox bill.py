from tkinter import *
from tkinter.ttk import Combobox
def quit():
    var.destroy()
balance=5000
var=Tk()
Label(var,text="Username").grid(row=0)
Label(var,text="Password").grid(row=1)
e1=Entry(var)
e1.grid(row=0,column=1)
e2=Entry(var,show="*")
e2.grid(row=1,column=1)
Button(var,text="Quit",command=quit).grid(row=2,column=2)
def onclick():
    root=Toplevel()
    l1=Label(root,text="Initial Balance : "+str(balance))
    l1.grid(row=0)
    Label(root,text="Amount").grid(row=1)
    e3=Entry(root)
    e3.grid(row=1,column=1)
    def deposit():
        global c
        c=balance+int(e3.get())
        l1.config(text="Final Balance : "+str(c))
    v=["Rent          200","Electricity 150","Food         100","Gas            500"]
    r=[200,150,100,500]
    cb=Combobox(root,value=v)
    cb.grid(row=2,column=1)
    def process():
        myobj=open("Billing amounts.txt","a")
        if(cb.get()==v[0]):
            global e
            e=c-r[0]
            myobj.write("\nFinal Balance : "+str(e))
        elif(cb.get()==v[1]):
            global f
            f=e-r[1]
            myobj.write("\nFinal Balance : "+str(f))
        elif(cb.get()==v[2]):
            global g
            g=f-r[2]
            myobj.write("\nFinal Balance : "+str(g))
        elif(cb.get()==v[3]):
            global h
            h=g-r[3]
            myobj.write("\nFinal Balance : "+str(h))
        myobj.close()
    Button(root,text="Deposit",command=deposit).grid(row=1,column=2)
    Button(root,text="Add",command=process).grid(row=2,column=2)
    Button(root,text="Close",command=quit).grid(row=0,column=2)
def clickwe():
    if(e1.get()=="web"):
        if(e2.get()=="1234"):
            myobj=open("Billing amounts.txt","w")
            myobj.write(e1.get())
            myobj.write(e2.get())
            onclick()
        else:
            quit()
    else:
        quit()
b1=Button(var,text="Login",command=clickwe)
b1.grid(row=2,column=1)

from tkinter import *
def quit():
    var.destroy()
balance=5000
var=Tk()
Label(var,text="ATM").grid(column=1)
Label(var,text="Username").grid(row=1)
Label(var,text="Password").grid(row=2)
e1=Entry(var)
e1.grid(row=1,column=1)
e2=Entry(var,show="*")
e2.grid(row=2,column=1)
Button(var,text="Quit",command=quit).grid(row=3,column=2)
def onclick():
    root=Toplevel()
    l1=Label(root,text="Initial Balance : "+str(balance))
    l1.grid(row=0)
    Label(root,text="Amount").grid(row=1)
    e1=Entry(root)
    e1.grid(row=1,column=1)
    def deposit():
        c=balance+int(e1.get())
        l1.config(text="Final Balance : "+str(c))
    def withdraw():
        if(int(e1.get())<=balance):
            c=balance-int(e1.get())
            l1.config(text="Final Balance : "+str(c))
        else:
            l6=Label(root,text="Transaction not possible")
            l6.grid(row=4,column=1)
    Button(root,text="Deposit",command=deposit).grid(row=2)
    Button(root,text="Withdraw",command=withdraw).grid(row=2,column=1)
    Button(root,text="Close",command=quit).grid(row=5,column=2)
def clickwe():
    if(e1.get()=="web"):
        if(e2.get()=="1234"):
            onclick()
        else:
            quit()
    else:
        quit()
b1=Button(var,text="Login",command=clickwe)
b1.grid(row=3,column=1)

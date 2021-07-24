from tkinter import *
import mysql.connector
def quit():
    var.destroy()
balance=5000
var=Tk()
f=IntVar()
f1=IntVar()
Label(var,text="ATM").grid(column=1)
Label(var,text="Username").grid(row=1)
Label(var,text="Password").grid(row=2)
e1=Entry(var)
e1.grid(row=1,column=1)
e2=Entry(var,show="*")
e2.grid(row=2,column=1)
Button(var,text="Quit",command=quit).grid(row=3,column=2)
def data():
    my=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="atmsql")
    mycur=my.cursor()
    mycur.execute("INSERT INTO T3(Initial_Balance,Amount,Final_Balance) values(%s,%s,%s)",(balance,f.get(),f1.get()))
    my.commit()
    my.close()
def onclick():
    roots=Toplevel()
    l1=Label(roots,text="Initial Balance : "+str(balance))
    l1.grid(row=0)
    Label(roots,text="Amount").grid(row=1)
    e1=Entry(roots,textvariable=f)
    e1.grid(row=1,column=1)
    def deposit():
        c=balance+int(e1.get())
        l1.config(text="Final Balance : "+str(c))
    def withdraw():
        if(int(e1.get())<=balance):
            c=balance-int(e1.get())
            l1.config(text="Final Balance : "+str(c))
        else:
            l6=Label(roots,text="Transaction not possible")
            l6.grid(row=4,column=1)
    Button(roots,text="Deposit",command=deposit).grid(row=2)
    Button(roots,text="Withdraw",command=withdraw).grid(row=2,column=1)
    Button(roots,text="Close",command=quit).grid(row=5,column=2)
    b1=Button(roots,text="Submit",command=data)
    b1.grid(row=4,column=2)
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

from tkinter import *
import mysql.connector
root=Tk()
f=StringVar()
f1=StringVar()
f2=StringVar()
f3=StringVar()
i=IntVar()
j=IntVar()
l1=Label(root,text="First Name")
l2=Label(root,text="Last Name")
l3=Label(root,text="Roll no.")
l4=Label(root,text="Contact no.")
l5=Label(root,text="Gender")
l6=Label(root,text="Course")
r1=Radiobutton(root,text="Male",value=1,variable=i)
r2=Radiobutton(root,text="Female",value=2,variable=i)
c1=Checkbutton(root,text="C",onvalue=1,variable=j)
c2=Checkbutton(root,text="C++",onvalue=2,variable=j)
c3=Checkbutton(root,text="Python",onvalue=3,variable=j)
l1.grid(row=0)
l2.grid(row=0,column=2)
l3.grid(row=1)
l4.grid(row=1,column=2)
l5.grid(row=2)
l6.grid(row=3)
r1.grid(row=2,column=1)
r2.grid(row=2,column=2)
c1.grid(row=3,column=1)
c2.grid(row=3,column=2)
c3.grid(row=3,column=3)
e1=Entry(root,textvariable=f)
e2=Entry(root,textvariable=f2)
e3=Entry(root,textvariable=f3)
e4=Entry(root,textvariable=f1)
e1.grid(row=0,column=1)
e2.grid(row=0,column=3)
e3.grid(row=1,column=1)
e4.grid(row=1,column=3)
def data():
    my=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="reg")
    mycur=my.cursor()
    mycur.execute("INSERT INTO T2(first_name,last_name,phone,E_Mail,gender,course) values(%s,%s,%s,%s,%s,%s)",(f.get(),f1.get(),f3.get(),f2.get(),i.get(),j.get()))
    my.commit()
    my.close()
b1=Button(root,text="Submit",command=data)
b1.grid(row=4,column=2)

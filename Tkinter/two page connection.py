from tkinter import *
def quit():
    var.destroy()
var=Tk()
Label(var,text="Login Page").grid(row=0,column=2)
Label(var,text="Username").grid(row=1,column=1)
Label(var,text="Password").grid(row=2,column=1)
e1=Entry(var)
e2=Entry(var,show="*")
e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
Button(var,text="Quit",command=quit).grid(row=3,column=2)
def onclick():
    print(e1.get())
    print(e2.get())
    root=Toplevel()
    i=IntVar()
    j=IntVar()
    def official():
        print(e11.get(),e12.get(),e13.get(),e14.get())
        quit()
    if(i.get()==1):
        print("Male")
    elif(i.get()==2):
        print("Female")
    if(j.get()==1):
        print("C")
    elif(j.get()==2):
        print("C++")
    elif(j.get()==3):
        print("Python")
    Label(root,text="First Name").grid(row=0)
    Label(root,text="Last Name").grid(row=0,column=2)
    Label(root,text="Roll no.").grid(row=1)
    Label(root,text="Contact no.").grid(row=1,column=2)
    Label(root,text="Gender").grid(row=2)
    Label(root,text="Course").grid(row=3)
    Radiobutton(root,text="Male",value=1,variable=i).grid(row=2,column=1)
    Radiobutton(root,text="Female",value=2,variable=i).grid(row=2,column=2)
    Checkbutton(root,text="C",onvalue=1,variable=j).grid(row=3,column=1)
    Checkbutton(root,text="C++",onvalue=2,variable=j).grid(row=3,column=2)
    Checkbutton(root,text="Python",onvalue=3,variable=j).grid(row=3,column=3)
    e11=Entry(root)
    e12=Entry(root)
    e13=Entry(root)
    e14=Entry(root)
    e11.grid(row=0,column=1)
    e12.grid(row=0,column=3)
    e13.grid(row=1,column=1)
    e14.grid(row=1,column=3)
    Button(root,text="Submit",command=official).grid(row=4,column=2)
def clickwe():
    if(e1.get()=="web"):
        if(e2.get()=="1234"):         
            onclick()
        else:
            quit()
    else:
        quit()
b1=Button(var,text="Submit",command=clickwe).grid(row=3,column=1)

from tkinter import *
var=Tk()
def clickme():
    a=list.curselection()
    print(a)
    for i in a:
        print(list.get(i))
list=Listbox(var,selectmode=EXTENDED)
list.pack()
b1=Button(var,text="SUBMIT",command=clickme)
b1.pack()
list.insert(1,"java")
list.insert(2,"python")
list.insert(3,"c++")
list.insert(4,"c")
var.mainloop()

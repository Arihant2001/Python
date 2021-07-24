from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
root=Tk()
Label(root,text="hello tkinter").pack()
messagebox.showinfo("welcome","welcome to tkinter program")
name=simpledialog.askstring("name","what is your name")
age=simpledialog.askinteger("age","what is your age")
output="your name is {} \n andd your age is {} years old.".format(name,age)
output+="\n\t Thank you using this program"
messagebox.showinfo("results",output)

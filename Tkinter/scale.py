from tkinter import *
def select():
    sel="value="+str(v.get())
    label.config(text=sel)
root=Tk()
root.geometry("200x100")
v=DoubleVar()
scale=Scale(root,variable=v,from_=1,to=50,orient=HORIZONTAL)
scale.pack()
bt1=Button(root,text="slider value",command=select)
bt1.pack()
label=Label(root)
label.pack()

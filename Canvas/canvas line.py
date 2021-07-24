from tkinter import *
root=Tk()
can=Canvas(root,width=200,height=200)
can.pack()
line1=can.create_line(0,0,200,100)
line2=can.create_line(200,100,0,200,fill="red")
root.mainloop()

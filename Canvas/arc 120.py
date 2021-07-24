from tkinter import *
root=Tk()
Canvas=Canvas(root,width=400,height=400,bg="blue")
Canvas.pack()
Canvas.create_arc(100,100,200,200,extent=120)
root.mainloop()

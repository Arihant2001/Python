from tkinter import *
root=Tk()
root.geometry("200x200")
root.title("scale")
sb=Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)
listbox=Listbox(root,yscrollcommand=sb.set)
for i in range(100):
    listbox.insert(END,"number"+str(i))
listbox.pack(side=LEFT)
sb.config(command=listbox.yview)
root.mainloop()
    

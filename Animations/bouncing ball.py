from tkinter import *
import random
import time
tk=Tk()
c=Canvas(tk,width=800,height=600)
tk.title("drawing")
c.pack()
ball=c.create_oval(10,10,60,60,fill="orange")
xspeed=2
yspeed=1
while True:
    c.move(ball,xspeed,yspeed)
    pos=c.coords(ball)
    if pos[3]>=600 or pos[1]<=0:
        yspeed=-yspeed
    if pos[2]>=800 or pos[0]<=0:
        xspeed=-xspeed
    tk.update()
    time.sleep(0.01)
tk.mainloop()
    

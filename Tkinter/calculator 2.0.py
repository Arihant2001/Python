from tkinter import *
root=Tk()
operator=""
def clickme(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
def clrdisplay():
    global operator
    operator=""
    text_Input.set("")
def equals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
text_Input=StringVar()
Entry(root,textvariable=text_Input).grid(row=0,columnspan=4)
Button(root,text="1",command=lambda:clickme(1)).grid(row=1)
Button(root,text="2",command=lambda:clickme(2)).grid(row=1,column=1)
Button(root,text="3",command=lambda:clickme(3)).grid(row=1,column=2)
Button(root,text="4",command=lambda:clickme(4)).grid(row=1,column=3)
Button(root,text="5",command=lambda:clickme(5)).grid(row=2)
Button(root,text="6",command=lambda:clickme(6)).grid(row=2,column=1)
Button(root,text="7",command=lambda:clickme(7)).grid(row=2,column=2)
Button(root,text="8",command=lambda:clickme(8)).grid(row=2,column=3)
Button(root,text="9",command=lambda:clickme(9)).grid(row=3)
Button(root,text="0",command=lambda:clickme(0)).grid(row=3,column=1)
Button(root,text="C",command=clrdisplay).grid(row=3,column=2)
Button(root,text="=",command=equals).grid(row=3,column=3)
Button(root,text="+",command=lambda:clickme("+")).grid(row=4)
Button(root,text="-",command=lambda:clickme("-")).grid(row=4,column=1)
Button(root,text="*",command=lambda:clickme("*")).grid(row=4,column=2)
Button(root,text="/",command=lambda:clickme("/")).grid(row=4,column=3)

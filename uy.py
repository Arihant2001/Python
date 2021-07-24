from tkinter import *
root=Tk()
Label(root,text="Age Calculator",fg="green").grid(column=2,columnspan=2)
Label(root,text="dd").grid(row=1,column=1)
Label(root,text="mm").grid(row=1,column=3)
Label(root,text="yyyy").grid(row=1,column=5)
Label(root,text="Present Date").grid(row=2)
Label(root,text="Present Month").grid(row=2,column=2)
Label(root,text="Present Year").grid(row=2,column=4)
Label(root,text="Date").grid(row=3)
Label(root,text="Month").grid(row=3,column=2)
Label(root,text="Year").grid(row=3,column=4)
Button(root,text="Quit",fg="red",command=quit).grid(row=4,column=6)
def clickwe():
    nod=((int(e3.get())-int(e6.get()))*365)+((int(e2.get())-int(e5.get()))*30)+(int(e1.get())-int(e4.get()))
    Label(root,text=str(nod)).grid(row=5,columnspan=2)
    Label(root,text="Days").grid(row=6,columnspan=2)
    years=int(nod/365),
    yearst=nod/365
    extradays=nod%365
    months=int(extradays/30)
    days=extradays%30
    Label(root,text=str(years)+" Years "+str(months)+" Months "+str(days)+" Days OR "+str(yearst)+" Years").grid(row=5,column=2,columnspan=2)
    Label(root,text="Age").grid(row=6,column=2,columnspan=2)
    if(int(e4.get())==9 and int(e5.get())==1 and int(e6.get())==1978):
        Label(root,text="MUMMY,").grid(row=5,column=4)
    elif(int(e4.get())==26 and int(e5.get())==1 and int(e6.get())==1946):
        Label(root,text="NANA JI,").grid(row=5,column=4,columnspan=2)
    elif(int(e4.get())==18 and int(e5.get())==2 and int(e6.get())==2003):
        Label(root,text="MAHAVEER,").grid(row=5,column=4,columnspan=2)
    elif(int(e4.get())==1 and int(e5.get())==3 and int(e6.get())==2001):
        Label(root,text="SHARU,").grid(row=5,column=4,columnspan=2)
    elif(int(e4.get())==9 and int(e5.get())==7 and int(e6.get())==2002):
        Label(root,text="KANNU,").grid(row=5,column=4,columnspan=2)
    elif(int(e4.get())==8 and int(e5.get())==9 and int(e6.get())==1973):
        Label(root,text="PAPA,").grid(row=5,column=4,columnspan=2)
    if(extradays==0):
        Label(root,text="VERY HAPPY B'DAY").grid(row=6,column=4,columnspan=2)
    else:
        bdtc=365-extradays
        bdtcm=int(bdtc/30)
        bdtcd=bdtc%30
        Label(root,text=str(bdtcm)+" Months "+str(bdtcd)+" Days").grid(row=5,column=5)
        Label(root,text="Next Birthday").grid(row=6,column=5)
b1=Button(root,text="OK",fg="blue",command=clickwe)
b1.grid(row=4,column=3)

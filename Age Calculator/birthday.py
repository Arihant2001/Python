from tkinter import *
root=Tk()
root.title("Age Calculator")
Label(root,text="dd").grid(row=0,column=1)
Label(root,text="mm").grid(row=0,column=3)
Label(root,text="yyyy").grid(row=0,column=5)
Label(root,text="Present Date").grid(row=1)
Label(root,text="Present Month").grid(row=1,column=2)
Label(root,text="Present Year").grid(row=1,column=4)
Label(root,text="Date").grid(row=2)
Label(root,text="Month").grid(row=2,column=2)
Label(root,text="Year").grid(row=2,column=4)
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)
e6=Entry(root)
e1.grid(row=1,column=1)
e2.grid(row=1,column=3)
e3.grid(row=1,column=5)
e4.grid(row=2,column=1)
e5.grid(row=2,column=3)
e6.grid(row=2,column=5)
Button(root,text="Quit",command=quit).grid(row=3,column=6)
def clickwe():
    nod=((int(e3.get())-int(e6.get()))*365)+((int(e2.get())-int(e5.get()))*30)+(int(e1.get())-int(e4.get()))
    print("No. of days u have lived = "+str(nod))
    years=int(nod/365)
    yearst=nod/365
    extradays=nod%365
    months=int(extradays/30)
    days=extradays%30
    print("Your Age is "+str(years)+" Years "+str(months)+" Months "+str(days)+" Days OR "+str(yearst)+" Years")
    if(int(e4.get())==9 and int(e5.get())==1 and int(e6.get())==1978):
        print("MUMMY,",end=" ")
    elif(int(e4.get())==26 and int(e5.get())==1 and int(e6.get())==1946):
        print("NANA JI,",end=" ")
    elif(int(e4.get())==18 and int(e5.get())==2 and int(e6.get())==2003):
        print("MAHAVEER,",end=" ")
    elif(int(e4.get())==1 and int(e5.get())==3 and int(e6.get())==2001):
        print("SHARU,",end=" ")
    elif(int(e4.get())==9 and int(e5.get())==7 and int(e6.get())==2002):
        print("KANNU,",end=" ")
    elif(int(e4.get())==8 and int(e5.get())==9 and int(e6.get())==1973):
        print("PAPA,",end=" ")
    if(extradays==0):
        print("VERY HAPPY B'DAY")
    else:
        bdtc=365-extradays
        bdtcm=int(bdtc/30)
        bdtcd=bdtc%30
        print("Your Birthday will come in "+str(bdtcm)+" Months "+str(bdtcd)+" Days")
b1=Button(root,text="OK",command=clickwe)
b1.grid(row=3,column=3)

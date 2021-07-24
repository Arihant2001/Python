class bank:
    bankname="PNB"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("updated balance is : ",self.balance)
    def withdrawl(self,amt):
        if(amt>self.balance):
            print("insufficient funds")
        else:
            self.balance=self.balance-amt
            print("updated balance is : ",self.balance)
name=input("enter customer name : \n")
c=bank(name)
while(True):
    print("1.withdrawl\n2.deposit\n")
    choice=int(input())
    if(choice==1):
        amt=float(input("enter amount : "))
        c.withdrawl(amt)
    elif(choice==2):
        amt=float(input("enter amount : "))
        c.deposit(amt)
    else:
        print("invalid choice")

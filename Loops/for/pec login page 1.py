n=int(input("WELCOME TO PEC LOGIN PAGE\n1. LOGIN or 2. SIGN UP : "))
usn=["a","arihant","electronics","computer"]
pasw=["m","jain","don","expert"]
if(n==1):
    username=str(input("Enter Username : "))
    if username in usn:
     c=usn.index(username)
     for i in range(0,3):
          password=str(input("Enter Password : "))
          if password in pasw:
             d=pasw.index(password)
             if(c==d):
                print("Welcome to PEC")
                break
             else:
                print("Incorrect Password for Username")
          else:
             print("Incorrect Password")
    else:
        print("invalid username")
elif(n==2):
    newusn=str(input("Enter Username : "))
    if newusn in usn:
        print("Username already exists. Please login")
    else:
        usn.append(newusn)
        newpasw=input("Enter Password : ")
        pasw.append(newpasw)
        print(usn)
       
      

usn=str(input("WELCOME TO PUNJAB ENGINEERING COLLEGE LOGIN PAGE\nUsername : "))
if(usn=="arihant" or usn=="electronics"):
     for i in range(1,4):
         p=str(input("Password : "))
         if(p=="jain" or p=="student"):
          print("You have access to your account")
          break
         elif(i<3):
          print("Incorrect password")
         else:
          print("Incorrect password. Your account is locked")
else:
    print("Incorrect Username. Your account is locked")


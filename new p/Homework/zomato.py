print("WELCOME TO ZOMATO\n1. Chinese\n2. Indian\n3. Western\n4. Desserts")
dish=int(input("Enter Dish number : "))
if(dish==1):
    print("CHINESE\n1. Noodles        150\n2. Manchurian     100\n3. Pasta          125\n4. Momos          50")
    b=int(input("Enter Item number : "))
    if(b==1):
     c=1
    elif(b==2):
     c=2
    elif(b==3):
     c=3
    elif(b==4):
     c=4
    else:
     print("Enter Item number as 1,2,3 or 4 only")
    #r1=[150,100,125,50]
elif(dish==2):
    print("Indian\n1. Dal       150\n2. Roti      300\n3. Paneer    200\n4. Rice      250")
    b=int(input("Enter Item number : "))
    if(b==1):
     c=5
    elif(b==2):
     c=6
    elif(b==3):
     c=7
    elif(b==4):
     c=8
    else:
     print("Enter Item number as 1,2,3 or 4 only")
    #r2=[150,300,200,250]
elif(dish==3):
    print("Western\n1. Macroni   110\n2. Hotdog    90\n3. Burgur    60\n4. Pizza     250")
    b=int(input("Enter Item number : "))
    if(b==1):
     c=9
    elif(b==2):
     c=10
    elif(b==3):
     c=11
    elif(b==4):
     c=12
    else:
     print("Enter Item number as 1,2,3 or 4 only")
    #r3=[110,90,60,250]
elif(dish==4):
    print("Desserts\n1. Rasgulla       20\n2. Gajrella       50\n3. Ice cream      80\n4. Shake          70")
    b=int(input("Enter Item number : "))
    if(b==1):
     c=13
    elif(b==2):
     c=14
    elif(b==3):
     c=15
    elif(b==4):
     c=16
    else:
     print("Enter item number as 1,2,3 or 4 only")
    #r4=[20,50,80,70]
else:
     print("No such case")
#d=[r1[b-1],r2[b-1],r3[b-1],r4[b-1]]
r=[150,100,125,50,150,300,200,250,110,90,60,250,20,50,80,70]
print("Billing amount = "+str(r[c-1]))
#print("billing amount is "+str(d[dish-1]))
code=str(input("Codes available : ZOM40, ZOM50. Enter Promo code : "))
if(code=="ZOM40"):
    nr=0.4*(int(r[c-1]))
    print("Amount payable = Rs. "+str(nr))
elif(code=="ZOM50"):
    nr=0.5*(int(r[c-1]))
    print("Amount payable = Rs. "+str(nr))
else:
    print("No such code")
print("*book* or *home delivery* (Rs. 60 extra) ?")
ans=str(input("What do you prefer : "))
if(ans=="book"):
    print("Your item has been booked. Address : SCO 200, Sector 35C")
elif(ans=="home delivery"):
    address=str(input("Enter your Address = "))
    ta=nr+60
    print("Total amount payable = Rs. "+str(ta))
else:
    print("No other option available")

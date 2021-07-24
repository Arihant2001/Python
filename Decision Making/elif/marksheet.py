print("student marksheet")
marks=float(input("enter marks : "))
if(100>=marks>90):
    print("grade A")
elif(90>=marks>80):
    print("grade B")
elif(80>=marks>70):
    print("grade C")
elif(70>=marks>60):
    print("grade D")
elif(60>=marks>50):
    print("grade E")
else:
    print("fail")

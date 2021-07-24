n=int(input("enter number to know its factors = "))
print("factors of "+str(n)+" are : ")
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")

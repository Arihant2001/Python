a=0
b=1
for i in range(0,8):
    if(i<=1):
        sum=i
    else:
        sum=a+b
        a=b
        b=sum
    print(sum)

myobj=open("arihant.txt","r")
while True:
    line=myobj.readline()
    if len(line)==0:
        break
    print(line)

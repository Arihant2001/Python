import time
for i in range(1,2):
    for j in range(1,24):
        if(j==18 or j==19 or j==21 or j==22):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
time.sleep(1)
for i in range(2,3):
    for j in range(1,24):
        if(j==17 or j==20 or j==23):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
time.sleep(1)
for i in range(3,4):
    for j in range(1,24):
        if(j==17 or j==23):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
time.sleep(1)
for i in range(4,5):
    for j in range(1,24):
        if(j==18 or j==22):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
time.sleep(1)
for i in range(5,6):
    for j in range(1,24):
        if(j==19 or j==21):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
time.sleep(1)
for i in range(6,7):
    for j in range(1,24):
        if(j==20):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
time.sleep(5)

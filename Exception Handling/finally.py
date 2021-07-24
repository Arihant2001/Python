try:
    a=20/0
    print("exception occured")
finally:
    print("code to be executed")
    a=20/2
    print(a)
    

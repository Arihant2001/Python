def hello(a,*vartuple):
    print(a)
    for var in vartuple:
        print(var)
    return
hello(10)
hello(10,20,30,40)

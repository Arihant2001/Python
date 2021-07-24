try:
    a=10
    print(a)
raise NameError("hello")
except NameError as e:
    print("exception occurs")
    print e

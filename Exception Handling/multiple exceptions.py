try:
    a=20/0
except ArithmeticError:
    print("arithmetic error")
else:
    print(a)

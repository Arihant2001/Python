try:
    a=20/0
    print(a)
except ArithmeticError:
    print("number is not divisible by 0")

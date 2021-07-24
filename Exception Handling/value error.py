try:
    age=int(input("enter age : "))
    if(age<18):
        raise ValueError;
    else:
        print("age is valid")
except ValueError:
    print("age isn't valid")
            

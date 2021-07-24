print("blood donation camp")
age=int(input("enter age : "))
if(age>=18):
    wgt=int(input("enter weight : "))
    if(wgt>=50):
        print("eligible for blood donation")
    else:
        print("not eligible due to less weight")
else:
    print("not eligible dut to less age")

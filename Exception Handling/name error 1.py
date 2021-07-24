try:
    f=open("file 1.txt","r")
    f.close()
except IOError:
    print("error : can't find file")
else:
    print("written content in file successfully")

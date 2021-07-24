try:
    f=open("file.txt","w")
    f.write("thus is my test file")
    f.close()
except IOError:
    print("error : can't find file")
else:
    print("content written in file successfully")

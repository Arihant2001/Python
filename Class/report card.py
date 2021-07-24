class student:
    def getstudent(self):
        self.name=input("name : ")
        self.age=input("age : ")
        self.gender=input("gender : ")
class test(student):
    def getmarks(self):
        self.stuclass=input("class")
        print("enter marks of respective subjects : ")
        self.literature=int(input("literature : "))
        self.maths=int(input("maths : "))
        self.biology=int(input("biology : "))
        self.physics=int(input("physics : "))
class marks(test):
    def display(self):
        print("\nname : ",self.name)
        print("age : ",self.age)
        print("gender : ",self.gender)
        print("study in : ",self.stuclass)
        print("total marks : ",self.literature+self.maths+self.biology+self.physics)
m1=marks()
m1.getstudent()
m1.getmarks()
m1.display()

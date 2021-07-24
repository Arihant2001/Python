class person:
    def display(self):
        print("hello,this is class person")
class employee(person):
    def printing(self):
        print("hello,this is derived class employee")
class programmer(employee):
    def show(self):
        print("hello,this is another derived class program")
p1=programmer()
p1.display()
p1.printing()
p1.show()

class A:
    def display(self):
        print("method belongs to class A")
class B(A):
    pass
b1=B()
b1.display()

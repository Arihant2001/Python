class student:
    clg='xyz'
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def display(self):
        print("student name : ",self.name)
        print("student roll no : ",self.rollno)
        print("college : ",student.clg)
student1=student('xyz 001',"arihant")
student1.display()
student2=student('xyz 056',"bro")
student2.display()

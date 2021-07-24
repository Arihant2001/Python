class land_animal:
    def printing(self):
        print("animal lives on land")
class water_animal:
    def display(self):
        print("animal lives in water")
class frog(land_animal,water_animal):
    pass
f1=frog()
f1.printing()
f1.display()
        

class dog:
    def sound(self):
        print("bow bow")
class cat:
    def sound(self):
        print("meow")
def makesound(animaltype):
    animaltype.sound()
catobj=cat()
dogobj=dog()
makesound(catobj)
makesound(dogobj)

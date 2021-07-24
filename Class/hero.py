class movie:
    def __init__(self,name,hero,heroine):
        self.name=name
        self.hero=hero
        self.heroine=heroine
    def display(self):
        print("Movie name : ",self.name)
        print("Hero : ",self.hero)
        print("Heroine : ",self.heroine)
movies=[]
n=int(input("Enter the number of movies : "))
for i in range(n):
    name=input("enter movie name : ")
    hero=input("enter hero name : ")
    heroine=input("enter heroine name : ")
    m=movie(name,hero,heroine)
    movies.append(m)
for movie in movies:
    movie.display()

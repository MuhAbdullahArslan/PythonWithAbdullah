class Movie:
    def __init__(self,title,time,hero):
        self.title = title
        self.time = time
        self.hero = hero
        
    def printer(self):
        print(f"Name of movie is {self.title}\nRunTime of movie is: {self.time}\nHero of movie is: {self.hero}")
    
list_of_moives = []   
while True:
    title = input("Enter the title of Movie:")
    time = input("Enter the Runtime of Movie:")
    hero = input("Enter the Hero name of Movie:")
    m1 = Movie(title,time,hero)
    list_of_moives.append(m1)
    ans = input("Do you want to continue(y/n)")
    if ans!= 'y':
        break

for movie_info in list_of_moives:
    movie_info.printer()
    
# Mini movie program


class Movie:
    '''Movie class for oops concept practice'''

    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print("Movie Name : ", self.title)
        print("Hero Name : ", self.hero)
        print("Heroine Name : ", self.heroine)

# m = Movie('Bahubali', 'Prabhas', 'Anushka')

list_of_movies = []

while True :
    title = input('Enter Movie Name : ')
    hero = input('Enter Hero Name : ')
    heroine = input('Enter heroine Name : ')

    m = Movie(title, hero, heroine)
    list_of_movies.append(m)
    print('Movie added to the list successfully')

    option = input('Do you want ot add one more movie [Yes | No]: ')
    if option.lower() == 'no' :
        break

print('All movies information ...')
print('#'*30)

for movie in list_of_movies:
    movie.info()
    print()
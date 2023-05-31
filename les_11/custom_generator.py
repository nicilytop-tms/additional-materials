def cart():
    yield 'iphone'
    yield 'macbook'
    yield 'airpods'


cart_generator = cart()
print(type(cart_generator), end='\n'+'*'*80+'\n')

print(next(cart_generator))
print(next(cart_generator))
print(next(cart_generator))
# print(next(cart_generator))


# when iterator is generator ->

class User:
    def __init__(self, name, password, age, nationality):
        self.name = name
        self.password = password
        self.age = age
        self.nationality = nationality
        self.gen = self.__gen()

    def __iter__(self):
        return self.gen

    def __gen(self):
        yield self.name
        yield self.password
        yield self.age
        yield self.nationality

    def __next__(self):
        return self.gen


alex = User('Alex', 'alskj93sdf', 30, 'Belarus')

for prop in alex:
    print(prop)

class Animal:
    def __float__(self):
        print('This method should return float')
        return 2.3


an = Animal()
x = float(an) + 1
print(x)


class Person:
    def __init__(self, age):
        self.age = age

    def __gt__(self, other):
        return self.age < other.age


vasya = Person(12)
dima = Person(13)

print(vasya > dima)

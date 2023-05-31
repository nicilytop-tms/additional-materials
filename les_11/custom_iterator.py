class User:
    def __init__(self, name, password, age, nationality):
        self.name = name
        self.password = password
        self.age = age
        self.nationality = nationality

        self.properties = self.name, self.password, self.age, self.nationality
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.properties[self.counter]
        except IndexError:
            self.counter = 0
            raise StopIteration

        self.counter += 1
        return result


alex = User('Alex', 'Hjks8320djsdf', 30, 'Belarus')
john = User('John', 'Hjks8320sadfdjsdf', 32, 'USA')
sam = User('Sam', 'asdfddf', 19, 'Belarus')

users = [alex, john, sam]

for user in users:
    for prop in user:
        print(prop)


for i in alex:
    print(i)

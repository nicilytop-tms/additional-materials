class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def print_name(self):
        print(self.name)

    def print_breed(self):
        print(self.breed)

    @classmethod
    def create_from_str(cls, data: str):
        name, breed = data.split('.')
        return cls(name, breed)


jastin = Dog('Jastin', 'shitzu')
jastin.print_name()
jastin.print_breed()

bobik = Dog.create_from_str('Bobik.husky')
bobik.print_name()
bobik.print_breed()

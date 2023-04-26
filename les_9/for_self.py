vitya = None


class User:
    def __init__(self, name):
        self.name = name

    def who_is_here(self):
        print(f'Here is {self}')
        global vitya
        vitya = self


dima = User('dima')

print(vitya)
dima.who_is_here()
print(vitya is dima)

#######################################################################################################################


class User:
    def __init__(self, name):
        self.name = name
        self.age = 12

    def print_all_ags_of_object(self):
        print(self.name, self.age)


dima = User('dima')
vitya = User('vitya')

User.print_all_ags_of_object(dima)
User.print_all_ags_of_object(vitya)

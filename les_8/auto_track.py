class Auto:
    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def __technical_service(self):
        print('Service approved')


class Truck(Auto):
    def __init__(self, max_load, brand, age, mark):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        super().__technical_service()
        print('move')


big_truck = Truck(3, 'Reno', 12, 'ddd')
big_truck.move()



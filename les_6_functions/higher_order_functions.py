from functools import reduce


def peter():
    print(peter.__name__)


def victor():
    print(victor.__name__)


def dmitry():
    print(dmitry.__name__)


def launch_it_n_time(func, n):
    for i in range(n):
        func()


launch_it_n_time(dmitry, 4)
#################################################################################################


names = ('yan', 'dima', 'Nicolas', 'John', 'Yarick', 'Tom', 'Elena')

filtered_names = filter(lambda name: len(name) > 4, names)
print(tuple(filtered_names))
#################################################################################################


list_of_numbers = [1, 2, 3, 4, 5, 5, 6, 2, 3, 4, 23, 20]

new_dict = {}


list(map(lambda x: new_dict.update({x: 'четное' if x % 2 == 0 else 'нечетное'}), list_of_numbers))
print(new_dict)
#################################################################################################


result = list(reduce(lambda prev, curr: prev + curr, ['H', 'e', 'l', 'l', 'o']))
print(result)

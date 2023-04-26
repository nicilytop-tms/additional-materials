"""
Swap key with value
"""
name_password_dict = {
    'name': 'password'
}
password_name_dict = {
    list(name_password_dict.values())[0]: list(name_password_dict.keys())[0]
}

# or

password_name_dict_1 = {v: k for k, v in name_password_dict.items()}
# this is a dictionary generator. more here: https://pyprog.pro/python/py/dict/dict_generators.html

"""
Here we can count of elements into our list input_list
"""
input_list = [1, 2, 4, 5, 4, 5, 5, 6, 7, 34]

result = {}
for el in input_list:
    result[el] = result.get(el, 0) + 1


"""
Different ways of writing a recursive function
"""


def factorial(i):
    return factorial(i - 1) * i if i > 1 else i

# or


def factorial_1(i):
    return i if i == 1 else factorial_1(i - 1) * i

# or


def factorial_2(i):
    if i == 1:
        return i
    return i * factorial_2(i - 1)

user_names = ['Alex', 'John', 'Bob', 'Robert']


iterator_by_users = iter(user_names)
print(iterator_by_users)

for name in iterator_by_users:  # Возвращает итерируемый объект (делает -> iter(user_names))
    print(name)

print('#'*80)

list  # попробуем найти внутри __iter__ __next__ методы

for at in user_names.__dir__():
    if at.startswith('__next__') or at.startswith('__iter__'):
        print(at, 'was wound!')

print('#'*80)

for at in iter(user_names).__dir__():
    if at.startswith('__next__') or at.startswith('__iter__'):
        print(at, 'was wound!')


next(user_names)

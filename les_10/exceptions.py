a = int(input(' a: '))
b = int(input(' b: '))
try:
    result = a / b
    b = [1,2,3,4]
    print(b[4])
except ZeroDivisionError as err:
    print(f'b is zero {err}!!!')
except Exception as err:
    print(f'SOMETHING WRONG {err}!!!')
else:
    print(' Ошибки не было')
finally:
    print('сработает всегда')


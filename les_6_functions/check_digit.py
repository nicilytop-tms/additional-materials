def _already_has_dot(ch, is_float):
    return ch == '.' and is_float


def own_is_digit(data):
    numbers_list = '0123456789.'
    is_negative, is_float = '-' == data[0], False

    for ch in data[1:] if is_negative else data:
        if _already_has_dot(ch, is_float) or ch not in numbers_list:
            return 'This is wrong number'

        is_float = ch == '.' or is_float

    return f'This is {"negative" if is_negative else "positive"} {"fractional number" if is_float else "integer"}'


own_is_digit('00098323')

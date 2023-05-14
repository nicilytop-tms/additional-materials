import re


def multiplication(a, b):
    return a * b


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def division(a, b):
    return a / b


regular_expressions = {
    r'\d+\s\*\s\d+': multiplication,
    r'\d+\s\+\s\d+': addition,
    r'\d+\s\-\s\d+': subtraction,
    r'\d+\s\/\s\d+': division,
}


def calculate(exp):
    for reg_exp, do in regular_expressions.items():
        if re.match(reg_exp, exp):
            a, _, b = exp.split(' ')
            return do(float(a), float(b))


expression = input()
result = calculate(expression)


print(result)

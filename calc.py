def add(x, y):
    x + y


def subtract(x, y):
    pass


def multiply(x, y):
    x * y


def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x // y

def add_number(x):
    return x*90

def twice(func, arg):
    return func(func(arg))

print(twice(add_number, 12))

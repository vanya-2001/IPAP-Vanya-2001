import time


def decoration(func):
    def wrapper():
        origin = func()
        modified = origin + ', декоратор'
        return modified

    return wrapper


def uppercase(func):
    def wrapper():
        origin = func()
        modified = origin.upper() + ', декоратор!'
        return modified

    return wrapper


@uppercase
def say_hello():
    return 'Hello'


def time_measure(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Затраченное время : {end - start}')

    return wrapper

@time_measure
def make_list():
    a = [i for i in range(5000000)]
    return a



make_list()


@decoration
def say_hello():
    return 'Hello'


"""
#greet =no_decoration(say_hello())
"""
#print(say_hello())

# LAST PYTHON CLASS - Thursday 22 - 09 - 2022
import functools
import time


def decorate(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        print("I am a before decorator")
        f = func(*args, **kwargs)
        print(func(*args, **kwargs))
        print("I am after decorator")
        return f

    return wrap


def performance_counter(google):
    @functools.wraps(google)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func = google(*args, **kwargs)
        end = time.perf_counter()
        print(f"the function {google.__name__} took {end - start} to run")
        return func

    return wrapper


@decorate
def hello(name):
    return f"Hello {name}"


@performance_counter
@decorate
def add(x, y):
    """
    adds two numbers
    """
    return x + y


hello = decorate(hello)

print(hello("Esther"))
print(add(10, 71))
print(performance_counter("Human Computer Interaction"))

# print(add.__name__)
# print(add.__doc__)

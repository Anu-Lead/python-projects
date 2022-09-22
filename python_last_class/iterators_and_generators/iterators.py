lst = [2, 4, 6, 8, 10]
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(list(it))


def custom_for(iterable):
    it = iter(iterable)

    while True:
        try:
            print(next(it))
        except StopIteration:
            print("End of Loop")
            return


print(custom_for(lst))


def infinite_number_generator():
    num = 10
    while True:
        yield num
        num += 10


gen = infinite_number_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

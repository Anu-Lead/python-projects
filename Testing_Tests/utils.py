"""def add(a, b):
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Only Int and Float is Required"
    assert a > 0 and b > 0, "Number Cannot be Negative"
    return a + b


# assert [1, 2, 4] == [2, 4, 6]
print(add("5", "7"))"""
from Testing_Tests.exceptions import MyCustomException

"""def sum_num(x, y) -> list:
    assert isinstance(x, list) and isinstance(y, list), "Provide List Type Data"
    return x + y


print(sum_num([12, 13, True, 14, "Goodness"], ["15, 16, 17"]))
# print(sum_num(12, ["15, 16, 17"]))"""

# def sum_num(y) -> list:
#     assert isinstance(y, list), "Provide List Type Data"
#     return y
#
#
# print(sum_num([12 + 13]))
# # print(sum_num(12, ["15, 16, 17"]))


# DOC TEST
import doctest


def adding_test(first, second):
    """
    >>> adding_test(4, 7)
    11
    >>> adding_test(4, 5)
    9
    >>> adding_test(4, "Hi") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last)
        ...
        TypeError:

    """
    if first > second:
        raise MyCustomException("Just Playing Around")

    return first + second


# print(adding_test(5, 5))
if __name__ == "__main__":
    doctest.testmod(verbose=True)



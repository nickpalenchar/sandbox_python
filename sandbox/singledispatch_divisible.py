"""
Given an int and a list of ints, determine if the first
is divisible by all others.

The second argument is an int to test or a list of ints, if
multiple must be tested

(An example for using singledispatch decorator)
"""
from functools import singledispatch
from typing import List

@singledispatch
def divisible_by(first: int, test: int):
    return first % test == 0

@divisible_by.register
def _(first: int, test: List[int]):
    for i in test:
        if first % i != 0:
            return False
    return True

if __name__ == '__main__':
    print(divisible_by(6, 3))
    print(divisible_by(6, [3, 2, 1]))

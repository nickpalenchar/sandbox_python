from functools import singledispatch
from typing import Union

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("let me just say: ", end=" ")
    print(arg)

@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("strength in numbers, eh? ", end=" ")
    print(arg)

@fun.register
def _(arg: Union[list, set], verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

if __name__ == '__main__':
    print("int overload")
    fun(3, True)

    print("list | set overload")
    fun([1,3,4], True)
    fun({8,10,23}, True)


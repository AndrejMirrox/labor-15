#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


class rec(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        while callable(result): result = result()
        return result

    def call(self, *args, **kwargs):
        return lambda: self.func(*args, **kwargs)


@rec
def factorial_opt(n, acc = 1):
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)


def factorial(n, acc = 1):
    if n == 0:
        return acc
    return factorial(n - 1, n * acc)


if __name__ == "__main__":
    print("Первый вариант:")
    print(f'{timeit.timeit(lambda: factorial_opt(250), number=10000)}')
    print("Второй вариант:")
    print(f'{timeit.timeit(lambda: factorial(15), number=10000)}')
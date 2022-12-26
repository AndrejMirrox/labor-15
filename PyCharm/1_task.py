#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache

def factorial_iteration(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


@lru_cache
def factorial_cache(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_cache(n - 1)

if __name__ == "__main__":
    print("Время обычной версии:")
    print(f'{timeit.timeit(lambda: factorial_iteration(200), number=10000)}, \n')
    print("Время рекурс. версии:")
    print(f'{timeit.timeit(lambda: factorial(200), number=10000)}, \n')
    print("Время рекурс. кеш. версии:")
    print(f'{timeit.timeit(lambda: factorial_cache(200), number=10000)}, \n')
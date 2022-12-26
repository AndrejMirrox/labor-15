#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

sys.setrecursionlimit(30000)


def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m - 1, 1)
    elif m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))


if __name__ == "__main__":

    in_m = int(input("Введите число m:"))
    in_n = int(input("Введите число n:"))
    print(f"A({in_m}, {in_m}) = {A(in_m, in_n)}")

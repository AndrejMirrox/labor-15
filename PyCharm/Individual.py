#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def sum(*a):
    if a:
        min_i = a.index(min(a))
        if min_i != len(a)-1:
            return math.fsum(a[min_i+1:])
        else:
            return "Дальше элементов нет"
    else:
        return "None"


if __name__ == "__main__":
    print(f"Сумма аргуметов после мин.: {sum(42, 15, 33, 10, 12, 12, 11)}")


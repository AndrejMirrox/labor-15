#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def average(*a):
    if a:
        nums = [1/num for num in a]
        out = len(nums)/math.fsum(nums)
        return out
    else:
        return "None"


if __name__ == "__main__":
    print(f"Вывод программы: {average(6, 4, 7)}")
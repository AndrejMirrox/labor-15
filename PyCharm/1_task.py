#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def geometric(*a):
    if a:
        nums = [num for num in a]
        out = math.pow(math.prod(nums), 1/len(nums))
        return out
    else:
        return "None"

if __name__ == "__main__":
    print(f"Вывод результата: {geometric(2, 5, 6, 8)}")
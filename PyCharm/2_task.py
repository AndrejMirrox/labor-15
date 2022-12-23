#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))
    s_side = 2 * math.pi * r * h

    def circle():
        s_circle = math.pi * r ** 2
        return s_circle

    check = input("Введите Y для бок. площ. или N для всей площ.: ")
    if check == "Y":
        print(f"Бок. площ. цилиндра: {s_side}")
    else:
        full_area = s_side + circle() * 2
        print(f"Полная площ. цилиндра: {full_area}")


if __name__ == "__main__":
    cylinder()
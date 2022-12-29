#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def del1(type="even"):
    def del2(b):
        if type == 'even':
            b = [num for idx, num  in enumerate(b) if num % 2 != 0]
            return b
        else:
            b = [num for idx, num in enumerate(b) if num % 2 == 0]
            return b
    return del2


if __name__ == "__main__":
    list = list(map(int, input("Введите список: ").split()))
    com = input("Введите параметр функции: ")
    print(f"Тест: {del1(com)(list)}")


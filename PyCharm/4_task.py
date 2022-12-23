#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    return input("Введите число: ")


def test_input(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def str_to_int(num):
    return int(num)


def print_int(num):
    print(num, type(num))


if __name__ == "__main__":
    number = get_input()
    print(number, type(number))
    if test_input(number):
        str_to_int(number)
        print_int(str_to_int(number))
    else:
        print(f"Нельзя преобразовать в число {number}")
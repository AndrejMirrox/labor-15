#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator_func(func):
    morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е':
        '.', 'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-',
             'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с':
                 '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.',
             'ш': ' - ---', 'щ': ' - -.-', 'ъ': ' - -.--', 'ы': ' -.--', 'ь': ' -..-', 'э': '..-..',
             'ю': '..--', 'я': '.-.-', ' ': '-···-'}
    def wrapper(text):
        text = func(text)
        text = ''.join([morze.get(ch, '') for ch in text])
        return text

    return wrapper


@decorator_func
def rus_lat(text):
    text = ' '.join(text.split())
    text = text.lower()
    return text


if __name__ == '__main__':
    txt = "Это тест   программы"
    print(rus_lat(txt))
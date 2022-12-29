#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator_func(func):

    def wrapper(text, chars=' !?'):
        text = ''.join(['-' if i in chars else i for i in text])
        while '--' in text:
            text = text.replace('--', '-')
        return func(text)

    return wrapper


@decorator_func
def rus_lat(text):
    morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е':
        '.', 'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-',
        'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с':
        '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.',
        'ш': ' - ---', 'щ': ' - -.-', 'ъ': ' - -.--', 'ы': ' -.--', 'ь': ' -..-', 'э': '..-..',
        'ю': '..--', 'я': '.-.-', ' ': '-···-'}

    text = ''.join([t[i] if i != '-' else '-' for i in text])
    return text


if __name__ == '__main__':
    txt = "Текст     ???? который .... нужно !!::заменить".lower()
    print(rus_lat(txt, chars='?!:;,. '))
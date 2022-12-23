#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date


def add_man():
    """
    Добавление людей
    """

    name = input("Фамилия и инициалы? ")
    post = input("Телефон? ")
    year = input("Год рождения? ")
    year = year.split(".")
    year = date(int(year[0]), int(year[1]), int(year[2]))

    # Создать словарь.
    man = {
        'name': name,
        'tel': post,
        'date': year,
    }

    # Добавить словарь в список.
    return man


def list_man(people):
    """
    Вывод людей
    """

    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 12
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^12} |'.format(
            "№",
            "Ф.И.О.",
            "Телефон",
            "Год рождения"
        )
    )
    print(line)

    for idx, man in enumerate(people, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>12} |'.format(
                idx,
                man.get('name', ''),
                man.get('tel', ''),
                str(man.get('date', 0))
            )
        )
    print(line)


def select_man(person):
    """
    Вывод конкретных людей
    """

    count = 0
    for man in people:
        if man.get('name', person).lower() == person.lower():
            count += 1
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 12
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^12} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Телефон",
                    "Год рождения"
                )
            )
            print(line)
            print(
                '| {:>4} | {:<30} | {:<20} | {:>12} |'.format(
                    count,
                    man.get('name', ''),
                    man.get('tel', ''),
                    str(man.get('date', 0))
                )
            )
            print(line)

    if count == 0:
        print("Люди с заданным именем не найдены.")


def help_man():
    print("Список команд:\n")
    print("add - добавить человека;")
    print("list - вывести список людей;")
    print("select <имя> - запросить людей с этим именем;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


if __name__ == '__main__':
    # Список работников.
    people = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == "add":
           people.append(add_man())
           if len(people) > 1:
               people.sort(key=lambda item: item.get('tel', ''))

        elif command == 'list':
           list_man(people)

        elif command.startswith('select'):
            parts = command.split(' ', maxsplit=1)
            period = parts[1]
            select_man(period)

        elif command == 'help':
           help_man()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
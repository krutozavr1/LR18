#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Используя замыкания функций, объявите внутреннюю функцию, которая принимает в
качестве параметров фамилию и имя, а затем, заносит в шаблон эти данные. Сам шаблон –
это строка, которая передается внешней функции и, например, может иметь такой вид:
«Уважаемый %F%, %N%! Вы делаете работу по замыканиям функций.» Здесь %F% - это
фрагмент куда нужно подставить фамилию, а %N% - фрагмент, куда нужно подставить имя.
(Шаблон может быть и другим, вы это определяете сами). Здесь важно, чтобы внутренняя
функция умела подставлять данные в шаблон, формировать новую строку и возвращать
результат. Вызовите внутреннюю функцию замыкания и отобразите на экране результат ее
работы.
"""


def print_message():
    """matches name and surname and prints message """
    name = ""
    surname = ""
    def match_data(n, s):
        nonlocal name
        nonlocal surname
        name = n
        surname = s
        sample = f"Уважаемый {name} {surname}! Вы делаете работу по замыканиям функций."
        print(sample)
    return match_data


if __name__ == "__main__":
    name = input()
    surname = input()
    
    printer = print_message()
    printer(name, surname)

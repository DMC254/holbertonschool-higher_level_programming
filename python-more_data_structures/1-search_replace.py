#!/usr/bin/python3
def searche_replace(my_list, searche, replace):
    return [replace if i == searche else i for i in my_list]

# -*- coding: utf-8 -*-
class GlobalVar:
    name = None


def set_name(name):
    GlobalVar.name = name


def get_name():
    return GlobalVar.name

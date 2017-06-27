#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


def ranchar():
    # 生成4位随机数函数，随机数可能是字母加数字或全部为数字
    checkcode = ''
    for i in range(4):
        current = random.randrange(0, 4)
        if current == i:
            tmp = chr(random.randint(65, 90))
        else:
            tmp = random.randint(0, 9)
        checkcode += str(tmp)
    return checkcode

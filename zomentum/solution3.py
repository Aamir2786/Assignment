# -*- coding: utf-8 -*-
"""
@author: aamir
"""
exp = "x = (21 - 1) / 10"
lhs, rhs = exp[0:4], exp[4:]

value = eval(rhs)
print(lhs+str(value))
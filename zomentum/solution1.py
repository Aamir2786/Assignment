# -*- coding: utf-8 -*-
"""
@author: aamir
"""
import json

def operator_name_to_symbol(arg):
    s={
       "equal": "=",
       "add": "+",
       "subtract": "-",
       "multiply": "*",
       "divide": "/"
       }
    return s.get(arg, None)

def convert_to_equation(equation_dict):
    global b
    global count
    s = ""
    for i in equation_dict:
        if i == "op":
            s += operator_name_to_symbol(equation_dict["op"])
            b += 1
        elif i == "lhs":
            l = equation_dict[i]
            if isinstance(l, dict):
                s= convert_to_equation(l) + " " + s
            else:
                l = f'{l}'
                if b <= 1:
                    s = l + " " + s
                    b = 1
                else:
                    s = "(" + l + " " + s
                    count = count+1
        else:
            r = equation_dict[i]
            if isinstance(r, dict):
                s = s + " " + convert_to_equation(r)
            else:
                r = f'{r}'
                if count == 0:
                    s = s + " " + r
                else:
                    s = s + " " + r + ")"
                    count = count-1
                    while count != 0:
                        s = s + ")"
                        count = count - 1
    return s

f = open("input.json", "r")
equation_dict = json.loads(f.read())
f.close()

b=-1
count = 0
           
print(convert_to_equation(equation_dict))
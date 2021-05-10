# -*- coding: utf-8 -*-
"""
@author: aamir
"""
def rev(arg):
    s = {
         "+": "-",
         "-": "+",
         "*": "/",
         "/": "*"
         }
    return s.get(arg, None)

equation = "1 + (x * 10) = 21"
equation = equation.split()
op = ["+", "-", "*", "/"]

equation_list=[]
for item in equation:
    if item in op:
        equation_list.append(item)
    else:
        if "(" in item:
            equation_list.append(item[0])
            equation_list.append(item[1:])
        elif ")" in item:
            pos = item.find(")")
            equation_list.append(item[0:pos])
            x = list(item[pos:])
            for i in x:
                equation_list.append(i)
        else:
            equation_list.append(item)             
lhs = equation_list[:-2]
rhs=equation_list[-1]

count = 0
a = 0
while(len(lhs)>1):
    if count != 0:
        rhs = "(" + rhs + ")"
    else:
        count = 1
        
    if lhs[0] == "(" and lhs[-1] != ")":
        lhs.pop(0)
        for i in range(len(lhs)-1, -1, -1):
            if lhs[i] == ")":
                rhs = rhs + " " + rev(lhs[i+1]) + " " + lhs[i+2]
                count = 1
                del lhs[i:i+3]
                break
    elif lhs[0] != "(":
        rhs = rhs + " " + rev(lhs[1]) + " " + lhs[0]
        del lhs [0:2]
    else:
        lhs.pop(0)
        rhs = rhs + " " + rev(lhs[1]) + " " + lhs[2]
        del lhs[1:]

transformed_equation = lhs[0] + " " + "=" + " " + rhs
print(transformed_equation)
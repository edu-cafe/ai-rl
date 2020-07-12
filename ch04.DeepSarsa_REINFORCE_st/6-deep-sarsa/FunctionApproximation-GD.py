# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:35:53 2020

@author: shkim
"""


x_old = 0
x_new = 6
eps = 0.01  # epsilon, step-size
precision = 0.00001

# f(x) = x**4 - 3x**3 + 2
# gd_f(x) = 4x**3 - 9x**2
def f_gd(x):
    return 4 * x**3 - 9 * x**2

while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old - eps*f_gd(x_old)
    # print('x_old:', x_old, 'x_new:', x_new, 'x_new-x_old:', abs(x_new-x_old))
    print('x_new-x_old:', abs(x_new-x_old))

print('Local Minimum occurs at ', x_new)
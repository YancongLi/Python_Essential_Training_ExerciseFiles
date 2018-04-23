#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
print('x is {}'.format(x))
print(type(x))

y = "\"you're good.\""
print('y is {}'.format(y) + ', and the type is: ')
print(type(y))
print(
'''----
abc
----'''.upper())

str = 'seven "{1:<9}" "{0:>9}"'.format(111,333)
print(str)

a = 8
b = 9
string = f'this is a and b: {a:<09} {b:>09}'
print(string)

from decimal import *

a1 = Decimal('0.10')
a2 = Decimal('0.30')
aa = a1 + a1 + a1 - a2
print('0.1 + 0.1 + 0.1 - 0.3 with decimal.Decimal Class is: {}'.format(aa))

z = 0.1 + 0.1 + 0.1 - 0.3
print('z is {}'.format(z))
print(type(z))

boolean = True
print('boolean is {}'.format(boolean))
print(type(boolean))

t1 = (1,'two',3.0,[4, 'four'],5)
print('x is {}'.format(t1))
print(type(t1))
print(type(t1[1]))
t2 = (1,'two',3.0,[4, 'four'],5)
print(id(t1))
print(id(t2))
print(id(t1[0]))
print(id(t2[0]))
if t1[0] is t2[0]:
    print('t1[0] is the same as t2[0]')

if isinstance(t1, tuple):
    print('{} is {}'.format(t1, tuple))

ttt = (1,2,3,4,5) #this is a tuple
lll = [1,2,3,4,5] #this is a list

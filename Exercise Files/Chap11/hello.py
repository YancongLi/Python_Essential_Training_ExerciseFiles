#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World   ß.'.casefold())
print('Hello, World.'.swapcase())
print(f'Hello World. {42 * 7}')

s1 = ' Helloooooo Worldddd'
s2 = s1.upper()

print(id(s1))
print(id(s2))

x = 42
y = 73
print('the number is {}, {}'.format(x, y))
print('the number is {1}, {0}, {1}'.format(x, y))
print('the number is {:b}'.format(x))

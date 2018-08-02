#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '47'
y = int(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

z = -666
z = abs(z)
print(f'z is {type(z)}')
print(f'z is {z}')

h = 7
h = divmod(h, 3)
print(f'h is {h}')

k = z + 6j
print(f'k is {k}')
print(f'k is {type(k)}')
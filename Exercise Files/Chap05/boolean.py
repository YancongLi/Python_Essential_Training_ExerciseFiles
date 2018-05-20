#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

print("1) -------------------------")
    
if a or b:
    print('expression is true')
else:
    print('expression is false')

print("2) -------------------------")

if a is b:
    print('expression is true')
else:
    print('expression is false')

print("3) -------------------------")

if y in x:
    print('expression is true')
else:
    print('expression is false')

print("4) -------------------------")

if y is x[0]:
    print(f"y is the same object as x[0]")
print(id(y))
print(id(x[0]))

print("5) -------------------------")
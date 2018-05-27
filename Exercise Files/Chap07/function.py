#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten(6, 6)
    kitten(1, 2, 3)
    x = 5
    print(f'The memory representaiton of x in main is: {id(x)}')
    call_by_value(x)
    print(f'in main : x is {x}')
    y = [2333]
    print(f'The memory representaiton of y in main is: {id(y)}')
    call_by_reference(y)
    print(f'in main : y is {y}')

def kitten(a, b, c = 0):
    print('Meow.')
    print(f'{a}, {b}, {c}')

def call_by_value(x):
    print(f'The memory representaiton of x in call_by_value is: {id(x)}')
    x = 666
    print(f'The memory representaiton of x in call_by_value is: {id(x)}')
    print(f'in function: x is {x}')

def call_by_reference(y):
    print(f'The memory representaiton of y in call_by_reference is: {id(y)}')
    y[0] = 666
    print(f'The memory representaiton of y in call_by_reference is: {id(y)}')
    print(f'in function: y is {y}')

if __name__ == '__main__': main()
#Reason: Python does not support forward declaration

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')

def return_type():
    return dict(x = 2333, y = 666)

returned_val = return_type()
print(type(returned_val), returned_val)

def f1(f):
    def f2():
        print('This is before function call')
        f()
        print('This is after function call')
    return f2

@f1
def f3():
    print('this is f3')

f3()

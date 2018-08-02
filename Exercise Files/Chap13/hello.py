#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'abcd'
print(repr(s))# representation of the variable

class bunny:
    def __init__(self, n):
        self._n = n
        
    def __repr__(self): #overriding the default function
        return f'the number of bunnies is {self._n}'
    
        
bunny = bunny(47)
print(repr(bunny))
print(ascii(bunny))

x = (1, 2, 3, 4, 5)
y = list(reversed(x))

print(x)
print(y)
for i in y: print(i)
print(sum(x, 10))
print(max(x))
print(min(x))
print(any(x))#if contains any ''true elements (positive)
print(all(x))
for a, b in zip(x, y):
    print(f' {a} --- {b}')

print('Hello, World.')

animal = ('cat', 'dog', 'rabbit')
for i, v in enumerate(animal):
    print(f'{i}: {v}')
    
    
q = 42
w = type(q)
e = isinstance(q, int)
print(q)
print(w)
print(e)

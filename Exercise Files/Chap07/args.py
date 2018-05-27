#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr', 'hello', 'world')
    print('-----')
    kitten()
    print('-----')
    y = ('a', 'b', 'c') #define a tuple(collection)
    kitten(*y) # here: * is for list

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow ???')

if __name__ == '__main__': main()

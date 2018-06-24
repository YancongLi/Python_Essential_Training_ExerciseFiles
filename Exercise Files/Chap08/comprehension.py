#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from math import pi

def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]
    seq3 = [x for x in seq if x % 3 == 0]
    seq4 = [round(pi, i) for i in seq]
    seq5 = { x: x**2 for x in seq }
    
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print(seq5)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

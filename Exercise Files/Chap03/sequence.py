#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = [ 1, 2, 3, 4, 5 ]
# x[4] = 666

x = list(range(5, 50, 5))
x[2] = 666
for i in x:
    print('i is {}'.format(i))
    
y = {'one':1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
y['three'] = 666
for k, v in y.items():
    print( 'key:{}, value:{}'.format(k, v) )

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
import datetime

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(2).hex())
    
    print(random.randint(1,10))
    x = list(range(20))
    print(x)
    random.shuffle(x)
    print(x)
    
    now = datetime.datetime.now()
    print(now)
    print(now.year)
    print(now.month)
    print(now.day)
    

if __name__ == '__main__': main()

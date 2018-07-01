#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

def main():
    try:
        # x = int('abc')
        y = 5/0
    except ValueError:
        print('I caught a ValueError')
    # except ZeroDivisionError:
    #     print('Don\'t divide by zero')
    except:
        print(f'Unknown error: {sys.exc_info()}')
    else:
        print(y)
        
        
    print('Good job')

if __name__ == '__main__': main()

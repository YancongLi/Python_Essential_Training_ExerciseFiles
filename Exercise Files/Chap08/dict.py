#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    animals['monkey'] = 'hahaha'
    print('Found!' if 'lion' in animals else 'nope!')
    print(666)
    print_dict(animals)
    
    print('---------------')
    
    dictionaryConstruct = dict(key1 = 'value1', key2 = 'value2', key3 = 'value3')
    print_dict(dictionaryConstruct)
    
    print('---------------')
    for k, v in animals.items():
        print(f'{k} => {v}')

    print('---------------')
    for k in animals.keys(): print(k)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()

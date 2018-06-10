#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ] #This is a list
    print(game[0:3])
    i = game.index('Paper')
    game.insert(0, 'Computer')
    game.remove('Rock')
    print_list(game)
    print(', '.join(game))
    print(len(game))
    print(game.pop())
    print(game)
    del game[1:3]
    print(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()

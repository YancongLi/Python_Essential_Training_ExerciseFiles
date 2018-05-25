#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'peter666'
pw = ''
auth = False
count = 0
max_attempt = 3


while pw != secret:
    count += 1
    pw = input(f"{count}: What's the secret word? ")
    if pw == secret:
        auth = True
    if (count + 1) > max_attempt:
        print("You tried too many times. Exiting...")
        break
    
print("Authorized. Welcome!" if auth else "You do not have access.")

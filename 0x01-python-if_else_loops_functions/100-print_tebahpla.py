#!/usr/bin/python3
for char in range(ord('z') and ord('a') - 1, -1):
    print(chr(char), end='')
    char -= 1
    if char >= ord('A'):
        print(chr(char - ord('a') + ord('A')), end='')

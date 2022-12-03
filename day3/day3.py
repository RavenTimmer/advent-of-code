#!/usr/bin/python3
import os

my_absolute_path = r'/home/raven/Documents/code/Advent_of_code_2022/day3/input.txt'
file1 = open(my_absolute_path, 'r')
lines = file1.readlines()

value = 0
current_line = 0

for start in range(0, len(lines), 3):
    a = list(set(lines[start].strip())&set(lines[start+1].strip())&set(lines[start+2].strip()))
    for i in a:
        if i.isupper():
            value += (ord(i) - 38)
        else:
            value += (ord(i) - 96)

print(value)
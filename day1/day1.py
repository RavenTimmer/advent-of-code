#!/usr/bin/python3
import os

my_absolute_path = r'/home/raven/Documents/UVA/Advent_of_code/day1/input.txt'

cal1 = 0; cal2 = 0; cal3 = 0; current_cal = 0

file1 = open(my_absolute_path, 'r')

while True:
    line = file1.readline()

    if not line:
        break

    if line == '\n':
        if current_cal > cal1:
            cal3 = cal2
            cal2 = cal1
            cal1 = current_cal
        elif current_cal > cal2:
            cal3 = cal2
            cal2 = current_cal
        elif current_cal > cal3:
            cal3 = current_cal

        current_cal = 0
        continue

    current_cal += int(line.strip())

total = cal1 + cal2 + cal3

print(total)
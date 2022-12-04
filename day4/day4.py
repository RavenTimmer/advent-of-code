#!/usr/bin/python3
import os

my_absolute_path = r'/home/raven/Documents/code/Advent_of_code_2022/day4/input.txt'
file1 = open(my_absolute_path, 'r')
lines = file1.readlines()

total = 0

def compare_ranges(x,y):
    return True if set(x) & set(y) else False

for line in lines:
    split = line.strip().split(",")
    range1 = split[0].split("-")
    range2 = split[1].split("-")

    if compare_ranges(range(int(range1[0]), int(range1[1]) + 1, 1), range(int(range2[0]), int(range2[1]) + 1, 1)):
        total += 1

print(total)

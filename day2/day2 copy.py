#!/usr/bin/python3
import os

my_absolute_path = r'/home/raven/Documents/UVA/Advent_of_code/day2/input.txt'
lines = open(my_absolute_path, 'r').readlines()

total_points = 0
played_hand = [2, 3, 1, 2, 3, 1, 2]

for line in lines:
    x = line.split()

    total_points += (ord(x[1]) - 88) * 3
    total_points += played_hand[(4 + (ord(x[0]) - 65)) - ((ord(x[1]) - 88) * 2)]

print(total_points)

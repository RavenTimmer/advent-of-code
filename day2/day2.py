#!/usr/bin/python3
lines = open(r'/home/raven/Documents/code/Advent_of_code_2022/day2/input.txt', 'r').readlines()
total_points = 0; played_hand = [2, 3, 1, 2, 3, 1, 2]

for line in lines:
    x = line.split()
    total_points += ((ord(x[1]) - 88) * 3) + played_hand[(4 + (ord(x[0]) - 65)) - ((ord(x[1]) - 88) * 2)]
print(total_points)
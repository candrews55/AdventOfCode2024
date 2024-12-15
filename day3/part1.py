# load data
import re

f = open("day3.txt", "r")

total = 0
for line in f:
    prog = re.compile(r"mul\([0-9]*,[0-9]*\)")
    mul = prog.findall(line)
    for value in mul:
        mathValues = value.replace('mul(', '').replace(')', '').strip().split(',')
        total += int(mathValues[0]) * int(mathValues[1])

print(total)


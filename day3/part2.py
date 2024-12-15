import re

# load data
f = open("day3.txt", "r")

shouldCompute = True
total = 0
for line in f:
    prog = re.compile(r"mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)")
    mul = prog.findall(line)
    for value in mul:
        match value:
            case 'do()':
                shouldCompute = True
            case 'don\'t()':
                shouldCompute = False
            case _:
                if shouldCompute:
                    mathValues = value.replace('mul(', '').replace(')', '').strip().split(',')
                    total += int(mathValues[0]) * int(mathValues[1])

print(total)


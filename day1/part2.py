# load data from file
f = open('day1.txt', 'r')

# set up the list
left = []
right = []

for line in f:
    parseLine = line.split('   ')
    left.append(int(parseLine[0]))
    right.append(int(parseLine[1]))

total = 0
for line in left:
    amount = right.count(line)
    total += line * amount

print(total)
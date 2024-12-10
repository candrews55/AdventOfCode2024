
# load data from file
f = open('day1.txt', 'r')

# set up the list
firstGroup = []
secondGroup = []

for line in f:
    parseLine = line.split('   ')
    firstGroup.append(int(parseLine[0]))
    secondGroup.append(int(parseLine[1]))

firstGroup.sort()
secondGroup.sort()

total = 0

for first, second in zip(firstGroup, secondGroup):
    if first > second:
        total += first - second
    else:
        total += second - first

print(total)

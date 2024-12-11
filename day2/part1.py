# loading data
f = open("day2.txt", "r")

total = 0
for line in f:
    isGreater = None
    first = None
    for second in map(lambda x: int(x), line.split()):
        if first is None:
            first = int(second)
            continue

        if (first > second and isGreater == False) or (first < second and isGreater == True) or first == second:
            break

        distance = abs(first - second)
        if distance > 3 or distance < 1:
            break

        isGreater = first > second
        first = second
    else:
        total += 1

print(total)

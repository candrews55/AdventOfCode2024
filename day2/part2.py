def is_safe_when_greater(first_number: int, second_number: int) -> bool:
    distance = first_number - second_number
    return distance == 1 or distance == 2 or distance == 3


def is_safe_when_lesser(first_number: int, second_number: int) -> bool:
    distance = first_number - second_number
    return distance == -1 or distance == -2 or distance == -3


def find_safe_level_greater(report_to_check: list[int]) -> int:
    for i in range(len(report_to_check) - 1):
        if not is_safe_when_greater(report_to_check[i], report_to_check[i + 1]):
            return i
    return -1


def find_safe_level_lesser(report_to_check: list[int]) -> int:
    for i in range(len(report_to_check) - 1):
        if not is_safe_when_lesser(report_to_check[i], report_to_check[i + 1]):
            return i
    return -1


def find_unsafe_level(report_to_check: list[int]) -> int:
    distance = report_to_check[0] - report_to_check[1]
    if distance == 0: return 0
    if distance > 0: return find_safe_level_greater(report_to_check)
    return find_safe_level_lesser(report_to_check)


# loading data
f = open("day2.txt", "r")

total = 0
for line in f:
    report = list(map(lambda x: int(x), line.split()))
    firstUnsafeLevel = find_unsafe_level(report)
    if firstUnsafeLevel == -1:
        total += 1
        continue

    for i in range(len(report)):
        # Generate new report with one of the elements removed
        if i == 0:
            newReport = report[1:]
        elif i == len(report) - 1:
            newReport = report[:-1]
        else:
            newReport = report[:i] + report[i + 1:]

        if find_unsafe_level(newReport) == -1:
            total += 1
            break

print(total)

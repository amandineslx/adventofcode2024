from functools import cmp_to_key

INPUT_FILE = "05-input.txt"
PRECEDENCES = dict()
MANUALS = []

def initialize():
    with open(INPUT_FILE, 'r') as f:
        is_precedence = True
        for line in f.readlines():
            if not line[:-1]:
                is_precedence = False
                continue
            if is_precedence:
                parts = line[:-1].split("|")
                if parts[0] not in PRECEDENCES.keys():
                    PRECEDENCES[parts[0]] = []
                PRECEDENCES[parts[0]].append(parts[1])
            else:
                parts = line[:-1].split(",")
                MANUALS.append(parts)

def compare(x, y):
    if x in PRECEDENCES.keys() and y in PRECEDENCES[x]:
        return -1
    else:
        return 1

def is_manual_valid(manual):
    for i in range(1, len(manual)):
        if manual[i] in PRECEDENCES.keys():
            intersection = list(set(manual[:i]) & set(PRECEDENCES[manual[i]]))
            if intersection:
                return False
    return True

def get_central_element_int(manual):
    return int(manual[int((len(manual) - 1) / 2)])

def compute_sum():
    sum = 0
    for manual in MANUALS:
        if is_manual_valid(manual):
            sum += get_central_element_int(manual)
    return sum

def compute_sum_sorted_manuals():
    sum = 0
    for manual in MANUALS:
        if not is_manual_valid(manual):
            sorted_manual = sorted(manual, key=cmp_to_key(compare))
            sum += get_central_element_int(sorted_manual)
    return sum

initialize()
#print(compute_sum())
print(compute_sum_sorted_manuals())

import json

INPUT_FILE = "01-input.txt"

def compute_sum(list_left, list_right):
    sum = 0
    for i in range(len(list_left)):
        sum += abs(list_left[i] - list_right[i])
    return sum

def compress_list(l):
    d = dict()
    for x in l:
        if x in d.keys():
            d[x] += 1
        else:
            d[x] = 1
    return d

def compute_similarities(list_left, compressed_list_right):
    similarity = 0
    for x in list_left:
        if x in compressed_list_right.keys():
            similarity += x*compressed_list_right[x]
        else:
            continue
    return similarity

def build_lists():
    list_left = []
    list_right = []

    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            parts = line[:-1].split("   ")
            list_left.append(int(parts[0]))
            list_right.append(int(parts[1]))

    return list_left,list_right

def part1():
    list_left,list_right = build_lists()
    list_left.sort()
    list_right.sort()
    print(compute_sum(list_left, list_right))

def part2():
    list_left,list_right = build_lists()
    compressed_list_right = compress_list(list_right)
    print(compute_similarities(list_left, compressed_list_right))

#part1()
part2()

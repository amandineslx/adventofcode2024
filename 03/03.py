import re

INPUT_FILE = "03-input.txt"
REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"

def compute_sum():
    line = ""
    sum = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            for match in re.finditer(REGEX, line):
                print(match.group(0))
                m = int(match.group(1))
                n = int(match.group(2))
                sum += n*m
    print(sum)

compute_sum()

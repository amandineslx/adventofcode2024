import re

INPUT_FILE = "03-input.txt"
REGEX_MUL = r"mul\((\d{1,3}),(\d{1,3})\)"
REGEX_IGNORE = r"don't\(\).*?(do\(\)|$)"

def remove_ignored_instructions(instructions):
    return re.sub(REGEX_IGNORE, "", instructions)

def compute_sum(instructions):
    sum = 0
    for match in re.finditer(REGEX_MUL, instructions):
        #print(match.group(0))
        m = int(match.group(1))
        n = int(match.group(2))
        sum += n*m
    return sum

def main():
    instructions = ""
    sum = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            sum += compute_sum(remove_ignored_instructions(line))
    print(sum)

main()

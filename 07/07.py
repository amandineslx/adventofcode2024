INPUT_FILE = "07-input.txt"
BASE = 3

def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def to_base(n):
    if BASE == 2:
        return str(bin(n))[2:]
    elif BASE == 3:
        return str(ternary(n))

def number_to_sequence(b, length):
    binary = str(to_base(b))
    l = ["0"] * (length - len(binary))
    l += binary
    return l

def number_to_operator(number):
    if number == "0":
        return "+"
    elif number == "1":
        return "*"
    elif number == "2":
        return "||"

def number_to_operators(b, length):
    l = number_to_sequence(b, length)
    return [number_to_operator(n) for n in l]

def compute_compare_result(numbers, operators, result):
    res = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == "||":
            res = int(str(res) + numbers[i])
        else:
            res = eval(str(res) + operators[i-1] + numbers[i])
    print(f"{res} // {result}")
    return result == res

def is_solvable(tuple):
    operators_number = len(tuple[1]) - 1
    if len(tuple[1]) == 1 and tuple[0] == tuple[1][0]:
        return True
    for i in range(pow(BASE, operators_number)):
        operators = number_to_operators(i, operators_number)
        if compute_compare_result(tuple[1], operators, tuple[0]):
            return True
    return False

def check_possible_operations(input):
    sum = 0
    for tuple in input:
        if is_solvable(tuple):
            sum += tuple[0]
            print(f"Sum: {sum}")
    return sum

def read_input():
    l = []
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            parts = line[:-1].split(": ")
            result = int(parts[0])
            numbers = parts[1].split(" ")
            l.append((result, numbers))
    return l

def main():
    input = read_input()
    print(input)
    print(check_possible_operations(input))

main()

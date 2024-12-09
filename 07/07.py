INPUT_FILE = "07-input.txt"

def binary_to_sequence(b, length):
    binary = str(bin(b))[2:]
    l = ["0"] * (length - len(binary))
    l += binary
    return l

def number_to_operator(number):
    if number == "0":
        return "+"
    elif number == "1":
        return "*"

def binary_to_operators(b, length):
    l = binary_to_sequence(b, length)
    return [number_to_operator(n) for n in l]

def compute_compare_result(numbers, operators, result):
    res = numbers[0]
    for i in range(1, len(numbers)):
        res = eval(str(res)+operators[i-1]+numbers[i])
    print(f"{res} // {result}")
    return result == res

def is_solvable(tuple):
    operators_number = len(tuple[1]) - 1
    for i in range(pow(2, operators_number)):
        operators = binary_to_operators(i, operators_number)
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

INPUT_FILE = "05-input.txt"

class Printer():
    def __init__(self):
        self.precedences = dict()
        self.manuals = []
        with open(INPUT_FILE, 'r') as f:
            is_precedence = True
            for line in f.readlines():
                if not line[:-1]:
                    is_precedence = False
                    continue
                if is_precedence:
                    parts = line[:-1].split("|")
                    if parts[0] not in self.precedences.keys():
                        self.precedences[parts[0]] = []
                    self.precedences[parts[0]].append(parts[1])
                else:
                    parts = line[:-1].split(",")
                    self.manuals.append(parts)

    def is_manual_valid(self, manual):
        print(manual)
        for i in range(1, len(manual)):
            if manual[i] in self.precedences.keys():
                intersection = list(set(manual[:i]) & set(self.precedences[manual[i]]))
                if intersection:
                    return False
        return True

    def compute_sum(self):
        sum = 0
        for manual in self.manuals:
            if self.is_manual_valid(manual):
                sum += int(manual[int((len(manual) - 1) / 2)])
        return sum

printer = Printer()
print(printer.compute_sum())

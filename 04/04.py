INPUT_FILE = "04-input.txt"

class Input:
    def __init__(self, input_file):
        self.input = []
        with open(INPUT_FILE, 'r') as f:
            for line in f.readlines():
                self.input.append(line[:-1])
        self.height = len(self.input)
        self.width = len(self.input[0])

    def get(self, x, y):
        return self.input[y][x]

    def count_global_xmas_occurrences(self):
        occurrences = []
        for y in range(self.width):
            for x in range(self.height):
                if self.is_char(x, y, 'X'):
                    occurrences += self.count_local_xmas_occurrences(x, y)
        return occurrences

    def is_char(self, x, y, expected_char):
        c = self.get(x, y)
        if c == expected_char:
            return True
        return False

    def count_local_xmas_occurrences(self, x, y):
        occurrences = []
        # check horizontal right
        if x < self.width-3:
            if self.is_char(x+1, y, 'M') and self.is_char(x+2, y, 'A') and self.is_char(x+3, y, 'S'):
                #print(f"horizontal right in ({x},{y})")
                occurrences.append((x,y))
        # check horizontal left
        if x >= 3:
            if self.is_char(x-1, y, 'M') and self.is_char(x-2, y, 'A') and self.is_char(x-3, y, 'S'):
                #print(f"horizontal left in ({x},{y})")
                occurrences.append((x,y))
        # check vertical downwards
        if y < self.height-3:
            if self.is_char(x, y+1, 'M') and self.is_char(x, y+2, 'A') and self.is_char(x, y+3, 'S'):
                #print(f"vertical down in ({x},{y})")
                occurrences.append((x,y))
        # check vertically upwards
        if y >= 3:
            if self.is_char(x, y-1, 'M') and self.is_char(x, y-2, 'A') and self.is_char(x, y-3, 'S'):
                #print(f"vertical up in ({x},{y})")
                occurrences.append((x,y))
        # check diagonal NE
        if x < self.width-3 and y >= 3:
            if self.is_char(x+1, y-1, 'M') and self.is_char(x+2, y-2, 'A') and self.is_char(x+3, y-3, 'S'):
                #print(f"diagonal NE in ({x},{y})")
                occurrences.append((x,y))
        # check diagonal SE
        if x < self.width-3 and y < self.height-3:
            if self.is_char(x+1, y+1, 'M') and self.is_char(x+2, y+2, 'A') and self.is_char(x+3, y+3, 'S'):
                #print(f"diagonal SE in ({x},{y})")
                occurrences.append((x,y))
        # check diagonal SW
        if x >= 3 and y < self.height-3:
            if self.is_char(x-1, y+1, 'M') and self.is_char(x-2, y+2, 'A') and self.is_char(x-3, y+3, 'S'):
                #print(f"diagonal SW in ({x},{y})")
                occurrences.append((x,y))
        # check diagonal NW
        if x >= 3 and y >= 3:
            if self.is_char(x-1, y-1, 'M') and self.is_char(x-2, y-2, 'A') and self.is_char(x-3, y-3, 'S'):
                #print(f"diagonal NW in ({x},{y})")
                occurrences.append((x,y))
        return occurrences

def main():
    input = Input(INPUT_FILE)
    occurrences = input.count_global_xmas_occurrences()
    print(occurrences)
    print(len(occurrences))

main()

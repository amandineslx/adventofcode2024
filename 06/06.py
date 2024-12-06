INPUT_FILE = "06-input.txt"

class OutOfBoundException(Exception):
    pass

class Square:
    def __init__(self, occupied, visited):
        self.occupied = occupied
        self.visited = visited

class Warehouse:
    def __init__(self):
        self.map = []
        y = 0
        with open(INPUT_FILE, 'r') as f:
            for line in f.readlines():
                line = line[:-1]
                decoded_line = []
                for x in range(len(line)):
                    char = line[x]
                    if char == '#':
                        decoded_line.append(Square(occupied=True, visited=False))
                    elif char == '^':
                        decoded_line.append(Square(occupied=False, visited=True))
                        self.current_position = (x,y)
                        self.current_direction = "UP"
                    else:
                        decoded_line.append(Square(occupied=False, visited=False))
                self.map.append(decoded_line)
                y += 1
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.counter = 1

    def get_square(self, x, y):
        return self.map[y][x]

    def change_directions(self):
        if self.current_direction == "UP":
            self.current_direction = "RIGHT"
        elif self.current_direction == "RIGHT":
            self.current_direction = "DOWN"
        elif self.current_direction == "DOWN":
            self.current_direction = "LEFT"
        elif self.current_direction == "LEFT":
            self.current_direction = "UP"

    def compute_next_position(self):
        if self.current_direction == "UP":
            next_x = self.current_position[0]
            next_y = self.current_position[1] - 1
        elif self.current_direction == "RIGHT":
            next_x = self.current_position[0] + 1
            next_y = self.current_position[1]
        elif self.current_direction == "DOWN":
            next_x = self.current_position[0]
            next_y = self.current_position[1] + 1
        else:
            next_x = self.current_position[0] - 1
            next_y = self.current_position[1]
        if not next_x in range(0, self.width) or not next_y in range(0, self.height):
            raise OutOfBoundException()
        return (next_x, next_y)

    def is_position_occupied(self, x, y):
        return self.get_square(x, y).occupied

    def update_position(self, x, y):
        self.current_position = (x, y)
        current_square = self.get_square(self.current_position[0], self.current_position[1])
        if not current_square.visited:
            self.counter += 1
            current_square.visited = True

    def count_visited_squares(self):
        try:
            while 1 == 1:
                next_position = self.compute_next_position()
                if self.is_position_occupied(next_position[0], next_position[1]):
                    self.change_directions()
                else:
                    self.update_position(next_position[0], next_position[1])
        except OutOfBoundException:
            #self.print()
            print(self.counter)

    def print(self):
        for line in self.map:
            l = ""
            for square in line:
                if square.occupied:
                    l += "#"
                elif square.visited:
                    l += "X"
                else:
                    l += "."
            print(l)

warehouse = Warehouse()
warehouse.count_visited_squares()

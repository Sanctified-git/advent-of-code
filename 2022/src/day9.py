from utils.io import get_input

class Rope:
    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]
        self.visited = {tuple([0, 0])}

    def move_head(self, direction):
        if direction == 'U':
            self.set_head([self.head[0], self.head[1] + 1])
        elif direction == 'D':
            self.set_head([self.head[0], self.head[1] - 1])
        if direction == 'L':
            self.set_head([self.head[0] - 1, self.head[1]])
        if direction == 'R':
            self.set_head([self.head[0] + 1, self.head[1]])

    def set_head(self, position):
        self.head = position
        move = [a - b for a, b in zip(self.head, self.tail)]
        
        if abs(move[0]) <= 1 and abs(move[1]) <= 1:
            return
        elif abs(move[0]) == 2 and abs(move[1]) == 2:
            self.tail[0] += move[0] / 2
            self.tail[1] += move[1] / 2
        elif abs(move[0]) == 2:
            self.tail[0] += move[0] / 2
            self.tail[1] = self.head[1]
        elif abs(move[1]) == 2:
            self.tail[1] += move[1] / 2
            self.tail[0] = self.head[0]

        self.visited.add(tuple(self.tail))

def day9():
    '''https://adventofcode.com/2022/day/9'''

    ### PART ONE ###
    rope = Rope()
    input: list = get_input(__file__)
    for line in input:
        direction, steps = line.split(' ')
        for _ in range(int(steps)):
            rope.move_head(direction)

    print(f"The tail of the rope has visited {len(rope.visited)} positions")

    ### PART TWO ###
    rope = [Rope() for _ in range(9)] # Rope is now ten knots long
    input: list = get_input(__file__)
    for line in input:
        direction, steps = line.split(' ')
        for _ in range(int(steps)):
            rope[0].move_head(direction)
            for i in range(8):
                rope[i+1].set_head(rope[i].tail)

    print(f"The tail of the new rope has visited {len(rope[8].visited)} positions")

if __name__ == "__main__":
    day9()

from utils.io import get_input

ROW_LENGTH = 40


class CPU:
    cycle: int
    x: int
    milestones: dict[int, int]
    crt_row: str

    def __init__(self) -> None:
        self.cycle = 1
        self.x = 1
        self.milestones = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}
        self.crt_row = "#"
        # The sprite always starts in the leftmost position just like the CRT,
        # so it will always be visible therefore we start with "#"

    def next_cycle(self) -> None:
        """Advance one cycle and calculate signal strength if a milestone is reached"""
        self.draw_pixel()
        self.cycle += 1
        if self.cycle in self.milestones.keys():
            self.milestones[self.cycle] = self.cycle * self.x

    def process_step(self, value: int) -> None:
        """Process an instruction, incrementing the register if needed"""
        self.next_cycle()

        if value is not None:
            self.x += value
            self.next_cycle()

    def draw_pixel(self) -> None:
        """Draw a pixel in the current CRT row, printing the row if fully drawn"""
        if len(self.crt_row) in [self.x - 1, self.x, self.x + 1]:
            self.crt_row += "#"
        else:
            self.crt_row += "."

        if len(self.crt_row) == ROW_LENGTH:
            print(self.crt_row)
            self.crt_row = ""


def day10():
    """https://adventofcode.com/2022/day/10"""
    input: list = get_input(__file__)
    cpu = CPU()

    for l in input:
        step = l.split(" ")
        value = int(step[1]) if len(step) > 1 else None
        cpu.process_step(value)

    print(f"The sum of the milestones' signal strength is {sum(cpu.milestones.values())}")


if __name__ == "__main__":
    day10()

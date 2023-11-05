"""https://adventofcode.com/2022/day/17"""
from utils.io import get_input
from utils.timer import Timer
from itertools import cycle
from copy import deepcopy

CWIDTH = 7
ROCKS = [
    set([0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j]),
    set([1 + 0j, 0 + 1j, 1 + 1j, 2 + 1j, 1 + 2j]),
    set([0 + 0j, 1 + 0j, 2 + 0j, 2 + 1j, 2 + 2j]),
    set([0 + 0j, 0 + 1j, 0 + 2j, 0 + 3j]),
    set([0 + 0j, 1 + 0j, 0 + 1j, 1 + 1j]),
]


class Iterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.current = None

    def __next__(self):
        try:
            self.current = next(self.iterator)
        except StopIteration:
            self.current = None
        finally:
            return self.current


def play_rounds(placed: set, move: Iterator, rounds: int):
    cmax: int = 0
    cur_height: int = 0
    for r in range(rounds):
        rested: bool = False
        cur_height += 3
        rock = new_rock(r % 5, cur_height)

        while not rested:
            rock = push_rock(rock, placed, next(move))

            if cur_height == 1:
                if cmax == 0:
                    rock = push_rock(rock, placed, next(move))
                    rested = True
                    break
                else:
                    rcopy = set([complex(r.real, r.imag + 1) for r in deepcopy(rock)])
                    if not rcopy & placed:
                        rock = push_rock(rock, placed, next(move))
                        rested = True
                        break

            for r in rock:
                r = complex(r.real, r.imag - 1)
            cur_height -= 1

        for r in rock:
            if (i := r.imag + 1) > cmax:
                cmax = i 
            placed.add(r)

    print(placed, cmax)
    return cmax


def new_rock(index: int, height: int) -> set:
    rock = deepcopy(ROCKS[index])
    for r in rock:
        r = complex(r.real + 2, r.imag + height)
    return rock


def push_rock(rock, placed, dir) -> list:
    print(dir)
    if dir > 0 and 7 <= dir + max(r.real for r in rock):
        return rock
    if dir < 0 and 0 > dir + min(r.real for r in rock):
        return rock
    
    rcopy = deepcopy(rock)
    for r in rcopy:
        r = complex(r.real + dir, r.imag)
    if not rcopy & placed:
        return rcopy
    return rock



if __name__ == "__main__":
    t = Timer()
    t.start()
    print("Parsing input")
    move = Iterator(
        cycle([1 if c == ">" else -1 for line in get_input(__file__) for c in line])
    )
    placed: set = set()
    t.step()

    ### PART ONE ###
    offset = 0
    cur_rock = 0
    height = play_rounds(placed, move, 1)
    t.stop()

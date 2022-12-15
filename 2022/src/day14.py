"""https://adventofcode.com/2022/day/14"""
from utils.io import get_input
from copy import deepcopy
from itertools import pairwise, count
from re import findall


def sign(x, y):
    return (x < y) - (x > y)


def fill_line(start: tuple, end: tuple):
    (x, y), (x2, y2) = start, end
    dx, dy = sign(x, x2), sign(y, y2)
    while (x, y) != end:
        x, y = x + dx, y + dy
        yield x, y


def place_rocks(input):
    rocks = set()
    for line in input:
        coords: list = findall(r"(\d+),(\d+)", line)
        path: list[tuple[int, int]] = [(int(x), int(y)) for x, y in coords]
        for start, end in pairwise(path):
            rocks.update([start, end])
            rocks.update(list(fill_line(start, end)))
    floor: int = max(r[1] for r in rocks) + 2
    return rocks, floor


def pour_sand(blocked, floor, part_two: bool = False):
    for c in count():
        x, y = 500, 0
        if part_two and (x, y) in blocked:
            return c
        while True:
            if y + 1 == floor:
                if not part_two:
                    return c
                blocked.add((x, y))
                break
            if (step := (x, y + 1)) not in blocked:
                x, y = step
            elif (step := (x - 1, y + 1)) not in blocked:
                x, y = step
            elif (step := (x + 1, y + 1)) not in blocked:
                x, y = step
            else:
                blocked.add((x, y))
                break


if __name__ == "__main__":
    rocks, floor = place_rocks(get_input(__file__))
    ### PART ONE ###
    print(f"{pour_sand(deepcopy(rocks), floor)} units of sand can come to rest on the rock formations")
    ### PART TWO ###
    print(f"{pour_sand(rocks, floor, part_two=True)} units of sand can come to rest before the source is blocked")
"""https://adventofcode.com/2022/day/12"""
import numpy as np
from queue import Queue
from utils.io import get_input

E_COST = 69
S_COST = 83
MIN_COST = 96 # 96 is ord(a) - 1
MAX_COST = 123 # 123 is ord(z) + 1


def letter(item: tuple) -> str:
    return grid[item[0]][item[1]]


def allowed(current: int, neighbor: tuple):
    nb_ord = ord(letter(neighbor))
    delta = MAX_COST - current if nb_ord == E_COST else nb_ord - current
    return True if delta <= 1 else False


def neighbors(item: tuple) -> list[tuple]:
    neighbors: list = []
    current_cost = ord(letter(item))
    h_min, h_max, w_min, w_max = (0, len(grid) - 1, 0, len(grid[0]) - 1)

    if current_cost == S_COST:
        current_cost = MIN_COST
    if item[0] > h_min:
        nb = (item[0] - 1, item[1])
        if allowed(current_cost, nb):
            neighbors.append(nb)
    if item[0] < h_max:
        nb = (item[0] + 1, item[1])
        if allowed(current_cost, nb):
            neighbors.append(nb)
    if item[1] > w_min:
        nb = (item[0], item[1] - 1)
        if allowed(current_cost, nb):
            neighbors.append(nb)
    if item[1] < w_max:
        nb = (item[0], item[1] + 1)
        if allowed(current_cost, nb):
            neighbors.append(nb)
    return neighbors


def breadth_first_search(start: tuple, goal: tuple) -> int:
    steps = 0
    frontier = Queue()
    frontier.put(start, 0)
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()

        if current == goal and letter(came_from[current]) == "z":
            while came_from[current]:
                steps += 1
                current = came_from[current]
            break

        for next in neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return steps


if __name__ == "__main__":
    grid: list = get_input(__file__)
    npgrid: np.ndarray = np.ndarray((len(grid), len(grid[0])), dtype="U1")

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            npgrid[i, j] = grid[i][j]

    goal: tuple = tuple(x[0] for x in np.where(npgrid == "E"))

    ### PART ONE ###

    start: tuple = tuple(x[0] for x in np.where(npgrid == "S"))
    print(f"Getting from S to E takes at least {breadth_first_search(start, goal)} steps")

    ### PART TWO ###

    candidates: list[tuple] = []
    matches = np.where(npgrid == "a")
    for i in range(len(matches[0]) - 1):
        candidates.append(tuple(x[i] for x in matches))
    steps: set = sorted(set([breadth_first_search(start, goal) for start in candidates]))
    steps.remove(0)
    print(f"Getting from any a to E takes at least {steps[0]} steps")

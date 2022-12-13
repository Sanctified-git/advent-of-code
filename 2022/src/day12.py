import numpy as np
from queue import Queue
from utils.io import get_input


def letter(item: tuple) -> str:
    return grid[item[0]][item[1]]


def allowed(current: int, neighbor: tuple):
    nb_ord = ord(letter(neighbor))
    delta = 123 - current if nb_ord == 69 else nb_ord - current
    return True if delta <= 1 else False


def neighbors(item: tuple) -> list[tuple]:
    neighbors: list = []
    current_cost = ord(letter(item))
    h_min, h_max, w_min, w_max = (0, len(grid) - 1, 0, len(grid[0]) - 1)

    if current_cost == 83:
        current_cost = 96
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
    """https://adventofcode.com/2022/day/12"""

    frontier = Queue()
    frontier.put(start, 0)
    came_from = {start: None}
    steps = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal and letter(came_from[current]) == "z":
            while came_from[current]:
                steps += 1
                current = came_from[current]

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

    start: tuple = tuple(x[0] for x in np.where(npgrid == "S"))

    ### PART ONE ###

    goal: tuple = tuple(x[0] for x in np.where(npgrid == "E"))
    print(f"Getting from S to E takes at least {breadth_first_search(start, goal)} steps")

    ### PART TWO ###

    candidates: list[tuple] = []
    match = np.where(npgrid == "a")
    for i in range(len(match[0]) - 1):
        candidates.append(tuple(x[i] for x in match))
    steps: set = sorted(set([breadth_first_search(start, goal) for start in candidates]))
    steps.remove(0)
    print(f"Getting from any a to E takes at least {steps[0]} steps")

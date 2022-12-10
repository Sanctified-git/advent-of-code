from utils.io import *


def priority(c: str) -> int:
    """Compute the priority of an item"""
    if c >= "a":
        return ord(c) - ord("a") + 1  # from 1 to 26
    else:
        return ord(c) - ord("A") + 27  # from 27 to 52


def day3():
    """https://adventofcode.com/2022/day/3"""
    input: list = get_input(__file__)

    ### PART ONE ###
    result = 0

    for l in input:
        c1 = l[: int(len(l) / 2)]
        c2 = l[int(len(l) / 2) :]
        result += priority("".join(set(c1).intersection(c2)))
    print(
        f"The sum of the priorities of the all the items common to both compartments of a rucksack is {result}"
    )

    ### PART TWO ###
    result2 = 0

    for i in range(0, len(input), 3):
        result2 += priority(
            "".join(set(input[i]).intersection(input[i + 1], input[i + 2]))
        )

    print(f"The sum of the priorities of all the group badges is {result2}")


if __name__ == "__main__":
    day3()

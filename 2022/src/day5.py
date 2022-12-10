from utils.io import *


def day5(crateMover9001: bool = False):
    """https://adventofcode.com/2022/day/5"""
    input: list = get_input(__file__)

    stacks_raw = [
        (
            row.replace("    ", " [ ]")
            .strip()
            .replace("[", "")
            .replace("] ", "")
            .replace("]", "")
        )  # Remove all brackets
        for row in input[:8]
    ]

    stack: dict[int, list[str]] = {}
    for i in range(len(stacks_raw[0])):
        # Process the input to populate each list in the dictionary
        stack[i + 1] = list(reversed([row[i] for row in stacks_raw if row[i] != " "]))

    for l in input[10:]:
        step = l.split(" ")
        to_move = int(step[1])  # Amount of crates to move
        src = int(step[3])  # Source stack
        dst = int(step[5])  # Destination stack

        if not crateMover9001:
            ### PART ONE  ###
            for i in range(to_move):
                if len(stack[src]) > 0:
                    stack[dst].append(stack[src].pop())
        else:
            ### PART TWO ###
            stack[dst].extend(stack[src][-to_move:])
            stack[src] = stack[src][:-to_move]

    res = ""
    for i in range(9):
        res += stack[i + 1].pop()
    return res


if __name__ == "__main__":
    print(
        f"The top of the stacks is {day5(False)} with the CrateMover 9000 and {day5(True)} with the CrateMover 9001"
    )

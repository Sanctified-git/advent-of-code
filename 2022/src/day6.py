from utils.io import *
from utils.timer import Timer


def day6(marker_size: int):
    """https://adventofcode.com/2022/day/6"""
    input: list = [*get_input(__file__)[0]]
    processed = marker_size
    for i in range(marker_size, len(input)):
        if len(set(input[i - marker_size : i])) != marker_size:
            processed += 1
        else:
            return processed


if __name__ == "__main__":
    t = Timer()

    ### PART ONE ###
    t.start()
    print(f"First start-of-packet marker found after processing {day6(4)} characters.")
    t.step()

    ### PART TWO ###
    print(f"First start-of-message marker found after processing {day6(14)} characters.")
    t.stop()
    
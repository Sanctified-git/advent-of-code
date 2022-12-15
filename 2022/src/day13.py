"""https://adventofcode.com/2022/day/13"""
from utils.io import get_input
from ast import literal_eval
from functools import cmp_to_key


def is_ordered(left, right) -> bool:
    # Manage cases where at least one operand is an integer
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    elif isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]

    # When we get to this point, both operands are lists
    # Check if any of the operands are empty
    if (not right) and not left:
        return None
    elif not left:
        return True
    elif not right:
        return False

    i = 0
    ordered = None
    while i < len(left) and ordered is None:
        if i >= len(right):  # The right list is shorter therefore the pair is in the wrong order
            return False
        ordered = is_ordered(left[i], right[i])
        if ordered is None and i == len(left) - 1 and i < len(right) - 1:
            # The left list is shorter than the right with all else being equal, which is the correct order
            return True
        i += 1
    return ordered


def compare(left: str, right: str) -> int:
    return bool_to_cmp[is_ordered(literal_eval(left), literal_eval(right))]


def count_ordered_pairs(pairs: list) -> int:
    count = 0
    for i in range(len(pairs)):
        left, right = [literal_eval(packet) for packet in pairs[i].split("\n")]
        if is_ordered(left, right) in [True, None]:
            count += i + 1
    return count


if __name__ == "__main__":
    packet_pairs: list = get_input(__file__, "\n\n")
    
    ### PART ONE ###
    print(f"{count_ordered_pairs(packet_pairs)} pairs of packets are in the right order")

    ### PART TWO ###
    divider_packets: list = ["[[2]]", "[[6]]"]
    packets: list = divider_packets
    bool_to_cmp: dict = {True: -1, None: 0, False: 1} # These are the values expected by sorted()

    for p in packet_pairs:
        packets.extend(p.split("\n"))
    sorted_packets: list = sorted(packets, key=cmp_to_key(compare))
    decoder_key = (sorted_packets.index(divider_packets[0]) + 1) * (sorted_packets.index(divider_packets[1]) + 1)
    print(f"The decoder key for the distress signal is {decoder_key}")

from utils.io import get_input
from utils.timer import Timer


def scenic_score(i: int, j: int) -> int:
    """Compute a tree's scenic score"""
    global input, i_max, j_max
    # Height of the tree whose scenic score is being computed
    reference = int(input[i][j])
    # Partial sums for each direction
    N_sum, S_sum, E_sum, W_sum = (0, 0, 0, 0)

    for N in reversed(range(0, i)):  # North
        N_sum += 1
        if reference <= int(input[N][j]):
            break
    for S in range(i + 1, i_max):  # South
        S_sum += 1
        if reference <= int(input[S][j]):
            break
    for W in reversed(range(0, j)):  # West
        W_sum += 1
        if reference <= int(input[i][W]):
            break
    for E in range(j + 1, j_max):  # East
        E_sum += 1
        if reference <= int(input[i][E]):
            break

    return N_sum * S_sum * W_sum * E_sum


def day8():
    """https://adventofcode.com/2022/day/8"""
    global input, i_max, j_max
    max_scenic_score = 0
    # All the trees on the edge of the grid are visible
    visible_trees = 2 * i_max + 2 * (j_max - 2)
    # The subtraction accounts for the trees on the corners of the grid which would otherwise be counted twice

    for i in range(1, i_max - 1):
        for j in range(1, j_max - 1):  # For every tree, check if :
            if (
                # The tree is taller than all trees to its right
                int(input[i][j]) > max(int(input[i][x]) for x in range(j))
                or
                # The tree is taller than all trees above it
                int(input[i][j]) > max(int(input[x][j]) for x in range(i))
                or
                # The tree is taller than all trees to its left
                int(input[i][j]) > max(int(input[i][x]) for x in range(j + 1, j_max))
                or
                # The tree is taller than all trees below it
                int(input[i][j]) > max(int(input[x][j]) for x in range(i + 1, i_max))
            ):
                # If any of the above statements is true, the tree is visible from the outside
                visible_trees += 1

            # Set new maximum scenic score value if the current tree beats the stored value
            max_scenic_score = max(scenic_score(i, j), max_scenic_score)

    print(f"{visible_trees} trees are visible from outside the grid")
    print(f"The highest scenic score is {max_scenic_score}")


if __name__ == "__main__":
    t = Timer()
    input: list = get_input(__file__)
    i_max = len(input)
    j_max = len(input[0])
    t.start()
    day8()
    t.stop()

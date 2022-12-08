from utils.io import get_input

def day8():
    input: list = get_input(__file__)
    i_max = len(input)
    j_max = len(input[0])

    visible_trees = 2*i_max + 2*(j_max-2) # All the trees on the edge of the grid are visible

    for i in range(1, i_max-1):
        for j in range(1, j_max-1):
            if (
                    int(input[i][j]) > max(int(input[i][x]) for x in range(j)) or
                    int(input[i][j]) > max(int(input[x][j]) for x in range(i)) or
                    int(input[i][j]) > max(int(input[i][x]) for x in range(j+1, j_max)) or
                    int(input[i][j]) > max(int(input[x][j]) for x in range(i+1, i_max))
                ):
                visible_trees += 1
                
    print(f"{visible_trees} trees are visible from outside the grid")

if __name__ == "__main__":
    day8()

from os.path import splitext, basename
from utils.io import *

def day1():
    input: list = get_input(splitext(basename(__file__))[0])
    sum: list[int] = [0]

    for l in input:
        if l == "":
            sum.append(0)
        else:
            sum[len(sum)-1] += int(l)
    sum.sort(reverse=True)

    print(f"The maximum gathered is {sum[0]} calories")
    print(f"The top three elves collectively gathered {sum[0]+sum[1]+sum[2]} calories")


if __name__ == "__main__":
    day1()
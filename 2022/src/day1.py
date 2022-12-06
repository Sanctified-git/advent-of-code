from utils.io import get_input

def day1():
    input: list = get_input(__file__).split('\n')
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

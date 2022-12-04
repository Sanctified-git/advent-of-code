def main():
    with open("1/input.txt", 'r', encoding="utf-8") as f:
        input_list: list = f.read().split('\n')
        sum: list = [0]
        for l in input_list:
            if l == "":
                sum.append(0)
            else:
                sum[len(sum)-1] += int(l)
        sum.sort(reverse=True)
        print(f"The maximum gathered is {sum[0]} calories")
        print(f"The top three elves collectively gathered {sum[0]+sum[1]+sum[2]} calories")


if __name__ == "__main__":
    main()
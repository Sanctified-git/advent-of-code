def priority (c: str): 
    if c >= 'a':
        return ord(c) - ord('a') + 1    ## from 1 to 26
    else:
        return ord(c) - ord('A') + 27   ## from 27 to 52

def main():
    with open("3/input.txt", 'r', encoding="utf-8") as f:
        input_list: list = f.read().split('\n')

        ### PART ONE ###
        result = 0
        for l in input_list:
            c1 = l[:int(len(l)/2)]
            c2 = l[int(len(l)/2):]
            result += priority(''.join(set(c1).intersection(c2)))
        print(f"The sum of the priorities of the all the items common to both compartments of a rucksack is {result}")
            
        ### PART TWO ###
        result2 = 0
        for i in range(0, len(input_list), 3):
            result2 += priority(''.join(set(input_list[i]).intersection(input_list[i+1], input_list[i+2])))

        print(f"The sum of the priorities of all the group badges is {result2}")

if __name__ == "__main__":
    main()
def main():
    with open("2/input.txt", 'r', encoding="utf-8") as f:
        input_list: list = f.read().split('\n')
        
        value: dict = {
            "X": 1,
            "Y": 2,
            "Z": 3
        }

        ### PART ONE ###
        total1 = 0
        for l in input_list:
            round: list = l.split(' ')
            total1 += value[round[1]]
            match round[0]:
                case "A":
                    match round[1]:
                        case "X":
                            total1 += 3
                        case "Y":
                            total1 += 6
                case "B":
                    match round[1]:
                        case "Y":
                            total1 += 3
                        case "Z":
                            total1 += 6
                case "C":
                    match round[1]:
                        case "X":
                            total1 += 6
                        case "Z":
                            total1 += 3
        print(f"The total score for part one is {total1}")

        ### PART TWO ###
        total2 = 0
        for l in input_list:
            round: list = l.split(' ')
            match round[0]:
                case "A": # Rock
                    match round[1]:
                        case "X": # Loss
                            total2 += 3
                        case "Y": # Draw
                            total2 += 4
                        case "Z": # Win
                            total2 += 8
                case "B": # Paper
                    match round[1]:
                        case "X": # Loss
                            total2 += 1
                        case "Y": # Draw
                            total2 += 5
                        case "Z": # Win
                            total2 += 9
                case "C": # Scissors
                    match round[1]:
                        case "X": # Loss
                            total2 += 2
                        case "Y": # Draw
                            total2 += 6
                        case "Z": # Win
                            total2 += 7
        print(f"The total score for part two is {total2}")

if __name__ == "__main__":
    main()
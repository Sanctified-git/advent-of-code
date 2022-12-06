from utils.io import *

def day4():
    input: list = get_input(__file__).split('\n')
    
    include = 0
    overlap = 0
    
    for l in input:
        pair: list = l.split(',')
        a: list[int] = [int(i) for i in pair[0].split('-')]
        b: list[int] = [int(i) for i in pair[1].split('-')]

        ### PART ONE  ###
        if ((a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1])):
            include += 1
        
        ### PART TWO  ###
        if not(a[1] < b[0] or a[0] > b[1]):
            overlap += 1

    print(f"There are {include} assignment pairs where one range includes the other")
    print(f"There are {overlap} overlapping assignment pairs")

if __name__ == "__main__":
    day4()
    
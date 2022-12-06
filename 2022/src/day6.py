from utils.io import *

def day6(marker_size: int):
    input: list = [*get_input(__file__)]
    processed = marker_size
    for i in range(marker_size, len(input)):
        if len(input[i-marker_size:i]) != len(set(input[i-marker_size:i])):
            processed += 1
        else:
            return processed

if __name__ == "__main__":
    print(f"First start-of-packet marker found after processing {day6(4)} characters. \nFirst start-of-message marker found after processing {day6(14)} characters.")
    
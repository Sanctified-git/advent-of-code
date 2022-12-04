from os.path import splitext, basename

def get_input(filename: str) -> list[str]:
    path: str = "2022/res/" + filename + ".txt"
    with open(path, 'r', encoding="utf-8") as f:
        return f.read().split('\n')

def strip_name(filename: str):
    return splitext(basename(filename))[0]
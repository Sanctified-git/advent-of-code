from os.path import splitext, basename


def get_input(filename: str) -> list[str]:
    """Return the input file corresponding to a given filename as a list."""
    path: str = "2022/res/" + strip_name(filename) + ".txt"
    with open(path, "r", encoding="utf-8") as f:
        return f.read().split("\n")


def strip_name(filename: str) -> str:
    """Remove path and extension from a given file path, returning only the file name."""
    return splitext(basename(filename))[0]

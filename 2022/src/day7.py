from utils.io import get_input
from utils.timer import Timer

MAX_SIZE = 100000
TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000


class File:
    def __init__(self, size=0) -> None:
        self.size = size


class Directory:
    def __init__(self) -> None:
        self.dirs: dict[str, Directory] = {}  # Container for subdirectories
        # Container for files in the directory
        self.files: dict[str, File] = {}

    def add_file(self, name, size):
        if name not in self.files:
            self.files[name] = File(size)

    def add_dir(self, name):
        if name not in self.dirs:
            self.dirs[name] = Directory()


def update_path(path: list[str], new_dir: str):
    """Update current path with the new directory"""
    if new_dir == ".." and path:
        path.pop()  # Go back one directory
    else:
        path.append(new_dir)  # Go into the given subdirectory


def insert_node(tree: Directory, node: str, path: list[str]):
    """Insert new node in the tree at a given path"""
    if not path:
        val, name = node.split(" ")
        if val == "dir":
            tree.add_dir(name)
        else:
            tree.add_file(name, int(val))
    else:
        insert_node(tree.dirs[path[0]], node, path[1:])


def dir_size(tree: Directory, find_candidate: bool = False) -> int:
    """Compute the size of all directories"""
    global result, to_delete, candidate
    # Sum the sizes of all files in this directory
    subtree_size = sum(f.size for f in tree.files.values())

    for d in tree.dirs.values():  # Recursively sum the sizes of the subdirectories
        subtree_size += dir_size(d, find_candidate)

    if not find_candidate and subtree_size <= MAX_SIZE:  # PART ONE
        result += subtree_size

    # PART TWO
    if (
        find_candidate
        and subtree_size > to_delete
        and (subtree_size < candidate or candidate == 0)
    ):
        candidate = subtree_size

    return subtree_size


def day7():
    """https://adventofcode.com/2022/day/7"""
    input: list[str] = get_input(__file__)
    t = Timer()
    root = Directory()  # Container for the filesystem tree
    # Path to the current working directory in the tree
    cur_path: list[str] = []
    global to_delete, candidate

    t.start()
    print("Preparing filesystem")
    # Skip the first line because it is pointless for us
    iterator = iter(range(1, len(input)))
    for i in iterator:
        if input[i][0] == "$":
            command = input[i][2:]
            match str(command[:2]):
                case "ls":
                    while i + 1 < len(input) and input[i + 1][0] != "$":
                        i = next(iterator)
                        insert_node(root, input[i], cur_path)
                case "cd":
                    update_path(cur_path, str(command[3:]))
    t.step()

    to_delete = NEEDED_SPACE + dir_size(root) - TOTAL_SPACE
    print(f"The total size of all the directories of at most {MAX_SIZE} is {result}")
    t.step()

    dir_size(root, True)
    print(f"The size of smallest directory that would free enough space is {candidate}")
    t.stop()


if __name__ == "__main__":

    result = 0
    to_delete = 0
    candidate = 0

    day7()

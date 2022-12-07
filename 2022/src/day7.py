from utils.io import get_input

MAX_SIZE = 100000
TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000

class File():
    def __init__(self, size = 0) -> None:
        self.size = size

class Directory():
    def __init__(self, dirs = {}, files = {}) -> None:
        self.dirs: dict[str, Directory] = dirs  # Container for subdirectories
        self.files: dict[str, File] = files     # Container for files in the directory

def update_path(path:list[str], new_dir: str): # Update current path with the new directory
    if new_dir == '..' and path:
        path.pop() # Go back one directory
    else:
        path.append(new_dir) # Go into the given subdirectory

def insert_node(tree: Directory, node: str, path: list[str]): # Insert new node in the tree at a given path
    if not path:
        size, name = node.split(' ')
        if name not in dict(tree.dirs, **tree.files):
            if size == 'dir':
                tree.dirs[name] = Directory()
            else:
                tree.files[name] = File(int(size))
    else:
        insert_node(tree.dirs[path[0]], node, path[1:])

def dir_size(tree: Directory, find_candidate: bool = False) -> int: # Compute the size of all directories
    global result, to_delete, candidate
    subtree_size = sum(f.size for f in tree.files.values()) # Sum the sizes of all files in this directory
    
    for d in tree.dirs.values(): # Recursively sum the sizes of the subdirectories
        subtree_size += dir_size(d, find_candidate)
    
    if not find_candidate and subtree_size <= MAX_SIZE: # PART ONE
        result += subtree_size

    if find_candidate and subtree_size > to_delete and (subtree_size < candidate or candidate == 0): # PART TWO
        candidate = subtree_size
    
    return subtree_size

def day7():
    input: list[str] = get_input(__file__)
    root = Directory('/')                   # Container for the filesystem tree
    cur_path: list[str] = []                # Path to the current working directory in the tree
    global to_delete, candidate

    iterator = iter(range(1, len(input)))   # Skip the first line because it is pointless for us
    for i in iterator:
        if input[i][0] == '$':
            command = input[i][2:]
            match str(command[:2]):
                case 'ls':
                    while (i+1 < len(input) and input[i+1][0] != '$'):
                        i = next(iterator)
                        insert_node(root, input[i], cur_path)
                case 'cd':
                    update_path(cur_path, str(command[3:]))

    to_delete = NEEDED_SPACE + dir_size(root) - TOTAL_SPACE

    print(f"The total size of all the directories of at most {MAX_SIZE} is {result}")

    dir_size(root, True)

    print(f"The size of smallest directory that would free enough space is {candidate}")

if __name__ == "__main__":
    
    result = 0
    to_delete = 0
    candidate = 0

    day7()

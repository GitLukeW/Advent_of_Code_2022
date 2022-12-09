import sys
from pathlib import Path
from collections import deque


def crates(input):
    data = input.split("\n\n")
    moves = data[0].split("\n")
    print(data)
    print("-------------")
    print(moves)
    print("-------------")
    stack = deque()
    stack.append(moves)
    print(stack)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        crates(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

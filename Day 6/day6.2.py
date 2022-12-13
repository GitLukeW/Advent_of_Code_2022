import sys
from pathlib import Path


def first_four(input):
    window_size = 14

    for list in range(len(input) - window_size + 1):
        four_group = (input[list: list + window_size])
        if len(set(four_group)) == len(four_group):
            print(four_group)
            print(list + window_size)
            break


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        first_four(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

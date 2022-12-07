import sys
import re
from pathlib import Path


def doubled_up(input):
    team = input.split('\n')
    count = 0
    for pair in team:
        nums = re.sub('\D', ' ', pair)
        sep = list(map(int, nums.split()))
        group_one = set(range(sep[0], sep[1]+1))
        group_two = set(range(sep[2], sep[3]+1))
        if group_one.intersection(group_two):
            count += 1
    print(count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        doubled_up(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

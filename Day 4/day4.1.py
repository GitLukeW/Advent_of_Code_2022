import sys
import re
from pathlib import Path


def doubled_up(input):
    team = input.split('\n')
    count = 0
    for pair in team:
        nums = re.sub('\D', ' ', pair)
        sep = list(map(int, nums.split()))
        first_contains_last = (sep[0] <= sep[2]) and (sep[1] >= sep[3])
        last_contains_first = (sep[0] >= sep[2]) and (sep[1] <= sep[3])
        if first_contains_last or last_contains_first:
            count += 1
    print(count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        doubled_up(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

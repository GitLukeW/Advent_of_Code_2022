import sys
import re
from pathlib import Path


def doubled_up(input):
    team = input.split('\n')
    count = 0
    for pair in team:
        nums = re.sub('\D', ' ', pair)
        sep = list(map(int, nums.split()))
        if (sep[0] <= sep[2]) and (sep[1] >= sep[3]):
            count += 1
        elif (sep[0] >= sep[2]) and (sep[1] <= sep[3]):
            count += 1
    print(count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        doubled_up(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

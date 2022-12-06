import sys
import string
from pathlib import Path


def rucksack(input):
    data = (input.split("\n"))
    group = list(data[i:i+3] for i in range(0, len(data), 3))

    alpha = string.ascii_letters
    points = {}
    sum = 0

    for i in range(len(alpha)):
        points[alpha[i]] = i+1

    for item in group:
        for line in item:
            for letter in line:
                if (letter in item[0]) and (letter in item[1]) and (letter in
                                                                    item[2]):
                    sum += points[letter]
                    break
    print(sum/3)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        rucksack(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

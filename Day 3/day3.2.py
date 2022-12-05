import sys
from pathlib import Path


def rucksack(input):
    data = (input.split("\n"))

    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    points = {}
    sum = 0

    for i in range(len(alpha)):
        points[alpha[i]] = i+1

    for item in data:
        first_half = item[:len(item)//2]
        second_half = item[len(item)//2:]
        for letter in first_half:
            if letter in second_half:
                sum += points[letter]
                break
    print(sum)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        rucksack(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

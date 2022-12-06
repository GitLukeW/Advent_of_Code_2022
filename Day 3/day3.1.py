import sys
import string
from pathlib import Path


def rucksack(input):
    data = (input.split("\n"))

    alpha = string.ascii_letters
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



import sys
from pathlib import Path
def rucksack(input):
    data = (input.split("\n"))
    # slight improvement -> look up the alphabet instead of typing
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    points = {}
    sum = 0
    for i in range(len(alpha)):
        points[alpha[i]] = i+1
    for item in data:
        first_half = item[:len(item)//2]
        second_half = item[len(item)//2:]
        # start #
        second_half_character_counts = {}
        for char in second_half:
             second_half_character_counts[char] = second_half_character_counts.get(char, 0) + 1
        # end #
        for letter in first_half:
            # does python have some optimization for checking "if char in str"? (I'm not actually sure..)
            # if not, this is a linear time lookup (you have to look through potentially all characters of the second_half for each letter in the first)
            if second_half_character_counts.get(letter):
                sum += points[letter]
                break
    print(sum)
    return sum

# tests
print(rucksack('FFaFFa') == 32)
                # 12 * 12 (n / 2 * n / 2)
                # 12 * 1 (n / 2)
                #         O(n^2) (was O n squared, inefficient)
                #         O(n) now it's O(n), much more efficient
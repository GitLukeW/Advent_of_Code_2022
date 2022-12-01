import sys
from pathlib import Path


def calorie_count(input):
    data = (input.split("\n"))
    calorie_count = 0
    max_calories = 0
    for nums in data:
        if nums == '':
            calorie_count = 0
        else:
            calories = nums
            calorie_count += int(calories)

        if calorie_count > max_calories:
            max_calories = calorie_count
    print(max_calories)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        calorie_count(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

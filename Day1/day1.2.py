import sys
import heapq
from pathlib import Path


def top_three(input):
    data = (input.split("\n"))
    calorie_count = 0
    max_calories = []
    for nums in data:
        if nums != '':
            calorie_count += int(nums)
            continue
        max_calories.append(calorie_count)
        calorie_count = 0
        print(heapq.nlargest(3, zip(max_calories)))
        max_calories.sort(reverse=True)
        print(sum(max_calories[:3]))


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        top_three(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

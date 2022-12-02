import sys
from pathlib import Path


# Row 1: A = Rock, B = Paper, C = Scissors
# Row 2: X = Rock, Y = Paper, Z = Scissors
# Score Per Shape: 1 = Rock, 2 = Paper, 3 = Scissors
# Score Per Outcome: 0 = Loss, 3 = Draw, 6 = Win
# Secret Outcome: X = Loss, Y = draw, Z = Win

def rps_game(input):
    data = input.split("\n")
    draw = 3
    win = 6
    loss = 0

    rock = 1
    paper = 2
    scissors = 3

    game_points = 0

    game = {

        'A X': loss + scissors,
        'A Y': draw + rock,
        'A Z': win + paper,
        'B X': loss + rock,
        'B Y': draw + paper,
        'B Z': win + scissors,
        'C X': loss + paper,
        'C Y': draw + scissors,
        'C Z': win + rock
    }

    for n in data:
        if n in data:
            game_points += game[n]
    print(game_points)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        rps_game(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

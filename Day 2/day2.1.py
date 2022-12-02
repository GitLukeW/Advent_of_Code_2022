import sys
from pathlib import Path


# Row 1: A = Rock, B = Paper, C = Scissors
# Row 2: X = Rock, Y = Paper, Z = Scissors
# Score Per Shape: 1 = Rock, 2 = Paper, 3 = Scissors
# Score Per Outcome: 0 = Loss, 3 = Draw, 6 = Win

def rps_game(input):
    data = (input.split("\n"))
    draw = 3
    win = 6
    loss = 0
    game_points = 0

    game = {

        'A X': draw + 1,
        'A Y': win + 2,
        'A Z': loss + 3,
        'B X': loss + 1,
        'B Y': draw + 2,
        'B Z': win + 3,
        'C X': win + 1,
        'C Y': loss + 2,
        'C Z': draw + 3
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

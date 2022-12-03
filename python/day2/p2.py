from pathlib import Path


def get_data(day: int):
    path_input = Path(__file__).parent.parent.parent / "input" / f"day{day}"

    with open(str(path_input), "r") as f:
        data = f.read().split("\n")

    return data


points = {
    # x - lose
    # y - draw
    # z - win
    # rock
    ("A", "X"): 3,  # lose   0 + 3 scissors
    ("A", "Y"): 4,  # tie:   3 + 1 rock
    ("A", "Z"): 8,  # win:   6 + 2 paper
    # paper
    ("B", "X"): 1,  # lose   0 + 1 rock
    ("B", "Y"): 5,  # tie    3 + 2 paper
    ("B", "Z"): 9,  # win    6 + 3 scissors
    # scissors
    ("C", "X"): 2,  # lose   0 + 2 paper
    ("C", "Y"): 6,  # tie    3 + 3 scissors
    ("C", "Z"): 7,  # win    6 + 1 rock
}


def run():
    score = 0
    for line in get_data(2):
        if not line:
            continue
        op, result = line.split()

        score += points[op, result]

    print(score)


if __name__ == "__main__":
    run()

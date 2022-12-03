from pathlib import Path


def get_data(day: int):
    path_input = Path(__file__).parent.parent.parent / "input" / f"day{day}"

    with open(str(path_input), "r") as f:
        data = f.read().split("\n")

    return data


points = {
    ("A", "X"): 4,
    ("A", "Y"): 8,
    ("A", "Z"): 3,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 7,
    ("C", "Y"): 2,
    ("C", "Z"): 6,
}


def run():
    score = 0
    for line in get_data(2):
        if not line:
            continue
        print("line", line)
        op, me = line.split()

        score += points[op, me]

    return score


if __name__ == "__main__":
    res = run()
    print(res)

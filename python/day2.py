def p1(data):
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

    score = 0
    for line in data:
        if not line:
            continue
        op, me = line.split()

        score += points[op, me]

    return score


def p2(data):
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

    score = 0
    for line in data:
        if not line:
            continue
        op, result = line.split()

        score += points[op, result]

    return score


def run(data):
    print(p1(data))
    print(p2(data))

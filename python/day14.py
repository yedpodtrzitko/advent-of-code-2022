def p1(data):

    grid = {}

    min_x, max_x = 999, 0
    min_y, max_y = 999, 0
    for line in data:
        line_coords = []
        for x in line.split("->"):
            x, y = x.split(",")
            # min_x = min(min_x, x)
            # min_y = min(min_y, y)
            # max_x = max(max_x, x)
            # max_y = max(max_y, y)
            line_coords.append([int(x.strip()), int(y.strip())])

        for p2_idx, p1 in enumerate(line_coords[:-1], start=1):
            p2 = line_coords[p2_idx]
            print("p1 p2", p1, p2)

            cursor = p1
            counter = 0
            while True:
                counter += 1
                if counter > 10:
                    break
                grid[tuple(cursor)] = "#"
                if cursor[0] > p2[0]:
                    cursor[0] -= 1
                elif cursor[0] < p2[0]:
                    cursor[0] += 1
                elif cursor[1] < p2[1]:
                    cursor[1] += 1
                elif cursor[1] > p2[1]:
                    cursor[1] -= 1
                elif cursor == p2:
                    break
                else:
                    print(cursor, p2)
                    raise Exception("unexpected")

    while True:
        S = [500, 0]
        below = [S[0] - 1, S[1]]


def p2(data):
    pass


def run(data):
    print(p1(data))
    # print(p2(data))


def test_p1():
    data_expected = 13

    data_raw = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p1(data_lines)
    assert res == data_expected

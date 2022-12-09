from copy import copy


MOVE = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1],
}


def p1(data):
    commands = []
    for line in data:
        direction, length = line.strip().split()
        commands.extend([direction] * int(length))

    h_pos = [0, 0]
    t_pos = [0, 0]
    t_history = {(0, 0)}
    for h_move in commands:
        h_pos[0] += MOVE[h_move][0]
        h_pos[1] += MOVE[h_move][1]

        diff_x = h_pos[0] - t_pos[0]
        diff_y = h_pos[1] - t_pos[1]
        if (abs(diff_x) + abs(diff_y)) > 2:
            t_pos[0] += 1 if diff_x > 0 else -1
            t_pos[1] += 1 if diff_y > 0 else -1
        elif abs(diff_x) > 1:
            t_pos[0] += 1 if diff_x > 0 else -1
        elif abs(diff_y) > 1:
            t_pos[1] += 1 if diff_y > 0 else -1

        t_history.add(tuple(t_pos))

    return len(t_history)


def p2(data):
    commands = []
    for line in data:
        direction, length = line.strip().split()
        commands.extend([direction] * int(length))

    all_nodes = {x: [0, 0] for x in range(10)}
    t_history = set()
    for h_move in commands:
        for node_idx, node_pos in all_nodes.items():
            if node_idx == 0:
                node_pos[0] += MOVE[h_move][0]
                node_pos[1] += MOVE[h_move][1]
                continue

            diff_x = all_nodes[node_idx - 1][0] - node_pos[0]
            diff_y = all_nodes[node_idx - 1][1] - node_pos[1]
            if (abs(diff_x) + abs(diff_y)) > 2:
                node_pos[0] += 1 if diff_x > 0 else -1
                node_pos[1] += 1 if diff_y > 0 else -1
            elif abs(diff_x) > 1:
                node_pos[0] += 1 if diff_x > 0 else -1
            elif abs(diff_y) > 1:
                node_pos[1] += 1 if diff_y > 0 else -1

            if node_idx == 9:
                t_history.add(tuple(node_pos))

    return len(t_history)


def run(data):
    print(p1(data))
    print(p2(data))


def test_p1():
    data_expected = 13

    data_raw = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p1(data_lines)
    assert res == data_expected


def test_p2():
    data_expected = 36

    data_raw = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p2(data_lines)
    assert res == data_expected

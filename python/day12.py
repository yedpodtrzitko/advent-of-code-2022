from copy import copy
from math import floor, lcm

import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, height):
        self.distance = None
        self.height = ord(height) - 96
        self.letter = height
        if self.letter == "E":
            # E is next to z
            self.height = ord("z") - 96 + 1
        if self.letter == "S":
            self.height = 0
            self.distance = 0


def p1(data):
    grid = []
    EX, EY = None, None
    SX, SY = None, None

    for line in data:
        grid.append([Node(x) for x in line])
        if "E" in line:
            EX = len(grid) - 1
            EY = line.index("E")
        if "S" in line:
            SX = len(grid) - 1
            SY = line.index("S")

    grid_rows = len(grid)
    grid_cols = len(grid[0])

    def visit_node(x, y):
        this_node = grid[x][y]
        if this_node.letter == "E":
            print("E distance", this_node.distance)
            # return

        for (ox, oy) in [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]:
            nx, ny = ox + x, oy + y
            if not ((0 <= nx < grid_rows) and (0 <= ny < grid_cols)):
                continue

            neigbour = grid[nx][ny]
            if neigbour.height > this_node.height + 1:
                continue

            if neigbour.distance is None:
                neigbour.distance = this_node.distance + 1
                visit_node(nx, ny)

            elif neigbour.distance > (this_node.distance + 1):
                # revisit neigbour through shorter path
                neigbour.distance = this_node.distance + 1
                visit_node(nx, ny)
            elif neigbour.distance < (this_node.distance - 1):
                # revisit neigbour since it can be closer
                visit_node(nx, ny)
            elif neigbour.distance == this_node.distance + 1:
                pass
            elif neigbour.distance == this_node.distance - 1:
                pass
            else:
                print("else wtf", x, y, " - ", neigbour.distance, this_node.distance)

    visit_node(SX, SY)
    return grid[EX][EY].distance - 2


def p2(data):
    grid = []
    EX, EY = None, None
    SX, SY = None, None

    for line in data:
        grid.append([Node(x) for x in line])
        if "E" in line:
            EX = len(grid) - 1
            EY = line.index("E")
        if "S" in line:
            SX = len(grid) - 1
            SY = line.index("S")

    grid_rows = len(grid)
    grid_cols = len(grid[0])

    def visit_node(x, y):
        this_node = grid[x][y]
        if this_node.letter == "E":
            print("E distance", this_node.distance)
            # return

        for (ox, oy) in [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]:
            nx, ny = ox + x, oy + y
            if not ((0 <= nx < grid_rows) and (0 <= ny < grid_cols)):
                continue

            neigbour = grid[nx][ny]
            if neigbour.height > this_node.height + 1:
                continue

            if neigbour.distance is None:
                neigbour.distance = this_node.distance + 1
                visit_node(nx, ny)

            elif neigbour.distance > (this_node.distance + 1):
                # revisit neigbour through shorter path
                neigbour.distance = this_node.distance + 1
                visit_node(nx, ny)
            elif neigbour.distance < (this_node.distance - 1):
                # revisit neigbour since it can be closer
                visit_node(nx, ny)
            elif neigbour.distance == this_node.distance + 1:
                pass
            elif neigbour.distance == this_node.distance - 1:
                pass
            else:
                print("else wtf", x, y, " - ", neigbour.distance, this_node.distance)

    visit_node(SX, SY)
    return grid[EX][EY].distance - 2


def run(data):
    print(p1(data))
    # print(p2(data))


def test_p1():
    data_expected = 31

    data_raw = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p1(data_lines)
    assert res == data_expected


def test_p2():
    data_expected = 29

    data_raw = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p1(data_lines)
    assert res == data_expected

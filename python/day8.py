from collections import defaultdict
from enum import Enum


class DIR(str, Enum):
    TOP = "TOP"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    BOTTOM = "BOTTOM"


def get_dict():
    return {
        DIR.TOP: 9,
        DIR.LEFT: 9,
        DIR.RIGHT: 9,
        DIR.BOTTOM: 9,
    }


def p1(data):
    idx_last = len(data) - 1

    TALLEST = defaultdict(get_dict)

    grid = []
    for line in data:
        grid.append([int(x) for x in line])

    for idx_y, line in enumerate(grid):
        # fill highest from left
        for idx_x, cell in enumerate(line):
            if idx_x == 0:
                dir_tallest = cell
            else:
                prev_tallest = TALLEST[idx_x - 1, idx_y][DIR.LEFT]
                prev_cell = grid[idx_y][idx_x - 1]
                dir_tallest = max(prev_cell, prev_tallest)

            TALLEST[idx_x, idx_y][DIR.LEFT] = dir_tallest

            # fill tallest from top
            if idx_y == 0:
                tallest_top = cell
            else:
                prev_tallest_top = TALLEST[idx_x, idx_y - 1][DIR.TOP]
                prev_cell = grid[idx_y - 1][idx_x]
                tallest_top = max(prev_tallest_top, prev_cell)

            TALLEST[idx_x, idx_y][DIR.TOP] = tallest_top

        # fill highest from right
        for idx_x, cell in reversed(list(enumerate(line))):
            if idx_x == idx_last:
                dir_tallest = cell
            else:
                prev_tallest = TALLEST[idx_x + 1, idx_y][DIR.RIGHT]
                prev_cell = grid[idx_y][idx_x + 1]
                dir_tallest = max(prev_cell, prev_tallest)

            TALLEST[idx_x, idx_y][DIR.RIGHT] = dir_tallest
            if dir_tallest == 9:
                # print('breaking from right ', idx_x, idx_y)
                break

    # fill tallest from bottom
    for idx_y, line in reversed(list(enumerate(grid))):
        for idx_x, cell in enumerate(line):
            if idx_y == idx_last:
                dir_tallest = cell
            else:
                prev_tallest = TALLEST[idx_x, idx_y + 1][DIR.BOTTOM]
                prev_cell = grid[idx_y + 1][idx_x]
                dir_tallest = max(prev_cell, prev_tallest)

            TALLEST[idx_x, idx_y][DIR.BOTTOM] = dir_tallest

    visibles = []
    SET_EDGES = {0, idx_last}
    for idx_y, line in enumerate(grid):
        for idx_x, cell in enumerate(line):
            cell_coords = (idx_x, idx_y)
            if set([idx_x, idx_y]) & SET_EDGES:
                visibles.append(cell_coords)
                continue

            if [x for x in TALLEST[idx_x, idx_y].values() if x < cell]:
                visibles.append(cell_coords)

    return len(visibles)


def p2(data):
    idx_last = len(data) - 1
    highest_score = 0

    grid = []
    for line in data:
        grid.append([int(x) for x in line])

    for idx_y, line in enumerate(grid):
        if idx_y in (0, idx_last):
            continue

        for idx_x, cell in enumerate(line):
            if idx_x in (0, idx_last):
                continue

            visible_left = 0
            visible_right = 0
            visible_top = 0
            visible_bottom = 0

            idx_look_left = idx_x - 1
            idx_look_right = idx_x + 1
            idx_look_top = idx_y - 1
            idx_look_bottom = idx_y + 1

            while idx_look_left >= 0:
                inspected_cell = grid[idx_y][idx_look_left]
                visible_left += 1
                idx_look_left -= 1
                if inspected_cell >= cell:
                    break

            while idx_look_right <= idx_last:
                inspected_cell = grid[idx_y][idx_look_right]
                visible_right += 1
                idx_look_right += 1
                if inspected_cell >= cell:
                    break

            while idx_look_top >= 0:
                inspected_cell = grid[idx_look_top][idx_x]
                visible_top += 1
                idx_look_top -= 1
                if inspected_cell >= cell:
                    break

            while idx_look_bottom <= idx_last:
                inspected_cell = grid[idx_look_bottom][idx_x]
                visible_bottom += 1
                idx_look_bottom += 1
                if inspected_cell >= cell:
                    break

            this_score = visible_left * visible_right * visible_top * visible_bottom
            highest_score = max(this_score, highest_score)

    return highest_score


def run(data):
    print(p1(data))
    print(p2(data))


def test_p1():
    data_expected = 21

    data_raw = """
30373
25512
65332
33549
35390"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p1(data_lines)
    assert res == data_expected


def test_p2():
    data_expected = 8

    data_raw = """
30373
25512
65332
33549
35390"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p2(data_lines)
    assert res == data_expected

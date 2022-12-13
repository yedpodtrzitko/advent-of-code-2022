class LeftSmaller(Exception):
    pass


class RightSmaller(Exception):
    pass


def adjust_types(left_value, right_value):
    if type(left_value) != list and type(right_value) == list:
        left_value = [left_value]
    elif type(right_value) != list and type(left_value) == list:
        right_value = [right_value]
    elif type(left_value) == type(right_value) == int:
        if left_value < right_value:
            raise LeftSmaller("")
        elif left_value > right_value:
            raise RightSmaller("")

    if type(left_value) == type(right_value) == list:
        for idx, _ in enumerate(left_value):
            adjust_types(left_value[idx], right_value[idx])

        # right is longer
        raise LeftSmaller("")


def compare_sides(left, right):
    try:
        adjust_types(left, right)
    except LeftSmaller:
        return True
    except RightSmaller:
        return False
    except IndexError:
        return False


def p1(data):
    left, right = None, None
    pair_idx = 1
    correct_sum = 0
    for line in data:
        if not line:
            pair_idx += 1
            left, right = None, None
            continue

        line_eval = eval(line)
        if left is None:
            left = line_eval
        elif right is None:
            # right = line_eval
            if compare_sides(left, line_eval):
                correct_sum += pair_idx

    return correct_sum


def p2(data):
    pass


def run(data):
    print(p1(data))
    # print(p2(data))


def test_p1():
    data_expected = 13

    data_raw = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p1(data_lines)
    assert res == data_expected

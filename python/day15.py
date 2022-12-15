import re


def man_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


RE_SENSOR = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)


def p1(data, Y_SEARCH=2000000):

    sensors = set()
    beacons = set()
    min_x, max_x = 999999999, -999999999
    max_dist = 0
    for line in data:
        match = RE_SENSOR.match(line)
        sx, sy, bx, by = [int(x) for x in match.groups()]
        min_x = min(bx, min_x)
        max_x = max(bx, max_x)

        this_dist = man_dist([sx, sy], [bx, by])
        max_dist = max(max_dist, this_dist)

        sensors.add((sx, sy, this_dist))
        beacons.add((bx, by))

    reach_from = min_x - max_dist
    reach_to = max_x + max_dist

    scanned = 0
    for test_x in range(reach_from, reach_to + 1):
        check_coords = (test_x, Y_SEARCH)
        if check_coords in beacons:
            continue

        for s in sensors:
            y_distance = man_dist(check_coords, s[:2])
            if y_distance <= s[2]:
                scanned += 1
                break

    return scanned


def p2(data):

    sensors = set()
    beacons = set()
    for line in data:
        match = RE_SENSOR.match(line)
        sx, sy, bx, by = [int(x) for x in match.groups()]

        this_dist = man_dist([sx, sy], [bx, by])

        sensors.add((sx, sy, this_dist))
        beacons.add((bx, by))

    def get_x_coverage(y):
        covered_segments = []
        for sx, sy, reach in sensors:
            y_offset = abs(y - sy)
            if y_offset <= reach:
                cover_from = sx - (reach - y_offset)
                cover_to = sx + (reach - y_offset)

                covered_segments.append([cover_from, cover_to])

        return covered_segments

    for test_y in range(0, 4000000):
        x_ints = get_x_coverage(test_y)
        intervals = merge_intervals(x_ints)
        if len(intervals) > 1:
            free_x = intervals[1][0] - 1

            return free_x * 4000000 + test_y


def is_overlaping(a, b):
    return a[0] <= b[0] <= a[1]


def merge_intervals(intervals):
    intervals.sort()
    merged_list = [
        intervals[0],
    ]

    for idx in range(1, len(intervals)):
        if is_overlaping(merged_list[-1], intervals[idx]):
            merged_list[-1][1] = max(merged_list[-1][1], intervals[idx][1])
        else:
            merged_list.append(intervals[idx])
    return merged_list


def run(data):
    print(p1(data))
    print(p2(data))


def test_p1():
    data_expected = 26

    data_raw = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

    data_lines = [x for x in data_raw.split("\n")][1:]
    res = p1(data_lines, 10)
    assert res == data_expected

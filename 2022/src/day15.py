"""https://adventofcode.com/2022/day/14"""
from utils.io import get_input
from utils.timer import Timer
from re import findall

ROW = 2000000
LIMIT = 4000000


def dist(a: complex, b: complex) -> int:
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))


def parse_input(input: list) -> tuple[set, set]:
    beacons: set[complex] = set()
    sensors: set[tuple[complex, int]] = set()
    # container for tuples of :
    # * the sensor's coordinates as a complex number
    # * the manhattan distance to the closest beacon
    for line in input:
        sensor, beacon = tuple(
            complex(int(x), int(y)) for x, y in findall(r"(-?\d+), y=(-?\d+)", line)
        )
        sensors.add(tuple([sensor, dist(sensor, beacon)]))
        beacons.add(beacon)
    return sensors, beacons


def get_overlap(sensors, y) -> tuple[int, int]:
    for sensor, distance in sensors:
        overlap = distance - abs(sensor.imag - y)
        if overlap >= 0:
            yield sensor.real - overlap, sensor.real + overlap


def get_blocked_positions(sensors: set, beacons: set, y: int) -> int:
    left, right = zip(*get_overlap(sensors, y))
    overlapping_beacons = len(set(by for b in beacons if (by := b.imag) == y))
    return max(right) + 1 - min(left) - overlapping_beacons


def get_border(sensor, radius) -> tuple[int, int]:
    for dx in range(radius + 2):
        dy = radius + 1 - dx
        yield sensor.real + dx, sensor.imag + dy
        yield sensor.real + dx, sensor.imag - dy
        yield sensor.real - dx, sensor.imag + dy
        yield sensor.real - dx, sensor.imag - dy


def find_tuning_frequency(sensors: set, limit: int) -> int:
    for sensor, radius in sensors:
        for x, y in get_border(sensor, radius):
            if (
                0 <= x <= limit and 0 <= y <= limit
                and all(dist(s, complex(x, y)) > r for s, r in sensors)
            ):
                return x * LIMIT + y


if __name__ == "__main__":
    t = Timer()
    sensors, beacons = parse_input(get_input(__file__))
    t.start()

    ### PART ONE ###
    print(
        f"{int(get_blocked_positions(sensors, beacons, y=ROW))} positions cannot contain a beacon in row {ROW}"
    )
    t.step()

    ### PART TWO ###
    print(
        f"The distress beacon's tuning frequency is {int(find_tuning_frequency(sensors, limit=LIMIT))}"
    )
    t.stop()

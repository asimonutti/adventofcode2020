
import argparse


def build_map(input):
    map = []
    for index in range(0, len(input)):
        row = []
        for i in input[index]:
            row.append(i)
        map.append(row)
    return map


class Slope:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def apply(self, x_0, y_0):
        return x_0 + self.x, y_0 + self.y

    def __repr__(self):
        return "[{0}, {1}]".format(self.x, self.y)


def check_slope(map, slope):
    encounters = {}
    loc = [0, 0]

    loc[0], loc[1] = slope.apply(loc[0], loc[1])
    while loc[0] < len(map):
        encounter = map[loc[0]][loc[1]]
        if encounter in encounters:
            encounters[encounter] += 1
        else:
            encounters[encounter] = 1
        loc[0], loc[1] = slope.apply(loc[0], loc[1])

        # If we end up off the right side of the map subtract the width of the map to simulate the pattern
        if loc[1] >= len(map[0]):
            loc[1] = loc[1] - len(map[0])

    return encounters["#"]


def main(input):
    map = build_map(input)

    encounter_by_slope = {
        Slope(1, 1): 0,
        Slope(1, 3): 0,
        Slope(1, 5): 0,
        Slope(1, 7): 0,
        Slope(2, 1): 0,
    }

    for slope in encounter_by_slope.keys():
        encounter_by_slope[slope] = check_slope(map, slope)
    print(encounter_by_slope)

    result = 1
    for _, v in encounter_by_slope.items():
        result = result * v
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, nargs=1, help="filename of our input")
    parser.add_argument("--output", type=str, required=False, help="filename of our expected output")
    arguments = parser.parse_args()

    with open(arguments.input[0], "r") as infile:
        input = infile.read().splitlines()

    result = main(input)
    print("Result: {0}".format(result))
    if arguments.output:
        with open(arguments.output, "r") as outfile:
            output = outfile.read().splitlines()[0]
        assert(result == int(output))


import argparse


def main(input):
    for v1 in input:
        for v2 in input:
            for v3 in input:
                if 2020 == (int(v1) + int(v2) + int(v3)):
                    return int(v1) * int(v2) * int(v3)


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

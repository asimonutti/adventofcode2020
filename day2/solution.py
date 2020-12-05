
import argparse


class Rule:
    def __init__(self, val1, val2, char):
        self.val1 = val1
        self.val2 = val2
        self.char = char

    def validate(self, password):
        pass

    @classmethod
    def from_string(cls, string):
        val1 = int(string.split("-")[0])
        val2 = int(string.split(" ")[0].split("-")[1])
        char = string.split(" ")[1]
        return cls(val1, val2, char)

    def __repr__(self):
        return("{0}, {1}, {2}".format(self.val1, self.val2, self.char))


class Part1Rule(Rule):
    def validate(self, password):
        char_map = {}
        for c in password:
            if c in char_map.keys():
                char_map[c] += 1
            else:
                char_map[c] = 1
        if self.char in char_map.keys():
            if char_map[self.char] >= self.val1 and char_map[self.char] <= self.val2:
                return True
        return False


class Part2Rule(Rule):
    def validate(self, password):
        if password[self.val1 - 1] == self.char and password[self.val2 - 1] == self.char:
            return False
        if password[self.val1 - 1] == self.char or password[self.val2 - 1] == self.char:
            return True
        return False


def main(input):
    results = {"valid": 0, "invalid": 0}
    for v in input:
        rule, password = v.split(": ")[0], v.split(": ")[1]
        rule = Part2Rule.from_string(rule)
        if rule.validate(password):
            print(password + " is valid!")
            results["valid"] += 1
        else:
            results["invalid"] += 1
    return results["valid"]


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

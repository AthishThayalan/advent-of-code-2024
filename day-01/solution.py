# Day 1 solution

import os

# PART 1


def parseInput():

    left, right = [], []

    file_path = os.path.join(os.path.dirname(
        __file__), "input.txt")

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            split_line = line.split("  ")
            int_values = [int(value) for value in split_line]
            left.append(int_values[0])
            right.append(int_values[1])
    return (left, right)


def calculate_distance():

    arrays = parseInput()
    l, r = sorted(arrays[0]), sorted(arrays[1])

    return sum([abs(l[i]-r[i]) for i in range(len(l))])


# PART 2

def calculate_similarity():

    arrays = parseInput()
    l, r = sorted(arrays[0]), sorted(arrays[1])

    return sum([l[i] * r.count(l[i]) for i in range(len(l))])


def main():
    # print(calculate_distance())
    print(calculate_similarity())


if __name__ == "__main__":
    main()

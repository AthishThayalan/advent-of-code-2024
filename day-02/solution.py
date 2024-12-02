import os


def parseInput():
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(file_path, "r") as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            matrix.append([int(num) for num in line.split()])
    return matrix


def is_row_safe(row):

    l, r = 0, 1

    is_increasing = row[0] < row[-1]

    while r < len(row):
        diff = row[r] - row[l] if is_increasing else row[l] - row[r]

        if 1 <= diff <= 3:
            l += 1
            r += 1
        else:
            return False

    return True


def calculate_no_safe_reports(use_dampener=False):

    matrix = parseInput()
    result = 0

    for row in matrix:
        if is_row_safe(row):
            result += 1
        elif use_dampener and problem_dampener(row):
            result += 1

    return result

# part 2


def problem_dampener(row):
    # now we need to see if an unsafe row becomes safe after removing erroneous elements.
    # similar logic

    matrix = parseInput()
    result = 0

    for i in range(len(row)):
        modified_row = row[:i] + row[i + 1:]
        if is_row_safe(modified_row):
            return True
    return False


def main():
    # part 1
    # print(calculate_no_safe_reports())

    #  part 2
    print(calculate_no_safe_reports(True))


if __name__ == "__main__":
    main()

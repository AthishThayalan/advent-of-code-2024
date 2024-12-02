import os


def parseInput():
    file_path = os.path.join(os.path.dirname(__file__), "mock_input.txt")

    with open(file_path, "r") as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            matrix.append([int(num) for num in line.split()])
    return matrix


def calculate_no_safe_reports():
    matrix = parseInput()
    result = 0

    for row in matrix:
        l, r = 0, 1
        # Determine if the row is increasing or decreasing
        is_increasing = row[0] < row[-1]

        while r < len(row):
            diff = row[r] - row[l] if is_increasing else row[l] - row[r]

            if 1 <= diff <= 3:
                l += 1
                r += 1
            else:
                break
        else:
            result += 1  # Increment result only if the while loop completes fully

    return result


def main():
    print(calculate_no_safe_reports())


if __name__ == "__main__":
    main()

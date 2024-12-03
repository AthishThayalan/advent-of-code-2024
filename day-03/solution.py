import os
import re


def read_file_as_string(file_name):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))

        os.chdir(script_dir)

        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File not found: {file_name}"
    except Exception as e:
        return f"An error occurred: {e}"


def mull_it_over():
    file_name = "mock_input.txt"
    content = read_file_as_string(file_name)

    pattern = r"(?<!don't\(\))mul\((\d+),(\d+)\)"

    return sum([int(num1) * int(num2) for (num1, num2) in re.findall(pattern, content)])


def mull_it_over_2():
    file_name = "input.txt"
    content = read_file_as_string(file_name)

    pattern = r"(?<!don't\(\))mul\((\d+),(\d+)\)"

    tokens = tokens = re.split(
        r"(\bdo\(\)|\bdon't\(\)|mul\(\d+,\d+\))", content)

    print(tokens)

    is_enabled = True

    result = 0

    for token in tokens:
        if token.startswith("mul(") and is_enabled:
            # had to look up regex and associated syntax
            match = re.match(r"mul\((\d+),(\d+)\)", token)
            if match:
                num1, num2 = map(int, match.groups())
                result += num1 * num2
        elif "do()" in token:
            is_enabled = True
        elif "don't()" in token:
            is_enabled = False
    return result


# part 2 , same thing , but remove the instances which are preceeded by "don't()"
if __name__ == "__main__":
    print(mull_it_over_2())

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
    file_name = "input.txt"
    content = read_file_as_string(file_name)

    pattern = r"mul\((\d+),(\d+)\)"

    return sum([int(num1) * int(num2) for (num1, num2) in re.findall(pattern, content)])


if __name__ == "__main__":
    print(mull_it_over())

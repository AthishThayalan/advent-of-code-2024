import os


def create_day_folder(day):
    day_folder = f"day-{day:02d}"
    os.makedirs(day_folder, exist_ok=True)
    with open(f"{day_folder}/solution.py", "w") as f:
        f.write("# Day {} solution\n\n".format(day))
    with open(f"{day_folder}/input.txt", "w") as f:
        f.write("# Paste puzzle input here\n")
    with open(f"{day_folder}/mock_input.txt", "w") as f:
        f.write("# Paste mock puzzle input here\n")
    print(f"Created {day_folder} structure.")


if __name__ == "__main__":
    day = int(input("Enter the day number: "))
    create_day_folder(day)

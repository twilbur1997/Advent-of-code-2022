import os


def day_05_challenge_part_1():
    # After the rearrangement procedure completes, what crate ends up on top of each stack?
    input_file = "input_05_day.txt"


    with open(input_file, "r") as file:
        prev_lines = []
        line = int(file.readline().strip())

        while line:
            prev_lines.append(line)
            line = int(file.readline().strip())

    return 0


def day_05_challenge_part_2():
    input_file = "input_05_day.txt"

    with open(input_file, "r") as file:
        prev_lines = []
        line = int(file.readline().strip())

        while line:
            prev_lines.append(line)
            line = int(file.readline().strip())

    return 0


def main():
    print(day_05_challenge_part_1())
    print(day_05_challenge_part_2())


if __name__ == "__main__":
    main()

import os


def day_01_challenge_part_1():
    # Find the Elf carrying the most Calories.
    # How many total Calories is that Elf carrying?

    input_file = "input_01_day.txt"

    with open(input_file, "r") as file:
        prev_lines = []
        most_cals = 0
        line = file.readline()

        while line:
            if line=="" or line=="\n":
                total_cals = sum(prev_lines)
                if total_cals > most_cals:
                    most_cals = total_cals
                prev_lines = []
            else:
                prev_lines.append(int(line))
            line = file.readline()

    return most_cals


def day_01_challenge_part_2():
    # Find the top three Elves carrying the most Calories.
    # How many Calories are those Elves carrying in total?

    input_file = "input_01_day.txt"

    with open(input_file, "r") as file:
        prev_lines = []
        most_cals = [0,0,0]
        line = file.readline()

        while line:
            if line=="" or line=="\n":
                total_cals = sum(prev_lines)
                if total_cals > most_cals[0]:
                    most_cals[0] = total_cals
                    most_cals.sort()
                prev_lines = []
            else:
                prev_lines.append(int(line))
            line = file.readline()

    return sum(most_cals)


def main():
    # print(day_01_challenge_part_1())
    print(day_01_challenge_part_2())


if __name__ == "__main__":
    main()

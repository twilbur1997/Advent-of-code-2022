import os


def convert_to_priority(character):
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.

    # >>> ord("a")
    # 97
    # >>> ord("A")
    # 65

    if character.islower():
        return ord(character)-96
    return ord(character)-38


def day_03_challenge_part_1():
    # Find the item type that appears in both compartments of each rucksack.
    # What is the sum of the priorities of those item types?

    input_file = "input_03_day.txt"
    total = 0

    with open(input_file, "r") as file:
        line = file.readline().strip()

        while line:
            middle = len(line)/2
            first_h = line[:middle]
            second_h = line[middle:]

            total += convert_to_priority(shared_letter)
            line = file.readline().strip()

    return 0


def day_03_challenge_part_2():
    input_file = "input_03_day.txt"

    with open(input_file, "r") as file:
        prev_lines = []
        line = file.readline().strip()

        while line:
            prev_lines.append(line)
            line = file.readline().strip()

    return 0


def main():
    print(day_03_challenge_part_1())
    print(day_03_challenge_part_2())


if __name__ == "__main__":
    main()

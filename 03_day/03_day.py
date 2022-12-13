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
            middle = len(line)//2
            first_h = line[:middle]
            second_h = line[middle:]
            for letter in first_h:
                if letter in second_h:
                    total += convert_to_priority(letter)
                    break

            line = file.readline().strip()

    return total


def day_03_challenge_part_2():
    # Find the item type that corresponds to the badges of each three-Elf group.
    # What is the sum of the priorities of those item types?
    input_file = "input_03_day.txt"
    total = 0

    with open(input_file, "r") as file:
        prev_lines = []
        line = file.readline().strip()

        while line:
            prev_lines.append(line)
            if len(prev_lines)==3:
                for elf1_letter in prev_lines[0]:
                    if elf1_letter in prev_lines[1] and elf1_letter in prev_lines[2]:
                        total += convert_to_priority(elf1_letter)
                        prev_lines = []
                        break

            line = file.readline().strip()

    return total


def main():
    print(day_03_challenge_part_1())
    print(day_03_challenge_part_2())


if __name__ == "__main__":
    main()

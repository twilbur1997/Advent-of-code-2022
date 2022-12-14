import os


def day_04_challenge_part_1():
    # In how many assignment pairs does one range fully contain the other?
    input_file = "input_04_day.txt"

    with open(input_file, "r") as file:
        line = file.readline().strip()
        total = 0

        while line:
            first_elf, second_elf = line.split(",")
            elf1_start = int(first_elf.split("-")[0])
            elf1_end = int(first_elf.split("-")[1])
            elf2_start = int(second_elf.split("-")[0])
            elf2_end = int(second_elf.split("-")[1])

            if elf1_start <= elf2_start and elf1_end >= elf2_end: # ex. 2-5 and 3-4
                total +=1
                line = file.readline().strip()
                continue

            if elf1_start >= elf2_start and elf1_end <= elf2_end: # ex. 5-6 and 4-8
                total +=1
                line = file.readline().strip()
                continue

            line = file.readline().strip()

    return total


def day_04_challenge_part_2():
    input_file = "input_04_day.txt"

    with open(input_file, "r") as file:
        line = file.readline().strip()
        total = 0

        while line:
            first_elf, second_elf = line.split(",")
            elf1_start = int(first_elf.split("-")[0])
            elf1_end = int(first_elf.split("-")[1])
            elf2_start = int(second_elf.split("-")[0])
            elf2_end = int(second_elf.split("-")[1])

            if elf1_start >= elf2_start and elf1_start <= elf2_end:
                total +=1
                line = file.readline().strip()
                continue

            if elf1_end >= elf2_start and elf1_end <= elf2_end:
                total +=1
                line = file.readline().strip()
                continue

            if elf2_start >= elf1_start and elf2_start <= elf1_end:
                total +=1
                line = file.readline().strip()
                continue

            if elf2_end >= elf1_start and elf2_end <= elf1_end:
                total +=1
                line = file.readline().strip()
                continue

            line = file.readline().strip()

    return total


def main():
    print(day_04_challenge_part_1())
    print(day_04_challenge_part_2())


if __name__ == "__main__":
    main()

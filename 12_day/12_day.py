import os


def day_12_challenge_part_1():
    input_file = "input_12_day.txt"

    with open(input_file, "r") as file:
        prev_lines = []
        line = int(file.readline().strip())

        while line:
            prev_lines.append(line)
            line = int(file.readline().strip())

    return 0
    

def day_12_challenge_part_2():
    input_file = "input_12_day.txt"

    with open(input_file, "r") as file:
        prev_lines = []
        line = int(file.readline().strip())

        while line:
            prev_lines.append(line)
            line = int(file.readline().strip())

    return 0


def main():
    print(day_12_challenge_part_1())
    print(day_12_challenge_part_2())
    

if __name__ == "__main__":
    main()


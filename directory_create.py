import os
import subprocess


def python_create(python_path, num):

    python_string = 'import os\n\n\ndef day_'+num+'_challenge_part_1():\n\
    input_file = "input_'+num+'_day.txt"\n\n\
    with open(input_file, "r") as file:\n\
        prev_lines = []\n\
        line = int(file.readline().strip())\n\n\
        while line:\n\
            prev_lines.append(line)\n\
            line = int(file.readline().strip())\n\n\
    return 0\n\
    \n\n\
def day_'+num+'_challenge_part_2():\n\
    input_file = "input_'+num+'_day.txt"\n\n\
    with open(input_file, "r") as file:\n\
        prev_lines = []\n\
        line = int(file.readline().strip())\n\n\
        while line:\n\
            prev_lines.append(line)\n\
            line = int(file.readline().strip())\n\n\
    return 0\n\n\n\
def main():\n\
    print(day_'+num+'_challenge_part_1())\n\
    print(day_'+num+'_challenge_part_2())\n\
    \n\n\
if __name__ == "__main__":\n\
    main()\n\n'

    print(python_string)

    with open(python_path, "w") as file:
        file.write(python_string)

    return


def create_directories(directory, python_file, input_file, num):
    cwd_dir = os.getcwd()
    print(cwd_dir)

    directory_path = os.path.join(cwd_dir, directory)
    os.mkdir(directory_path)

    python_path = os.path.join(directory_path, python_file)
    input_path = os.path.join(directory_path, input_file)

    python_create(python_path, num)
    with open(input_path, "w") as file:
        file.write("\n")

    print("Directory '% s' created" % directory)
    return


def delete_dirs(x, directory):
    command = 'rm -r '+x+directory
    if os.path.exists(x+directory):
        subprocess.run(command, shell=True)


def loop_through_directories():
    directory = "_day"
    python_file = "_day.py"
    input_file = "_day.txt"

    for x in range(1,26):
        if x < 10:
            x = "0"+str(x)
        else:
            x = str(x)
        create_directories(x+directory, x+python_file, "input_"+x+input_file, x)

        # delete_dirs(x, directory) # Uncomment this line to delete all directories recursively


def main():
    # Uncomment this to create all directories
    # loop_through_directories()

    print("Uncomment line in program to do anything")


if __name__ == "__main__":
    main()

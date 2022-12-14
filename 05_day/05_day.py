import os

stack0 = ''
stack1 = 'WRTG'
stack2 = 'WVSMPHCG'
stack3 = 'MGSTLC'
stack4 = 'FRWMDHJ'
stack5 = 'JFWSHLQP'
stack6 = 'SMFNDJP'
stack7 = 'JSCGFDBZ'
stack8 = 'BTR'
stack9 = 'CLWNH'

all_stacks = [stack0,stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]


def move_num_from_a_to_b(num, a, b):
    for x in range(num):
        '''
        print(all_stacks[a][0])
        print(all_stacks[a])
        print(all_stacks[b], '\n')
        '''
        all_stacks[b] = all_stacks[a][0]+all_stacks[b]
        all_stacks[a] = all_stacks[a][1:]
        '''
        print(all_stacks[a])
        print(all_stacks[b],'\n')
        '''


def day_05_challenge_part_1():
    # After the rearrangement procedure completes, what crate ends up on top of each stack?
    input_file = "input_05_day.txt"


    with open(input_file, "r") as file:
        line = file.readline().strip()

        while "move" not in line:
            line = file.readline().strip()

        while line:
            # move 3 from 4 to 3
            split_line = line.split(' ')
            num_moved = int(split_line[1])
            from_pile = int(split_line[3])
            to_pile = int(split_line[5])
            move_num_from_a_to_b(num_moved, from_pile, to_pile)

            line = file.readline().strip()

    top_of_stacks = ''
    for item in all_stacks[1:]:
        top_of_stacks = top_of_stacks+item[0]

    return top_of_stacks


def move_num_from_a_to_b_multiple(num, a, b):
    print(all_stacks[a][0:num])
    print(all_stacks[a])
    print(all_stacks[b], '\n')

    all_stacks[b] = all_stacks[a][0:num]+all_stacks[b]
    all_stacks[a] = all_stacks[a][num:]

    print(all_stacks[a])
    print(all_stacks[b],'\n')


def day_05_challenge_part_2():
    input_file = "input_05_day.txt"

    with open(input_file, "r") as file:
        line = file.readline().strip()

        while "move" not in line:
            line = file.readline().strip()

        while line:
            # move 3 from 4 to 3
            split_line = line.split(' ')
            num_moved = int(split_line[1])
            from_pile = int(split_line[3])
            to_pile = int(split_line[5])
            move_num_from_a_to_b_multiple(num_moved, from_pile, to_pile)

            line = file.readline().strip()


    top_of_stacks = ''
    for item in all_stacks[1:]:
        top_of_stacks = top_of_stacks+item[0]

    return top_of_stacks


def main():
    '''
    for item in all_stacks:
        print(item)
    return
    '''
    # print(day_05_challenge_part_1())
    print(day_05_challenge_part_2())


if __name__ == "__main__":
    main()

import os


def day_02_challenge_part_1():
    # The score for a single round is the score for the shape you selected
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # plus the score for the outcome of the round
    # 0 if you lost, 3 if the round was a draw, and 6 if you won.
    # Rock (A, X), Paper(B, Y), Scissors (C, Z)
    input_file = "input_02_day.txt"

    opp_shape_dict = {"A":1, "B":2, "C":3}
    shape_dict = {"X":1, "Y":2, "Z":3}
    outcome_dict = {-2:0, -1:6, 0:3, 1:0, 2:6} # opp minus response
    # -2 = Rock wins to Scissors (Opp wins, 0 points)
    # -1 = Rock loses to Paper, Paper loses to Scissors (Opp loses, 6 points)
    # 0 = Tie (3 points, draw)
    # +1 = Paper wins to Rock, Scissors wins to Paper (Opp wins, 0 points)
    # +2 = Scissors loses to Rock (Opp loses, 6 points)


    with open(input_file, "r") as file:
        line = file.readline().strip()
        total = 0
        while line:
            opponent, response = line.split(" ")
            shape_score = shape_dict[response]
            opp_shape_score = opp_shape_dict[opponent]
            win_points = outcome_dict[opp_shape_score-shape_score]
            round_points = win_points+shape_score
            total+=round_points

            line = file.readline().strip()

    return total


def day_02_challenge_part_2():
    input_file = "input_02_day.txt"

    opp_shape_dict = {"A":1, "B":2, "C":3}
    shape_dict = {"X":1, "Y":2, "Z":3}
    my_shape_list = [3,1,2,3,1]

    outcome_dict = {1:0, 2:3, 3:6}
    # lose, tie, win

    with open(input_file, "r") as file:
        line = file.readline().strip()
        total = 0
        while line:
            opponent, response = line.split(" ")
            shape_score = shape_dict[response]
            opp_shape_score = opp_shape_dict[opponent]
            my_shape = opp_shape_score+(shape_score-2)
            final_shape = my_shape_list[my_shape] # converts 0 to 3 and 4 to 1

            win_points = outcome_dict[shape_score]
            round_points = win_points+final_shape
            total+=round_points

            line = file.readline().strip()

    return total


def main():
    print(day_02_challenge_part_1())
    print(day_02_challenge_part_2())


if __name__ == "__main__":
    main()

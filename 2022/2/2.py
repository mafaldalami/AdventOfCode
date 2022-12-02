shape_points = {"X": 1, "Y": 2, "Z": 3}

wins = [("A", "Y"), ("B", "Z"), ("C", "X")]

ties = [("A", "X"), ("B", "Y"), ("C", "Z")]

loose = {"A": "Z", "B": "X", "C": "Y"}
draw = {"A": "X", "B": "Y", "C": "Z"}
win = {"A": "Y", "B": "Z", "C": "X"}


def part_one(plays: list):
    total_points = 0
    for round in plays:
        play = round.split(" ")
        total_points += shape_points[play[1]]
        if tuple(play) in wins:
            total_points += 6
        if tuple(play) in ties:
            total_points += 3
    return total_points


# X -> lose; Y -> draw; Z -> win
def part_two(plays: list):
    total_points = 0
    for round in plays:
        play = round.split(" ")
        if play[1] == "X":
            total_points += shape_points[loose[play[0]]]
        if play[1] == "Y":
            total_points += shape_points[draw[play[0]]] + 3
        if play[1] == "Z":
            total_points += shape_points[win[play[0]]] + 6
    return total_points


def main():
    input_path = "input.txt"
    file = open(input_path)
    plays = file.read().split("\n")
    print("---Part One---")
    print(part_one(plays))

    print("---Part Two---")
    print(part_two(plays))


if __name__ == "__main__":
    main()

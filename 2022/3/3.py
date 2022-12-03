def cal_letter_value(letter: str) -> int:
    val = 0
    if letter.islower():
        val += ord(letter) % 64 - 32
    else:
        val += ord(letter) % 64 + 26
    return val


def part_one(runsacks: list):
    sum_priorities = 0
    for runsack in runsacks:
        split = int(len(runsack)/2)
        compartment1 = runsack[:split]
        compartment2 = runsack[split:]
        shared_items = set(compartment1).intersection(compartment2)
        for char in shared_items:
            val = cal_letter_value(char)
            sum_priorities += val
    return sum_priorities


def part_two(runsacks: list):
    sum_priorities = 0
    groups = [runsacks[i:i+3] for i in range(0, len(runsacks), 3)]
    for group in groups:
        g1 = group[0]
        g2 = group[1]
        g3 = group[2]
        shared_items = set(g1).intersection(set(g2).intersection(g3))
        for char in shared_items:
            val = cal_letter_value(char)
            sum_priorities += val
    return sum_priorities


def main():
    input_path = "input.txt"
    file = open(input_path)
    runsacks = file.read().split("\n")
    print("---Part One---")
    print(part_one(runsacks))

    print("---Part Two---")
    print(part_two(runsacks))


if __name__ == "__main__":
    main()
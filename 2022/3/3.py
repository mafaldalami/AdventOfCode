def part_one(runsacks: list):
    sum_priorities = 0
    for runsack in runsacks:
        split = int(len(runsack)/2)
        compartment1 = runsack[:split]
        compartment2 = runsack[split:]
        shared_items = set(compartment1).intersection(compartment2)
        for char in shared_items:
            val = +ord(char) % 64
            if char.islower():
                sum_priorities += val - 32
            else:
                sum_priorities += val + 26
    return sum_priorities


def part_two(plays: list):
    pass


def main():
    input_path = "input.txt"
    file = open(input_path)
    runsacks = file.read().split("\n")
    print("---Part One---")
    print(part_one(runsacks))

    print("---Part Two---")
    # print(part_two(plays))


if __name__ == "__main__":
    main()
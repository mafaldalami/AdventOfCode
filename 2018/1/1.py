def part_one(changes: list):
    frequency = 0
    for change in changes:
        frequency += int(change)
    return frequency

def part_two(changes: list):
    frequency = 0
    seen = {frequency}
    while True:
        for change in changes:
            frequency += int(change)
            # if value was already seen it is the seen set, else it is added to the seen set
            if frequency in seen:
                return frequency
            seen.add(frequency)


def main():
    input_path = "input.txt"
    file = open(input_path)
    changes = file.read().split("\n")
    print("---Part One---")
    print(part_one(changes))

    print("---Part Two---")
    print(part_two(changes))


if __name__ == "__main__":
    main()
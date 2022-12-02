def calculate_cals(elves: list) -> list:
    elves_cals = []
    max = -1
    for elf in elves:
        cals = 0
        for cal in elf.split("\n"):
            cals += int(cal)
        elves_cals.append(cals)
    return elves_cals


def main():
    input_path = "input.txt"
    file = open(input_path)
    elves = file.read().split("\n\n")
    elves_cals = sorted(calculate_cals(elves), reverse=True)
    print(elves_cals)
    print("---Part One---")
    print(elves_cals[0])

    print("---Part Two---")
    print(elves_cals[0] + elves_cals[1] + elves_cals[2])


if __name__ == "__main__":
    main()

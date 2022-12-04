def containing_pair(elf1: list, elf2: list) -> bool:
    if int(elf1[0]) <= int(elf2[0]) and int(elf2[1]) <= int(elf1[1]):
        return True
    elif int(elf2[0]) <= int(elf1[0]) and int(elf1[1]) <= int(elf2[1]):
        return True
    return False


def overlapping_pair(elf1: list, elf2: list) -> bool:
    if int(elf1[0]) <= int(elf2[0]) and int(elf2[0]) <= int(elf1[1]):
        return True
    elif int(elf2[0]) <= int(elf1[0]) and int(elf1[0]) <= int(elf2[1]):
        return True
    return False


def part_one(pairs: list) -> int:
    total_overlap = 0
    for pair in pairs:
        assignments = pair.split(",")
        elf1 = assignments[0].split("-")
        elf2 = assignments[1].split("-")
        if containing_pair(elf1, elf2):
            total_overlap += 1
    return total_overlap


def part_two(pairs: list):
    overlap = 0
    for pair in pairs:
        assignments = pair.split(",")
        elf1 = assignments[0].split("-")
        elf2 = assignments[1].split("-")
        if overlapping_pair(elf1, elf2):
            overlap += 1
    return overlap


def main():
    input_path = "input.txt"
    file = open(input_path)
    pairs = file.read().split("\n")
    print("---Part One---")
    print(part_one(pairs))

    print("---Part Two---")
    print(part_two(pairs))


if __name__ == "__main__":
    main()

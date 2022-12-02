from collections import Counter


def part_one(box_ids: list):
    two_rep = 0
    three_rep = 0
    for box_id in box_ids:
        count = Counter(box_id).values()
        if 2 in count:
            two_rep += 1
        if 3 in count:
            three_rep += 1
    return two_rep * three_rep


def part_two(box_ids: list):
    final_string = ""
    for i, box_id1 in enumerate(box_ids):
        for box_id2 in box_ids[i+1:]:
            different = 0
            for l1, l2 in zip(box_id1, box_id2):
                if l1 != l2:
                    different += 1
                    if different > 1:
                        break
            if different == 1:
                for l1, l2 in zip(box_id1.strip(), box_id2.strip()):
                    if l1 == l2:
                        final_string = "".join((final_string, l1))
    return final_string


def main():
    input_path = "input.txt"
    file = open(input_path)
    box_ids = file.read().split("\n")
    print("---Part One---")
    print(part_one(box_ids))

    print("---Part Two---")
    print(part_two(box_ids))


if __name__ == "__main__":
    main()

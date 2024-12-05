from aocd import get_data

dummy_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
dummy_data_part_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
dummy_data_newline = """xmul(8,5)&mul[3,7]!^don't()don't()do()don't()
_mul(500,15)don't()+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


def process_data(data: str) -> str:
    return data


def part_1(data: str) -> int:
    data_split = data.split("mul(")
    ret = 0
    for x in data_split:
        x = x.split(")")
        for parts in x:
            potential = parts.split(",")
            if len(potential) == 2:
                if (1 <= len(potential[0]) <= 3) and (1 <= len(potential[1]) <= 3):
                    try:
                        ret += int(potential[0]) * int(potential[1])
                    except ValueError:
                        continue
    return ret


def part_2(data: str) -> int:
    ret = 0

    cursor = 0
    while True:
        do_idx = data.find("do()", cursor)
        dont_idx = data.find("don't()", cursor)

        part = data[cursor:dont_idx]
        ret += part_1(part)

        # if dont_idx > do_idx:
        #     ret += part_1(data[do_idx:dont_idx])

        cursor = do_idx + 4

        if dont_idx == -1:
            break

    return ret


if __name__ == "__main__":
    data = process_data(get_data(day=3, year=2024))
    # data = process_data(dummy_data)
    # data = process_data(dummy_data_part_2)
    # data = process_data(dummy_data_newline)
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")

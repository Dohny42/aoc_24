from collections import Counter

from aocd import get_data


def process_data(data: str) -> tuple[list[int], list[int]]:
    # split the data into two columns
    left_col, right_col = [], []
    for line in data.splitlines():
        left, right = line.split()
        left_col.append(int(left.strip()))
        right_col.append(int(right.strip()))
    return left_col, right_col


def part_1(data: tuple[list[int], list[int]]) -> int:
    left_col, right_col = data
    # sort both columns
    left_col.sort()
    right_col.sort()

    # sum up distances between items
    ret = 0
    for l_item, r_item in zip(left_col, right_col):
        ret += abs(l_item - r_item)

    return ret


def part_2(data: tuple[list[int], list[int]]):
    left_col, right_col = data
    # count each number in right column
    right_col_counter = Counter(right_col)

    # sum up each item from left * right count
    ret = 0
    for l_item in left_col:
        ret += l_item * right_col_counter[l_item]

    return ret


if __name__ == "__main__":
    data = process_data(get_data(day=1, year=2024))
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")

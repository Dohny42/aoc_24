import itertools

from aocd import get_data

dummy_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def process_data(data: str) -> list[str]:
    return data.splitlines()


op_map = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, "||": lambda x, y: int(f"{x}{y}")}


def part_1(data: list[str]) -> int:
    ret = 0
    for line in data:
        line_split = line.split(": ")
        val = int(line_split[0])
        nums = list(map(int, line_split[1].split()))

        # generate all possible combinations of operators (+, *)
        op_combs = itertools.product(["+", "*"], repeat=len(nums) - 1)
        # apply each combination of operators to the numbers and check if the result is equal to the target value
        for op_comb in op_combs:
            cur_val = nums[0]
            for i in range(len(op_comb)):
                cur_val = op_map[op_comb[i]](cur_val, nums[i + 1])
                if cur_val > val or cur_val == val:
                    break
            if cur_val == val:
                ret += val
                break
    return ret


def part_2(data: list[str]) -> int:
    ret = 0
    for line in data:
        line_split = line.split(": ")
        val = int(line_split[0])
        nums = list(map(int, (line_split[1].split())))

        # generate all possible combinations of operators (+, *, ||)
        op_combs = itertools.product(["+", "*", "||"], repeat=len(nums) - 1)
        # apply each combination of operators to the numbers and check if the result is equal to the target value
        for op_comb in op_combs:
            cur_val = int(nums[0])
            for i in range(len(op_comb)):
                cur_val = op_map[op_comb[i]](cur_val, nums[i + 1])
                if cur_val > val or cur_val == val:
                    break
            if cur_val == val:
                ret += val
                break
    return ret


if __name__ == "__main__":
    data = process_data(get_data(day=7, year=2024))
    # data = process_data(dummy_data)
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")

from aocd import get_data

dummy_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def process_data(data: str) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in data.splitlines()]


def part_1(data: list[list[int]]) -> int:
    ret = 0
    for report in data:
        safe = True
        # check for monotonicity
        should_inc = report[0] - report[1] < 0
        should_dec = report[0] - report[1] > 0

        for i in range(len(report) - 1):
            dist = report[i] - report[i + 1]
            # safe checks
            if should_inc and dist <= -1 and dist >= -3:
                continue
            if should_dec and dist >= 1 and dist <= 3:
                continue
            else:
                safe = False
                break
        if safe:
            ret += 1
    return ret


def part_2(data: list[list[int]]) -> int:
    ret = 0
    for report in data:
        safe = True
        # check for monotonicity
        should_inc = report[1] - report[0] > 0
        should_dec = report[1] - report[0] < 0
        for i in range(1, len(report) - 1):
            dist = report[i - 1] - report[i]
            # safe checks
            if should_inc and dist <= -1 and dist >= -3:
                continue
            if should_dec and dist >= 1 and dist <= 3:
                continue
            else:
                del report[i - 1]
                i -= 1
                for j in range(i, len(report)):
                    # since we removed, we should recalculate
                    dist = report[j - 1] - report[j]
                    # safe checks
                    if should_inc and dist <= -1 and dist >= -3:
                        continue
                    if should_dec and dist >= 1 and dist <= 3:
                        continue
                    else:
                        safe = False
                        break
                if not safe:
                    break
        if safe:
            ret += 1
    return ret


if __name__ == "__main__":
    data = process_data(get_data(day=2, year=2024))
    # data = process_data(dummy_data)
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")

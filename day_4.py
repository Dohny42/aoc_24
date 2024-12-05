from aocd import get_data

dummy_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def process_data(data: str) -> list[list[str]]:
    return [list(x) for x in data.split("\n")]


def part_1(data: list[list[str]]) -> int:
    ret = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            # if we can look left
            if j >= 3:
                potential = "".join([data[i][j - x] for x in range(4)])
                if potential == "XMAS":
                    ret += 1
                    print(f"Found 'XMAS' left at ({i}, {j})")
            # diagonally up left
            if i >= 3 and j >= 3:
                potential = "".join([data[i - x][j - x] for x in range(4)])
                if potential == "XMAS":
                    ret += 1
                    print(f"Found 'XMAS' diagonally up left at ({i}, {j})")
            # up
            if i >= 3:
                potential = "".join([data[i - x][j] for x in range(4)])
                if potential == "XMAS":
                    ret += 1
                    print(f"Found 'XMAS' up at ({i}, {j})")
            # diagonally up right
            if i >= 3 and j <= len(data[i]) - 4:
                potential = "".join([data[i - x][j + x] for x in range(4)])
                if potential == "XMAS":
                    ret += 1
                    print(f"Found 'XMAS' diagonally up right at ({i}, {j})")
            # right
            if j <= len(data[i]) - 4:
                potential = "".join(data[i][j : j + 4])
                if potential == "XMAS":
                    ret += 1
                    print(f"Found 'XMAS' right at ({i}, {j})")
            # diagonally down right
            if i <= len(data) - 4 and j <= len(data[i]) - 4:
                potential = "".join([data[i + x][j + x] for x in range(4)])
                if potential == "XMAS":
                    ret += 1
                    print(f"Found 'XMAS' diagonally down right at ({i}, {j})")
            # down
            if i <= len(data) - 4:
                potential = "".join([data[i + x][j] for x in range(4)])
                if potential == "XMAS":
                    ret += 1
                    print(f"Found 'XMAS' down at ({i}, {j})")
            # diagonally down left
            if i <= len(data) - 4 and j >= 3:
                potential = "".join([data[i + x][j - x] for x in range(4)])
                if potential == "XMAS":
                    ret += 1
                    print(f"Found 'XMAS' diagonally down left at ({i}, {j})")
    return ret


def part_2(data: list[list[str]]) -> int:
    ret = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            if data[i][j] == "A":
                potential_first_diag_mas = "".join(
                    [data[i - 1][j - 1], data[i][j], data[i + 1][j + 1]]
                )
                potential_second_diag_mas = "".join(
                    [data[i - 1][j + 1], data[i][j], data[i + 1][j - 1]]
                )
                if potential_first_diag_mas in ("SAM", "MAS") and potential_second_diag_mas in (
                    "SAM",
                    "MAS",
                ):
                    ret += 1
                    print(f"Found 'MAS' at ({i}, {j})")
    return ret


if __name__ == "__main__":
    data = process_data(get_data(day=4, year=2024))
    # data = process_data(dummy_data)
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")

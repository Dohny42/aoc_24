from aocd import get_data

dummy_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def process_data(data: str) -> list[list[str]]:
    return [list(x) for x in data.splitlines()]


def part_1(data: list[list[str]]) -> int:
    # determine the starting position of guard (^)
    ret = 0
    visited = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "^":
                facing_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                idx = 0
                while True:
                    visited.add((i, j))
                    i += facing_dirs[idx][0]
                    j += facing_dirs[idx][1]
                    # out of bounds
                    if (
                        i + facing_dirs[idx][0] < 0
                        or i + facing_dirs[idx][0] >= len(data)
                        or j + facing_dirs[idx][1] < 0
                        or j + facing_dirs[idx][1] >= len(data[i])
                    ):
                        break
                    if data[i + facing_dirs[idx][0]][j + facing_dirs[idx][1]] == "#":
                        idx = (idx + 1) % 4
                break
    ret = len(visited) + 1
    return ret


def part_2(data: ...) -> ...:
    pass


if __name__ == "__main__":
    data = process_data(get_data(day=6, year=2024))
    # data = process_data(dummy_data)
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")

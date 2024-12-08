from pprint import pprint

from aocd import get_data

dummy_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

dummy_data_own = """.....
.x...
x.x...
x....
....."""


def parse_for_ant_chars(data: str) -> set[str]:
    ret = set(data)
    ret.remove("\n")
    ret.remove(".")
    return ret


def process_data(data: str) -> str:
    return data


def part_1(data: str) -> int:
    ant_chars = parse_for_ant_chars(data)
    grid = [list(line) for line in data.splitlines()]
    ret = 0
    visited = set()
    while ant_chars:
        ant_char = ant_chars.pop()
        ant_char_pos = [
            (i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == ant_char
        ]
        # for each possible combination of ant_char_pos
        for i in range(len(ant_char_pos)):
            x1, y1 = ant_char_pos[i]
            for j in range(i, len(ant_char_pos)):
                if i == j:
                    continue
                x2, y2 = ant_char_pos[j]
                # rel to current
                rel_x1 = x1 - x2
                rel_y1 = y1 - y2
                # rel to other
                rel_x2 = x2 - x1
                rel_y2 = y2 - y1

                anti_1 = x1 + rel_x1, y1 + rel_y1
                anti_2 = x2 + rel_x2, y2 + rel_y2
                if (
                    anti_1[0] >= 0
                    and anti_1[1] >= 0
                    and anti_1[0] < len(grid)
                    and anti_1[1] < len(grid[0])
                ):
                    print(anti_1)
                    visited.add(anti_1)
                if (
                    anti_2[0] >= 0
                    and anti_2[1] >= 0
                    and anti_2[0] < len(grid)
                    and anti_2[1] < len(grid[0])
                ):
                    print(anti_2)
                    visited.add(anti_2)
    pprint(grid)
    ret = len(visited)
    return ret


def part_2(data: str) -> int:
    ant_chars = parse_for_ant_chars(data)
    grid = [list(line) for line in data.splitlines()]
    ret = 0
    visited = set()
    while ant_chars:
        ant_char = ant_chars.pop()
        ant_char_pos = [
            (i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == ant_char
        ]
        # for each possible combination of ant_char_pos
        for i in range(len(ant_char_pos)):
            x1, y1 = ant_char_pos[i]
            for j in range(i, len(ant_char_pos)):
                if i == j:
                    continue
                x2, y2 = ant_char_pos[j]

                visited.add((x1, y1))
                visited.add((x2, y2))

                # rel to current
                rel_x1 = x1 - x2
                rel_y1 = y1 - y2
                # rel to other
                rel_x2 = x2 - x1
                rel_y2 = y2 - y1

                k = 1
                while True:
                    anti_1 = x1 + (k * rel_x1), y1 + (k * rel_y1)
                    anti_2 = x2 + (k * rel_x2), y2 + (k * rel_y2)
                    k += 1
                    anti_1_in_grid = (
                        anti_1[0] >= 0
                        and anti_1[1] >= 0
                        and anti_1[0] < len(grid)
                        and anti_1[1] < len(grid[0])
                    )
                    print(anti_1_in_grid)
                    anti_2_in_grid = (
                        anti_2[0] >= 0
                        and anti_2[1] >= 0
                        and anti_2[0] < len(grid)
                        and anti_2[1] < len(grid[0])
                    )
                    if anti_1_in_grid:
                        visited.add(anti_1)
                    if anti_2_in_grid:
                        visited.add(anti_2)
                    if not anti_1_in_grid and not anti_2_in_grid:
                        break
    ret = len(visited)
    return ret


if __name__ == "__main__":
    data = process_data(get_data(day=8, year=2024))
    # data = process_data(dummy_data)
    # data = process_data(dummy_data_own)
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")

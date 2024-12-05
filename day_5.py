from collections import defaultdict

from aocd import get_data

dummy_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def process_data(data: str) -> tuple[list[str], list[str]]:
    data_split = data.split("\n\n")
    return data_split[0].splitlines(), data_split[1].splitlines()


def part_1(data: tuple[list[str], list[str]]) -> int:
    update_rules_raw, updates_raw = data
    # construct the update dictionary
    update_rules_dict = defaultdict(set)
    for rule in update_rules_raw:
        rule_split = rule.split("|")
        update_rules_dict[rule_split[0]].add(rule_split[1])

    ret = 0
    for update in updates_raw:
        update_split = update.split(",")
        correct = True
        for i in range(len(update_split)):
            # check from ith element to the end
            for j in range(i + 1, len(update_split)):
                if update_split[j] not in update_rules_dict[update_split[i]]:
                    correct = False
                    break
            if not correct:
                break
            # check until ith element
            for j in range(i):
                if update_split[i] not in update_rules_dict[update_split[j]]:
                    correct = False
                    break
            if not correct:
                break
        if correct:
            # int middle value of the update split
            ret += int(update_split[len(update_split) // 2])
    return ret


def part_2(data: tuple[list[str], list[str]]) -> int:
    update_rules_raw, updates_raw = data
    # construct the update dictionary
    update_rules_dict = defaultdict(set)
    for rule in update_rules_raw:
        rule_split = rule.split("|")
        update_rules_dict[rule_split[0]].add(rule_split[1])
    print(update_rules_dict)
    ret = 0
    for update in updates_raw:
        update_split = update.split(",")
        correct = True
        for i in range(len(update_split)):
            # check from ith element to the end
            for j in range(i + 1, len(update_split)):
                if update_split[j] not in update_rules_dict[update_split[i]]:
                    temp = update_split[i]
                    update_split[i] = update_split[j]
                    update_split[j] = temp
                    correct = False
            # check until ith element
            for j in range(i):
                if update_split[i] not in update_rules_dict[update_split[j]]:
                    temp = update_split[j]
                    update_split[j] = update_split[i]
                    update_split[i] = temp
                    correct = False
        if not correct:
            # int middle value of the update split
            ret += int(update_split[len(update_split) // 2])
    return ret


if __name__ == "__main__":
    data = process_data(get_data(day=5, year=2024))
    # data = process_data(dummy_data)
    print(f"part 1: {part_1(data)}")
    print(f"part 2: {part_2(data)}")

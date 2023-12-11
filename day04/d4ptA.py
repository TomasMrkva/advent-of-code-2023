def parse_line(line: str) -> list:
    left, right = line[line.index(':') + 2:].split('|')
    return [parse_nums(left), parse_nums(right)]

def parse_nums(nums: str) -> list:
    return set(map(int, nums.split()))

def compare(l: list[set]) -> int:
    left, right = l
    intersect_len = len(left.intersection(right))
    return 2 ** (intersect_len - 1) if intersect_len else 0

with open("input.txt", "r") as f:
    cards = f.read().splitlines()
    res = sum(map(compare, map(parse_line, cards)))
    print(res)
from collections import defaultdict

def parse_line(line: str) -> list:
    left, right = line[line.index(':') + 2:].split('|')
    return [parse_nums(left), parse_nums(right)]

def parse_nums(nums: str) -> list:
    return set(map(int, nums.split()))

def compare(l: list[set]) -> int:
    return len(l[0].intersection(l[1]))

def sol(cards: str, n: int, d: defaultdict) -> int:
    if n >= len(cards): return 0
    matches = compare(parse_line(cards[n]))
    for i in range(1, matches + 1):
        d[n + i] += d[n]
    return d[n] + sol(cards, n + 1, d)

with open("input.txt", "r") as f:
    cards = f.read().splitlines()
    d = defaultdict(lambda: 1)
    print(sol(cards, 0, d))
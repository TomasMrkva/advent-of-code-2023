import re

def parse_line(line: str) -> tuple[str]:
    return re.findall(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)[0]

def move_to_value(move: str) -> int:
    return 0 if move == 'L' else 1

def infinite_moves(moves: str):
    while True:
        yield from map(move_to_value, moves)

def get_next_move(generator):
    return next(generator)

def sol(lines: list[str]):
    d = {}
    for l in lines[2:]:
        s, l, r = parse_line(l)
        d[s] = (l, r)
    gen = infinite_moves(lines[0])
    curr = 'AAA'
    count = 0
    while curr != 'ZZZ':
        curr = d[curr][get_next_move(gen)]
        count += 1
    print(count)


with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    sol(lines)

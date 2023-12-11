import re
import math

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
    
    counts = []
    starting_positions = [pos for pos in d.keys() if pos.endswith('A')]
    for curr in starting_positions:
        count = 0
        gen = infinite_moves(lines[0])
        
        while not curr.endswith('Z'):
            curr = d[curr][get_next_move(gen)]
            count += 1
        counts.append(count)
    
    print(math.lcm(*counts))


with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    sol(lines)

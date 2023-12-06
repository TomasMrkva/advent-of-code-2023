from functools import reduce

def parse_seeds(s: str) -> list[int]:
    seed_vals = s[s.index(':') + 1:].strip()
    return list(map(int, seed_vals.split()))

def parse_map(s: str) -> dict:
    content = s[s.index(':') + 1:].strip().splitlines()
    parsed_arr = [map(int, row.split()) for row in content]
    m = {}
    for (d, s, r) in parsed_arr:
        m[(s, s+r-1)] = d - s
    return m

def find_next_source(num: int, m: dict) -> int:
    for (s, e), v in m.items():
        if num in range(s, e+1):
            return num + v
    return num

def traverse(ms: list[dict], num: int) -> int:
    return reduce(find_next_source, ms, num)

with open("input.txt", "r") as f:
    content = f.read().split("\n\n")
    seeds = parse_seeds(content[0])
    maps = list(map(parse_map, content[1:]))
    res = min([traverse(maps, s) for s in seeds])
    print(res)
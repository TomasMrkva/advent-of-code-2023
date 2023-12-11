f = open("input.txt", "r")
ls = f.read().splitlines()

gap = 1000000 - 1

def expand_rows(lines: list[str]) -> list[str]:
    for l in lines:
        if not '#' in l:
            yield from ('.' * len(lines[0]) for _ in range(gap))
        yield l

def expand_cols(lines: list[str]) -> list[str]:
    i = 0
    while i < len(lines[0]):
        if not '#' in [lines[x][i] for x in range(len(lines))]:
            lines = [lines[x][:i] + '.' * gap + lines[x][i:] for x in range(len(lines))]
            i += gap
        i += 1
    return lines

def get_stars_pos(lines: list[str]):
    for row, l in enumerate(lines):
        yield from ((row, col) for col, ch in enumerate(l) if ch == '#')
        
def get_all_combs(stars: list[tuple[int]]):
    for i, el in enumerate(stars):
        yield from [(el, x) for x in stars[:i] + stars[i+1:]]
        
def get_manhattan_diff(pair) -> int:
    x, y = pair
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

x = expand_cols(list(expand_rows(ls)))
sky = expand_cols(list(expand_rows(ls)))
combs = get_all_combs(list(get_stars_pos(sky)))
res = sum(list(map(get_manhattan_diff, combs))) // 2
print(res)
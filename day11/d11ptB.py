f = open("input.txt", "r")
ls = f.read().splitlines()

row_gaps = []
col_gaps = []
gap = 1000000

def expand_rows(lines: list[str]) -> list[str]:
    for i,l in enumerate(lines):
        if not '#' in l:
            row_gaps.append(i)
        yield l

def expand_cols(lines: list[str]) -> list[str]:
    for i in range(len(lines[0])):
        if not '#' in [lines[x][i] for x in range(len(lines))]:
            col_gaps.append(i)
    return lines

def get_stars_pos(lines: list[str]):
    for row, l in enumerate(lines):
        yield from ((row, col) for col, ch in enumerate(l) if ch == '#')
        
def get_all_combs(stars: list[tuple[int]]):
    for i, el in enumerate(stars):
        yield from [(el, x) for x in stars[:i] + stars[i+1:]]
        
def get_manhattan_diff(pair) -> int:
    a, b = pair
    mul_rows = 0
    mul_cols = 0
    
    for i in range(min(a[0], b[0]), max(a[0], b[0])):
        if i in row_gaps:
            mul_rows += 1

    for i in range(min(a[1], b[1]), max(a[1], b[1])):
        if i in col_gaps:
            mul_cols += 1
    
    return abs(a[0] - b[0]) - mul_rows + mul_rows * gap + abs(a[1] - b[1]) - mul_cols + mul_cols * gap

sky = expand_cols(list(expand_rows(ls)))
combs = get_all_combs(list(get_stars_pos(sky)))
res = sum(list(map(get_manhattan_diff, combs))) // 2

print(res)
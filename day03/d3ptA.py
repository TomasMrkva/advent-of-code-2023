import sys
sys.setrecursionlimit(20000)

def loop(grid, pos, found, acc, res):
    x, y = pos
    if x == len(grid): return res
    updated_res = res + [acc] if found and acc != "" else res
    if y == len(grid[0]): return loop(grid, (x + 1, 0), False, "", updated_res)
    curr = grid[x][y]
        
    if str.isdigit(curr):
        if found: return loop(grid, (x, y + 1), True, acc + curr, res)
        found_next = any((is_symbol(ch) for ch in get_neighbour_chars(grid, pos)))
        return loop(grid, (x, y + 1), found_next, acc + curr, res)
    
    return loop(grid, (x, y + 1), False, "", updated_res)

def is_symbol(ch):
    return not str.isdigit(ch) and ch != "."     

def get_neighbour_chars(grid, pos):
    return filter(lambda x: x != None, (check_pos(grid, x) for x in gen_available_pos(pos)))

def gen_available_pos(pos):
    x, y = pos
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)] 

def check_pos(grid, pos):
    x, y = pos
    if all((x >= 0, x < len(grid), y >= 0, y < len(grid[0]))):
        return grid[x][y]
    return None

with open("input.txt", "r") as f:
    grid = f.read().splitlines() 
    res = loop(grid, (0, 0), False, "", [])
    print(sum(map(int, res)))
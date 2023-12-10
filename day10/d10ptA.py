import math

f = open("input.txt", "r")
map = f.read().splitlines()

def get_start_cord() -> tuple:
    for i, line in enumerate(map):
        if 'S' in line:
            return (i, line.index('S'))
    raise Exception

def go_north(row, col):
    return (row - 1, col, 'N')

def go_south(row, col):
    return (row + 1, col, 'S')

def go_east(row, col):
    return (row, col + 1, 'E')

def go_west(row, col):
    return (row, col - 1, 'W')

def get_next(ch: str, prev: str, row: int, col: int) -> tuple:
    print(ch, prev) 
    match (ch, prev):
        case '-', 'W': return go_west(row, col)
        case '-', 'E': return go_east(row, col)
        
        case '|', 'S': return go_south(row, col)
        case '|', 'N': return go_north(row, col)
        
        case 'L', 'S': return go_east(row, col)
        case 'L', 'W': return go_north(row, col)
        
        case 'J', 'E': return go_north(row, col)
        case 'J', 'S': return go_west(row, col)
        
        case '7', 'N': return go_west(row, col)
        case '7', 'E': return go_south(row, col)
        
        case 'F', 'W': return go_south(row, col)
        case 'F', 'N': return go_east(row, col)
        
    raise Exception

def get_start_pipe(pos: tuple[int]):
    row, col = pos
    west = map[row][col-1] in '-FL'
    if west: return go_west(row, col)
    
    east = map[row][col+1] in '-J7'
    if east: return go_east(row, col)
        
    north = map[row-1][col] in '|F7'
    if north: return go_north(row, col)
    
    south = map[row+1][col] in '|JL'
    if south: return go_south(row, col)
    raise Exception
    

def get_total_path_count(row: int, col: int, prev: str) -> int:
    count = 0
    while map[row][col] != 'S':
        row, col, prev = get_next(map[row][col], prev, row, col)
        count += 1
    return count

start = get_start_pipe(get_start_cord())
res = get_total_path_count(*start)
print(math.ceil(res/2))
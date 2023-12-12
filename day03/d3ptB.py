def generate_num_dict(grid):
    d = {}
    for r_i, row in enumerate(grid):
        c_i = 0
        while c_i < len(row):
            if str.isdigit(row[c_i]):
                num = ""
                j = c_i
                while j < len(row) and str.isdigit(row[j]):
                    num += row[j]
                    j += 1
                for c_ii in range(c_i, j):
                    d[(r_i, c_ii)] = int(num)
                c_i += len(num)
            c_i += 1
    return d

def find_gears(grid, d):
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if row[j] == '*':
                num_pos = set(gen_available_pos((i, j)))
                nums = list(get_nums_from_pos(num_pos, d))
                if len(nums) == 2:
                    yield nums[0] * nums[1]

def get_nums_from_pos(num_pos, d):
    return set(filter(lambda x: x != None, [d[pos] if pos in d else None for pos in num_pos]))

def gen_available_pos(pos):
    x, y = pos
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)] 

with open("input.txt", "r") as f:
    grid = f.read().splitlines() 
    d = generate_num_dict(grid)
    print(sum(find_gears(grid, d)))
f = open("input.txt", "r")
ls = f.read().splitlines()

def parse_lines(lines: list[str]):
    for l in lines:
        left, right = l.split()
        right = list(map(int, right.split(',')))
        yield (left, right)
        
def generate(line: str) -> list[list[str]]:
    if line == '': return [[]]
    if line[0] == '?':
        left = list(map(lambda x: ['.'] + x,  generate(line[1:])))
        right = list(map(lambda x: ['#'] + x,  generate(line[1:])))
        return left + right
    return list(map(lambda x: [line[0]] + x,  generate(line[1:])))

def check(nums: list[int], row: list[str]):
    count = 0
    res = []
    for ch in row:
        match ch, count:
            case '.', 0: continue
            case '.', _:
                if count: 
                    res += [count]
                    count = 0
            case '#', _: count += 1
    if count != 0:
        res += [count]
    return res == nums
    
options = [(gen, nums) for row, nums in parse_lines(ls) for gen in generate(row)]
count = 0
for row, nums in options:
    count += check(nums, row)
print(count)
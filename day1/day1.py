def sol(x: str):
    lines = map(parse_words, x.splitlines())
    return sum(map(_sol, lines))

def _sol(x: str):
    digits = list(filter(str.isdigit, x))
    return int(digits[0]) * 10 + int(digits[-1])

valid = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
d = {valid[i-1]: str(i) for i in range(1, 10)}

def parse_words(x: str) -> str:
    if not x: return ""
    if x[0].isdigit(): return x[0] + parse_words(x[1:])
    if len(x) < 3: return parse_words(x[1:])
    
    ch3, ch4, ch5 = x[:3], x[:4], x[:5]
    if ch3 in d: return d[ch3] + parse_words(x[2:])
    if ch4 in d: return d[ch4] + parse_words(x[3:])
    if ch5 in d: return d[ch5] + parse_words(x[4:])
    return parse_words(x[1:])

with open('input.txt', 'r') as f:
    print(sol(f.read()))
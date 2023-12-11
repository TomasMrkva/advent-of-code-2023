import functools 
from parsy import *

digits = digit.at_least(1)
number = digits.concat().map(int)

# parser
@generate
def cubes() -> Parser:
    n = yield number
    yield whitespace
    c = yield (string('red') | string('green') | string('blue'))
    if c == "red": return (n, 0, 0)
    if c == "green": return (0, n, 0)
    return (0, 0, n)

fn = lambda x: functools.reduce(lambda a, b: tuple(map(sum, zip(a, b))), x, (0, 0, 0))
throw = cubes.sep_by(string(", "), min=1).map(fn)
throws = throw.sep_by(string("; "), min=1)

@generate
def game():
    yield string("Game ")
    n = yield number
    yield string(": ")
    ts = yield throws
    return (n, ts)

games = game.sep_by(string("\n"))

def is_valid_throw(throw):
    r, g, b = throw
    return r <= 12 and g <= 13 and b <= 14

def is_valid_game(game):
    return all(map(is_valid_throw,  game[1]))

with open("input.txt", "r") as f:
    parsed = games.parse(f.read())
    sol = sum(map(lambda x: x[0], filter(is_valid_game, parsed)))
    print(sol)
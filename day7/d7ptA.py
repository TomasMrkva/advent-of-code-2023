def parse(card: str):
    a, b = card.split()
    return (a, int(b))

def encode_card(card: str):
    order = '23456789TJQKA'
    return [order.index(ch) for ch in card]

def create_type(card: str):
    ordered_types = [
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1],
        [2, 2, 1],
        [3, 1, 1],
        [3, 2],
        [4, 1],
        [5]
    ]
    label_counts = [card.count(c) for c in set(card)]
    return ordered_types.index(sorted(label_counts, reverse=True))

with open("input.txt", "r") as f:
    cards = f.read().splitlines()
    cards_bets = (parse(card) for card in cards)
    res = []
    for c, b in cards_bets:
        res.append([create_type(c), *encode_card(c), b])
    res = sorted(res, key=lambda x: x[:-1])
    amount = sum(rank * card[-1] for rank, card in enumerate(res, start=1))
    print(amount)
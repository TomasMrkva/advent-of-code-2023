def parse(card: str):
    a, b = card.split()
    return (a, int(b))

def encode_card(card: str):
    order = 'J23456789TJQKA'
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
    label_counts = [card.count(c) for c in set(card.replace('J', ''))] or [0]
    label_counts.sort(reverse=True)
    # label_counts = update_jokers(label_counts, card.count('J'))
    label_counts[0] += card.count('J')
    return ordered_types.index(label_counts)

# def update_jokers(label_counts: list[int], n: int):
#     if n == 0: return label_counts
#     label_counts[0] += 1
#     return update_jokers(label_counts, n-1)    

with open("input.txt", "r") as f:
    cards = f.read().splitlines()
    cards_bets = (parse(card) for card in cards)
    res = []
    for c, b in cards_bets:
        res.append([create_type(c), *encode_card(c), b])
    res = sorted(res, key=lambda x: x[:-1])
    amount = sum(rank * card[-1] for rank, card in enumerate(res, start=1))
    print(amount)
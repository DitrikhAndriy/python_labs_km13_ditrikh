suits = ["diamonds", "clubs", "hearts", "spades"]
cards = ["A", *range(2,11), "J", "Q", "K"]

def pack():
    for suit in suits:
        for card in cards:
            yield f"{card} {suit}"

packing = pack()
while packing:
    print(next(packing))